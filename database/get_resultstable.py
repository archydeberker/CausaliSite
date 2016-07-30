# Get all results for a given user and return as a json object

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.join(os.path.realpath(__file__))), os.pardir)))
import db_utils as db
import pymongo
from mail.email_defs import confirm_signup_meditation

experiment_id = sys.argv[1]
user_id = sys.argv[2]

print(experiment_id, user_id)

db.get_results(ObjectID(experiment_id),ObjectID(user_id)
#

print("Finished get_resultstable.py")