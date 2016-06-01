#import packages
import os
import sys
import logging
from django.conf import settings
import database.db_utils as db_utils
import pymongo
from bson.objectid import ObjectId # to be able to query _id in mongo

# these variables are passed in
trialHash 	= sys.argv[1]
trialRating = sys.argv[2]

# setup connection to the database
uri 		= os.environ['MONGO_URI']
client 		= pymongo.MongoClient(uri)
usersCol 	= client['zapscience'].trials

# use Hash tag
trialID 	= "803faa43b47173aee6c0a38b2f5eabdd7121ea0edc9d1c2ab902c56ce5995a57"

# now update the relevant entry
usersCol.update_one({'hash_sha256': trialID}, {'$set': {'response_given': True, 'trialRating': trialRating}, "$currentDate": {'last_modified': True}})

client.close()