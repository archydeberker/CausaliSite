# import packages
import pymongo
import sys
import os
import datetime
from bson.objectid import ObjectId # to be able to query _id in mongo
import numpy as np

# find the database URI. If not available in the environment, use local mongodb host
URI = os.getenv('MONGO_URI', 'mongodb://localhost')

# function definitions that can be used by other scripts
def open_connection(URI=URI, db='zapscience', collectionName='users'):
	""" Opens connection and returns connection details
	Input:
		URI 			server to connect to (includes credentials)
		db 				database to connect to
		collectionName	what collection to set up
	Returns
		client 			handle to server
		db_handle 		handle to database
		coll_handle 	handle to collection (e.g. can now do coll.find({}))

	"""
	client = pymongo.MongoClient(URI)
	db_handle = client[db]
	coll_handle = db_handle[collectionName]
	return client, db_handle, coll_handle


def close_connection(client):
	"""Close a connection
	Input:
		client 		class is pymongo.MongoClient() as generated by open_connection()
	"""
	client.close()


def store_user(name, email, collection=None, timezone=0):
	""" Store user info in a collection.
	As I understand it you don't have to sanitise inputs in MongoDB unless you're concatenating strings.
	Instead of using the has we can use the objectID in the mongoDB database, which is unique. 
	HOWEVER, IT MIGHT BE EASY TO PREDICT WHAT OTHER OBJECT IDS LOOK LIKE BASED ON YOUR OWN, so
	should probably start using a random string at some point. 
	
	Input:
		name 		string
		email 		string
		collection 	pymongo handle to collection, as provided by open_connection(). If not provided, opens connection using open_connection()
		timezone 	number (int or float) indicating offset from UTC (should use proper timezone stuff [pytz] at some point, but too big a hassle for now)
	Returns:
		result 		contains unique id of user as insert_results.inserted_id
	"""
	# get default collection if none is provided
	if not collection:
		client, db, collection = open_connection()
	# write the user info to the database
	result = collection.insert_one({
		'name': name,
		'email': email,
		'created_at': datetime.datetime.utcnow(),
		'last_modified': datetime.datetime.utcnow(),
		'timezone': timezone,
		'first_name': name.partition(' ')[0] # get the first part of the name until a space (or whole thing if no space)
		})
	return result 

	
def init_trials(user_id, experiment_id):
	""" Initialises all the trials for an experiment for a user, reading a document in the 'experiments' database and populating the 'trials' collection.

	This assumes that the experiment already exists in the database, and simply reads out the experiments and makes sure all reminders are set, timezones are corrected for,
	and order of conditions is randomised
	Inputs
		user_id 		string, not an ObjectId
		experiment_id 	string, not an ObjectId
	"""
	# get a handle to the users collection and experiments collection
	client, db_handle, users_coll = open_connection(collectionName='users')
	experiments_coll = db_handle['experiments']
	# get information about the user and store it into variable using next()
	user = list(users_coll.find({"_id": ObjectId(user_id)}))[0]
	# get information about the experiment and store it into the variable using next()
	exp = list(experiments_coll.find({"_id": ObjectId(experiment_id)}))[0]
	# create an array of all the condition strings
	condition_array = []
	for ix, con in enumerate(exp["conditions"]): # iterate over each condition in the experiment
		# append the condition with appropriate number of replications
		condition_array += ([con] * exp["nTrials"][ix])
	# do not re-seed the RNG but check it's not the same number coming out every time (in which case, seed with os.urandom)
	print('numpy-generated random number: %.10f' % np.random.random())
	# shuffle the array depending on requested method, either 1000 times or until satisfied. Wouldn't want to crash the server
	satisfied = False
	iterations = 0
	while (not satisfied) and (iterations<1000):
		# increase iterations 
		iterations += 1
		# select randomisation method
		if exp["randomise"] == 'complete':
			# completely random, no restraints on ordering
			np.random.shuffle(condition_array)
			satisfied = True
		elif exp["randomise"] == 'max3':	
			# shuffle in some way that maximally 3 times in a row the same condition is given
			random.shuffle(condition_array)
			# check if restraint is satisfied
			# https://stackoverflow.com/questions/29081226/limit-the-number-of-repeats-in-pseudo-random-python-list
			if all(len(list(group)) <= 3 for _, group in groupby(condition_array)):
				satisfied = True
	if not satisfied:
		print('did not reach criterion for randomising; using current state of condition_array instead')
	
	# get the first condition email and response request. We can then just add 24 hours to each of these
	first_instruction_datetime = datetime.datetime.combine(  # first define the date and time in UTC
			datetime.date.today() + datetime.timedelta(days=1), # tomorrow's date
			datetime.time(hour=exp["condition_prompt"]) # the time of day to send the prompt
		) + datetime.timedelta(hours=user["timezone"]) # then add a delta based on the timezone
	first_response_datetime = datetime.datetime.combine( # first define the date and time in UTC
			datetime.date.today() + datetime.timedelta(days=1), # tomorrow's date
			datetime.time(hour=exp["response_prompt"]) # the time of day to send the prompt
		) + datetime.timedelta(hours=user["timezone"]) # then add a delta based on the timezone

	# insert each trial into database
	for ix, condition in enumerate(condition_array):
		db_handle['trials'].insert_one({
			'user_id': user_id,
			'experiment_id': experiment_id,
			'trial_number': ix,
			'condition': condition,
			'instruction_sent': False,
			'response_request_sent': False,
			'response_given': False,
			'condition_date': first_instruction_datetime + datetime.timedelta(hours=ix * exp["ITI"]), # add one day for each next trial
			'response_date': first_response_datetime + datetime.timedelta(hours=ix * exp["ITI"]), # ditto
			'created_at': datetime.datetime.utcnow(),
			'last_modified': datetime.datetime.utcnow(),
		})
		
		
def init_results(user_id, experiment_id):
	""" initialise the results document for a user's experiment
	"""
	client, db_handle, results_coll = open_connection(collectionName='results')
	insert_result = results_coll.insert_one({
		'user_id': user_id,
		'experiment_id': experiment_id,
		'created_at': datetime.datetime.utcnow(),
		'last_modified': datetime.datetime.utcnow(),
	})
	return insert_result

		
def init_experiment_meditation():
	""" temporary code to initialise the meditation experiment in the database. Helpful to identify what variables to store and how to name them
	Returns an instance of pymongo InsertOneResult, e.g. insert_result.inserted_id to get the ID of inserted document
	
	"""
	# open a new connection
	client, db, collection = open_connection()
	# set the experiments collection
	collection = db['experiments']
	# fill with single experiment. Does not check for unique name 
	insert_result = collection.insert_one({
		'name': 'meditation',
		'conditions': ["meditate", "do not meditate"],
		'dependent_vars': ["happiness"],
		'nTrials': [10, 10],
		'condition_prompt': 7, #time of day in hours between 0 and 24
		'response_prompt': 15, #time of day in hours between 0 and 24
		'ITI': 24, # set the ITI between trials in hours
		'randomise': 'complete', #how to randomise; see init_trials() for implementation
		'created_at': datetime.datetime.utcnow(),
		'last_modified': datetime.datetime.utcnow(),
	})
	
	return insert_result
	
