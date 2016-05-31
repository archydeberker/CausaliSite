# This sends an email to a newly signed up User, confirming their signup and adding them to the database.
# This supercedes the template archyEmail.py

import os
import sys
import logging
from postmark import PMMail
from django.conf import settings
import database.db_utils as db_utils

print sys.argv[1]
print sys.argv[2]

message = PMMail(api_key = os.environ.get('POSTMARK_API_TOKEN'),
	#,'4322111a-0d75-4777-8111-2d83f0664762'
                 subject = "Welcome to Causali!" ,
                 sender = "zapscience@gmail.com",
                 to = sys.argv[2],
                 text_body = "Hey " + sys.argv[1] + " Thanks for signing up for your first experiment. We'll send you your first trial tomorrow!",
                 tag = "welcome")

settings.configure()

message.send()

# write to database
db_utils.store_user(name=sys.argv[1], email=sys.argv[2])	