import os
import sys
import logging
from postmark import PMMail
from django.conf import settings


message = PMMail(api_key = os.environ.get('POSTMARK_API_TOKEN'),
                 subject = "first part of concatenated string " + sys.argv[2],
                 sender = "a@deberker.com",
                 to = "a@deberker.com",
                 text_body = sys.argv[1],
                 tag = "hello")

settings.configure()

message.send()

import pymongo
uri = os.environ['MONGO_URI']
client = pymongo.MongoClient(uri)
usersCol = client['zapscience'].users
usersCol.insert({'name': sys.argv[1], 'email': sys.argv[2]})
client.close()
