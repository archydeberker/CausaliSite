# import packages
import pymongo
import sys
import os
import datetime

# find the database URI. If not available in the environment, assume running locally
try: # will fail if no MONGO_URI in environment
	URI = os.environ['MONGO_URI']
except NameError:
	print('no environment mongoDB URI found, using local server')
	URI = 'mongodb://localhost'

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
		_id 		_id (unique ID) of written user 
	"""
	# get default collection if none is provided
	if not collection:
		client, db, collection = open_connection()
	# write the user info to the database
	result = collection.insert_one({
		'name': name,
		'email': email,
		'created_at':  datetime.datetime.utcnow(),
		'last_updated': datetime.datetime.utcnow(),
		'timezone': timezone,
		'first_name': name.partition(' ')[0] # get the first part of the name until a space (or whole thing if no space)
		})
	return result.inserted_id

	
def init_trials(user_id, experiment_id, ):
	""" Initialises all the trials for an experiment for a user, reading a document in the 'experiments' database and populating the 'trials' database with trials
	This assumes that the experiment already exists in the database, and simply reads out the experiments and makes sure all reminders are set, timezones are corrected,
	and order of conditions is randomised
	"""

	
		
def init_experiment_meditation():
	""" temporary code to initialise the meditation experiment in the database. Helpful to identify what variables to store and how to name them
	
	"""
	# open a new connection
	client, db, collection = open_connection()
	# set the experiments collection
	collection = db['experiments']
	# fill with single experiment, replacing if duplicate name exists FOR DEBUGGING PURPOSES (otherwise you get tons of entries for meditation)
	# and inserting if it doesn't exist yet.
	collection.update_one({'name': 'meditation'}, {
		"$set": {
			'name': 'meditation',
			'conditions': ["meditate", "do not meditate"],
			'dependent_vars': ["happiness"],
			'nTrials': np.array([10, 10]),
			'condition_prompt': datetime.time(7), #time of day (first arg is hour of day, 0 to 24
			'response_prompt': datetime.time(15), #time of day
			'randomise': 'max3' #as example for now; indicates max 3 times the same condition in a row
		},
		# set last_modified to the current date
		"$currentDate": 
			{"last_modified": True}
		# set upsert to insert the document if no document is found to update.
		}, upsert=True)
	
	
	