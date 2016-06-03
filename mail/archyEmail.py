import os
import sys
import logging
from postmark import PMMail
from django.conf import settings
import database.db_utils as db_utils


message = PMMail(api_key = os.environ.get('POSTMARK_API_TOKEN'),
	#,'4322111a-0d75-4777-8111-2d83f0664762'
                 subject = "first part of concatenated string " + sys.argv[2],
                 sender = "a@deberker.com",
                 to = "a@deberker.com",
                 text_body = sys.argv[1],
                 tag = "hello")

settings.configure()

message.send()

# write to database
db_utils.store_user(name=sys.argv[1], email=sys.argv[2])	