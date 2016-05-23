# import packages
import pymongo
import sys
import os
import hashlib
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


def store_user(name, email, collection=None):
	""" Store user info in a collection.
	As I understand it you don't have to sanitise inputs in MongoDB unless you're concatenating strings.
	Adds a hash of the email, not necessarily unique
	Input:
		name 		string
		email 		string
		collection 	pymongo handle to collection, as provided by open_connection(). If not provided, opens connection using open_connection()
	Returns:
		_id 		_id (unique ID) of written doc 
	"""
	# get default collection if none is provided
	if not collection:
		client, db, collection = open_connection()
	# write the user info to the database
	result = collection.insert_one({
		name: name,
		email: email,
		hashID: hash(email), # hashed version of email using the custom function in this doc
		created_at:  datetime.datetime.utcnow(),
		last_updated: datetime.datetime.utcnow(),
		first_name: name.partition(' ')[0] # get the first part of the name until a space (or whole thing if no space)
		})
	return result._id


def hash(str):
	# hashes a string using hashlib
	# https://docs.python.org/2/library/hashlib.html
	return hashlib.sha224(str).hexdigest()