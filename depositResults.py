#import packages
import os
import sys
import logging
from django.conf import settings
import database.db_utils as db_utils
import pymongo

# these variables are passed in
trialHash 	= sys.argv[1]
trialRating = sys.argv[2]

# setup connection to the database
uri 		= os.environ['MONGO_URI']
client 		= pymongo.MongoClient(uri)
usersCol 	= client['zapscience'].trials

trialID 	= "574dfa79dee0ae00032ad982"


# now update the relevant entry
usersCol.update_one({'_id': trialID}, {'$set': {'response_given': True, 'trialRating': trialRating}, "$currentDate": {'last_modified': True}})

client.close()