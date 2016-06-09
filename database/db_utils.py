	# import packages

import pymongo
import sys
import os
import datetime
from bson.objectid import ObjectId # to be able to query _id in mongo
import numpy as np
import hashlib
import mail.ProbeEmail as ProbeEmail
import pandas as pd
from itertools import groupby




# find the database URI. If not available in the environment, use local mongodb host
# URI = os.getenv('MONGO_URI', 'mongodb://localhost')
URI = 'mongodb://peter:test@ds011943.mlab.com:11943/zapscience' # FOR DEV ONLY

# function definitions that can be used by other scripts
def open_connection(URI=URI, db='zapscience', collectionName='users'):
	""" Opens connection and returns connection details
	Inputs
		URI 			server to connect to (includes credentials)
		db 				database to connect to
		collectionName	what collection to set up
	Returns
		client 			handle to server
		db_handle 		handle to database
		coll_handle 	handle to collection (e.g. can now do coll.find({}))

	Example
		client, db, collection = open_connection(collectionName='users')
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


def store_user(name, email, timezone=0):
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
	
	client, db, collection = open_connection(collectionName='users')
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


def register_user_experiment(name, email, timezone, exp_name, condition1, nTrials1, condition2, nTrials2, dependents, ITI, instruction_time, response_time):
	"""First point of contact after user designs a custom experiment.

	Initialises the user, experiment, trials and results. Inputs come from welcome_custom_exp.php and
	index_full_exp.html

	Returns
		success 			if things go wrong at any point (not valid email, or anything else), returns a False so we can let user know it didn't work
	"""
	print("Storing user experiment...")
	print(exp_name)
	# input checking and default settings
	if (not name) or (not email):
		return False
	if not timezone:
		timezone = 0
	else: # convert to int
		timezone = int(timezone)
	if not exp_name:
		exp_name = 'My Experiment'
	# store conditions, either default or user provided
	conditions = []
	if not condition1:
		conditions.append('condition1')
	else:
		conditions.append(condition1)
	if not condition2:
		conditions.append('condition2')
	else:
		conditions.append(condition2)
	# store nTrials
	nTrials = []
	if not nTrials1:
		nTrials.append(10)
	else:
		nTrials.append(int(nTrials1))
	if not nTrials2:
		nTrials.append(10)
	else:
		nTrials.append(int(nTrials2))
	if not dependents:
		dependents = ['happiness']
	if not ITI:
		ITI = 24
	else:
		ITI = int(ITI)
	if not instruction_time:
		instruction_time = 7
	else:
		instruction_time = int(instruction_time)
	if not response_time:
		response_time = 15
	else:
		response_time = int(response_time)

	user = store_user(name, email, timezone)
	exp = store_experiment(exp_name, conditions, dependents, nTrials, instruction_time, response_time, ITI)
	init_trials(str(user.inserted_id), str(exp.inserted_id))
	init_results(str(user.inserted_id), str(exp.inserted_id))
	print("Successfully registered user, stored experiment, and initiated trials and results.")
	sys.stdout.flush()
	return True


def init_trials(user_id, experiment_id):
	""" Initialises all the trials for an experiment for a user, reading a document in the 'experiments' database and populating the 'trials' collection.

	This assumes that the experiment already exists in the database, and simply reads out the experiments and makes sure all reminders are set, timezones are corrected for,
	and order of conditions is randomised
	Inputs
		user_id 		string, not an ObjectId
		experiment_id 	string, not an ObjectId

	Returns
		input_result	array of insert results
	"""
	# get a handle to the users collection and experiments collection
	client, db_handle, users_coll = open_connection(collectionName='users')
	experiments_coll = db_handle['experiments']
	# get information about the user and store it into variable using next()
	user = users_coll.find_one({"_id": ObjectId(user_id)})
	# get information about the experiment and store it into the variable using next()
	exp = experiments_coll.find_one({"_id": ObjectId(experiment_id)})
	# create an array of all the condition strings
	condition_array = []
	for ix, con in enumerate(exp["conditions"]): # iterate over each condition in the experiment
		# append the condition with appropriate number of replications
		condition_array += ([con] * exp["nTrials"][ix])
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
			np.random.shuffle(condition_array)
			# check if restraint is satisfied
			# https://stackoverflow.com/questions/29081226/limit-the-number-of-repeats-in-pseudo-random-python-list
			if all(len(list(group)) <= 3 for _, group in groupby(condition_array)):
				satisfied = True
	if not satisfied:
		print('did not reach criterion for randomising; using current state of condition_array instead')
	
	# get the first condition email and response request. We can then just add 24 hours to each of these
	first_instruction_datetime = datetime.datetime.combine(  # first define the date and time in UTC
			datetime.date.today() + datetime.timedelta(days=1), # tomorrow's date
			datetime.time(hour=exp["instruction_prompt"]) # the time of day to send the prompt
		) + datetime.timedelta(hours=user["timezone"]) # then add a delta based on the timezone
	first_response_datetime = datetime.datetime.combine( # first define the date and time in UTC
			datetime.date.today() + datetime.timedelta(days=1), # tomorrow's date
			datetime.time(hour=exp["response_prompt"]) # the time of day to send the prompt
		) + datetime.timedelta(hours=user["timezone"]) # then add a delta based on the timezone

	# insert each trial into database.
	insert_result = []
	for ix, condition in enumerate(condition_array):
		insert_result.append(db_handle['trials'].insert_one({
			'user_id': user_id,
			'experiment_id': experiment_id,
			'trial_number': ix,
			'condition': condition,
			'instruction_sent': False,
			'response_request_sent': False,
			'response_given': False,
			'instruction_date': first_instruction_datetime + datetime.timedelta(hours=ix * exp["ITI"]), # add one day for each next trial
			'response_date': first_response_datetime + datetime.timedelta(hours=ix * exp["ITI"]), # ditto
			'created_at': datetime.datetime.utcnow(),
			'last_modified': datetime.datetime.utcnow(),
			'random_number': np.random.random(),
			'hash_sha256': hashlib.sha256(user_id+experiment_id+str(ix)+str(np.random.random())).hexdigest() # add a random hash, because if you don't add the np.random.random() then the same user doing experiment twice will go messed up
		}))
	return insert_result
		
		
def init_results(user_id, experiment_id):
	""" initialise the results document for a user's experiment

	Inputs
		user_id			string, should match an _id in users collection
		experiment_id 	string, should match an _id in experiments collection

	Returns
		insert_result 	see insert_result.inserted_id for _id of inserted document
	"""
	client, db_handle, results_coll = open_connection(collectionName='results')
	insert_result = results_coll.insert_one({
		'user_id': user_id,
		'experiment_id': experiment_id,
		'created_at': datetime.datetime.utcnow(),
		'last_modified': datetime.datetime.utcnow(),
	})
	return insert_result

		
def store_experiment(exp_name=['My Experiment'], conditions=['condition1', 'condition2'], dependents=['happiness'], nTrials=[10, 10], instruction_prompt=7, response_prompt=15, ITI=24, randomise='max3'):
	"""Store a custom experiment.

	See default values for format of input.

	"""
	# open a new connection
	client, db, collection = open_connection(collectionName='experiments')
	# fill with single experiment. Does not check for unique name 
	insert_result = collection.insert_one({
		'name': exp_name,
		'conditions': conditions,
		'dependent_vars': dependents,
		'nTrials': nTrials,
		'instruction_prompt': instruction_prompt, #time of day in hours between 0 and 24
		'response_prompt': response_prompt, #time of day in hours between 0 and 24
		'ITI': ITI, # set the ITI between trials in hours
		'randomise': randomise, #how to randomise; see init_trials() for implementation
		'created_at': datetime.datetime.utcnow(),
		'last_modified': datetime.datetime.utcnow(),
	})
	return insert_result


def init_experiment_meditation():
	""" temporary code to initialise the meditation experiment in the database. Helpful to identify what variables to store and how to name them
	
	Returns an instance of pymongo InsertOneResult, e.g. insert_result.inserted_id 
	to get the ID of inserted document
	"""
	# open a new connection
	client, db, collection = open_connection(collectionName='experiments')
	# fill with single experiment. Does not check for unique name 
	insert_result = collection.insert_one({
		'name': 'meditation',
		'conditions': ["meditate", "do not meditate"],
		'dependent_vars': ["happiness"],
		'nTrials': [10, 10],
		'instruction_prompt': 7, #time of day in hours between 0 and 24
		'response_prompt': 15, #time of day in hours between 0 and 24
		'ITI': 24, # set the ITI between trials in hours
		'randomise': 'complete', #how to randomise; see init_trials() for implementation
		'created_at': datetime.datetime.utcnow(),
		'last_modified': datetime.datetime.utcnow(),
	})
	return insert_result
	

def get_uncompleted_instructions(include_past=True, include_future=False, sort='chronological', limit=0):
	""" Looks at 'trials' database and return a list of uncompleted instructions 

	This should be useful e.g. for a CRON job to check if anything needs to be sent.

	Inputs
		include_past 		if True, includes uncompleted events in the past (before current time)
		include_future 		if True, includes uncompleted events in the future
		sort				how to sort the resulting list, should be 'chronological' or anything else for anti-chronological
		limit 				integer, maximum number of documents to return

	Returns
		instructions 		sorted list of dictionaries representing instructions
	"""
	# get current datetime in format that mongodb understands
	right_now = datetime.datetime.utcnow()
	if include_past and include_future:
		datesearch = {}
	elif include_past and not include_future:
		datesearch = {'instruction_date': {"$lte": right_now}}
	elif not include_past and include_future:
		datesearch = {'instruction_date': {"$gte": right_now}}
	elif not include_past and not include_future: # this is retarded of course
		datesearch = {'instruction_date': right_now}
	# update original query with additional constraints on what documents to return
	instruction_query = {'instruction_sent': False}
	instruction_query.update(datesearch)
	# set sort
	if sort == 'chronological':
		sort_as = pymongo.ASCENDING
	else:
		sort_as = pymongo.DESCENDING

	# get connection to database
	client, db, collection = open_connection(collectionName='trials')
	# execute query and return as list of dicts
	return list(collection.find(instruction_query).sort('instruction_date', sort_as).limit(limit))


def get_uncompleted_response_prompts(include_past=True, include_future=False, sort='chronological', limit=0):
	""" Looks at 'trials' database and return a list of uncompleted response prompts 

	This should be useful e.g. for a CRON job to check if anything needs to be sent.

	Inputs
		include_past 		if True, includes uncompleted events in the past (before current time)
		include_future 		if True, includes uncompleted events in the future
		sort				how to sort the resulting list, should be 'chronological' or anything else for anti-chronological
		limit 				integer, maximum number of documents to return

	Returns
		instructions 		sorted list of dictionaries representing response prompts
	"""
	# get current datetime in format that mongodb understands
	right_now = datetime.datetime.utcnow()
	if include_past and include_future:
		datesearch = {}
	elif include_past and not include_future:
		datesearch = {'response_date': {"$lte": right_now}}
	elif not include_past and include_future:
		datesearch = {'response_date': {"$gte": right_now}}
	elif not include_past and not include_future: # this is retarded of course
		datesearch = {'response_date': right_now}
	# update original query with additional constraints on what documents to return
	response_query = {'response_request_sent': False}
	# response_query.update(datesearch)
	# set sort
	if sort == 'chronological':
		sort_as = pymongo.ASCENDING
	else:
		sort_as = pymongo.DESCENDING

	# get connection to database
	client, db, collection = open_connection(collectionName='trials')
	# execute query and return as list of dicts
	return list(collection.find(response_query).sort('response_date', sort_as).limit(limit))


def store_response(trial_hash, response):
	"""Stores a trial response and sets the flags to indicate response is received.

	Inputs
		trial_hash			should match a hash_sha256 in the 'trials' collection
		response 			a response in the format of the dependent variable of the experiment
	"""
	# open connection to trials database
	client, db_handle, trials_coll = open_connection(collectionName='trials')
	# check the has is in the database
	doc = trials_coll.find_one({"hash_sha256": trial_hash})
	if not doc: # if doc cannot be found
		print("could not find the document with hash %s" % trial_hash)
		return None
	# deposit result
	trials_coll.update_one({"hash_sha256": trial_hash}, {
		'$set': {
			'response_given': True,
			'trialRating': response
		},
		"$currentDate": {
			'last_modified': True
		}
	})


def send_outstanding_response_prompts():
	"""Uses get_uncompleted_response_prompts() to get to-do list, then sends emails.

	"""
	outstanding = get_uncompleted_response_prompts(include_past=True, include_future=False)
	if not outstanding: # if list is empty
		print("no outstanding response prompts")
		return None

	client, db_handle, users_coll = open_connection(collectionName='users')
	trials_coll = db_handle["trials"]
	# at this stage there are outstanding response prompts
	for prompt in outstanding:
		# get the user
		user = users_coll.find_one({"_id": prompt['user_id']})
		result = ProbeEmail.ProbeEmail(trialHash=prompt['hash_sha256'], userName=user['first_name'], userEmail=user['email'])
		# TO DO check that result is correct and only continue if correct
		#################

		# store that instruction is sent, set the time instruction was sent, and update last_modified
		trials_coll.update_one({"_id": prompt["_id"]}, {
			"$set": {
				"response_request_sent": True
			}, 
			"$currentDate": {
				"response_request_sent_date": True, 
				"last_modified": True
			}
		})


def send_outstanding_instructions():
	"""Uses get_uncompleted_response_prompts() to get to-do list, then sends emails.

	"""
	outstanding = get_uncompleted_instructions(include_past=True, include_future=False)
	if not outstanding: # if list is empty
		print("no outstanding instructions")
		return None

	client, db_handle, users_coll = open_connection(collectionName='users')
	trials_coll = db_handle["trials"]
	# at this stage there are outstanding response prompts
	for prompt in outstanding:
		# get the user
		user = users_coll.find_one({"_id": prompt['user_id']})
		INSTRUCTION_EMAIL_FUNCTION_DOES_NOT_EXIST_YET(trialHash=prompt['hash_sha256'], userName=user['first_name'], userEmail=user['email'], condition=prompt['condition'])
		# store in the trials collection that the instruction has been sent and exact datetime
		trials_coll.update_one({"_id": prompt["_id"]}, {
			"$set": {
				"instruction_sent": True
			}, 
			"$currentDate": {
				"instruction_sent_date": True, 
				"last_modified": True
			}
		})


def trials_completed(filter={}):
	"""Returns number of completed trials for a particular filter.

	Queries the trials collection and looks for completed trials.
	Input
		filter 			passed to mongodb .find. Could e.g. filter by a particular experiment or user

	Returns
		integer with number of completed trials

	"""
	client, db_handle, trials_collection = open_connection(collectionName='trials')
	# construct the query for completed trials
	query = {
		'instruction_sent': True,
		'response_request_sent': True, 
		'response_given': True
		}
	# apply the filter
	query.update(filter)
	# search and return the number of retrieved docs
	return trials_collection.find(query).count()


def update_results(results_filter={}):
	"""Updates every doc in the 'results' collection that fits the filter
	
	First finds all results that satisfy the filter, and then loops over them to update.
	Filter might contain something like last_modified, a particular results _id, a user, experiment,
	and so on. 

	Input
		results_filter 		a filter passes directly to mongodb to select documents in the 'results' collection

	"""
	# open connection
	client, db, results_collection = open_connection(collectionName='results')
	# get documents to update
	docs = results_collection.find(results_filter)
	# loop over each document
	for doc in docs:
		# get all trials for this user and this experiment
		# and put into a list
		trials = pd.DataFrame(list(db['trials'].find({
			"experiment_id": doc["experiment_id"], 
			"user_id": doc["user_id"]
		})))
		# get experiment to read out conditions
		exp = db['experiments'].find_one({'_id': ObjectId(doc['experiment_id'])})
		# generate as many lists as conditions, each with a numpy array
		# with non-NaN scores for that condition.
		# This will make it easier to do things like std, mean, median, t-tests, f-tests
		dat = [np.array(trials[(trials.condition == cond) & (trials.response_given)].trialRating) for cond in exp['conditions']]
		# now update the results doc, calculating some measures along the way
		print doc["_id"]
		results_collection.update_one({"_id": doc["_id"]}, {
			"$set": {
				"n_completed": int(np.sum(trials.response_given)),
				"proportion_complete": float(np.sum(trials.response_given)/len(trials.index)),
				"response_rate": float(np.sum(trials.response_given)/np.sum(trials.response_request_sent)),
			 	"mean_score": float(np.nanmean(trials.trialRating)),
				"mean_score_per_condition": [np.mean(cond) for cond in dat],
				"std_score_per_condition": [np.std(cond) for cond in dat],
				"median_score_per_condition": [np.median(cond) for cond in dat],
				"scores_per_condition": [list(cond) for cond in dat],
				"Cohen_effect_size_0_minus_1": (np.mean(dat[0])-np.mean(dat[1])) / np.sqrt(((len(dat[0])-1)*np.var(dat[0]) + (len(dat[1])-1)*np.var(dat[1])) /	(len(dat[0])+len(dat[1]))),
			},
			"$currentDate": {
				"last_modified": True
			}
		})


def delete_user(_id):
	"""Delete a user
	
	Input
		_id			string, will be converted to ObjectId

	Returns
		DeleteResult result (.deleted_count)
	"""
	_, _, coll = open_connection(collectionName='users')
	return coll.delete_one({'_id': ObjectId(_id)})


def delete_experiment(_id):
	"""Delete an experiment

	Input
		_id 		string, will be converted to ObjectId

	Returns
		DeleteResult
	"""
	_, _, coll = open_connection(collectionName='experiments')
	return coll.delete_one({'_id': ObjectId(_id)})


def delete_trials(trial_list):
	"""Takes a list of trial id strings and delete these trials

	Input
		trial_list		an iterable that contains _id strings
	Returns
		a list of DeleteResults
	"""
	_, _, coll = open_connection(collectionName='trials')
	result = []
	for _id in trial_list:
		result.append(coll.delete_one({'_id': ObjectId(_id)}))
	return result


def delete_result(_id):
	"""Delete a result doc

	Input
		_id 		string, will be converted to ObjectId

	Returns
		DeleteResult
	"""
	_, _, coll = open_connection(collectionName='results')
	return coll.delete_one({'_id': ObjectId(_id)})


# References
## Bulk operations in mongoDB: http://stackoverflow.com/a/36213728