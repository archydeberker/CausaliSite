import os
import sys
import logging
from postmark import PMMail
from django.conf import settings
import datetime
import random

choiceStr = ["SHOULD","SHOULDN'T"]
meditate = random.randrand(0,2)

message = PMMail(api_key = os.environ.get('POSTMARK_API_TOKEN'),
                 subject = "Email job",
                 sender = "a@deberker.com",
                 to = "a@deberker.com",
                 text_body = "Sent at " + datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S') + ". Today you " + choiceStr[meditate] + "meditate!" ,
                 tag = "hello")

settings.configure()

message.send()

import pymongo
uri = os.environ['MONGO_URI']
client = pymongo.MongoClient(uri)
usersCol = client['zapscience'].users
usersCol.insert({'name': "archy", 'email': "a@deberker.com",'meditate_today':meditate})
client.close()

