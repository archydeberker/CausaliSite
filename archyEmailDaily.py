import os
import sys
import logging
from postmark import PMMail
from django.conf import settings
import datetime



message = PMMail(api_key = os.environ.get('POSTMARK_API_TOKEN'),
                 subject = "Email job",
                 sender = "a@deberker.com",
                 to = "a@deberker.com",
                 text_body = "Sent at " + datetime.datetime.now().time(),
                 tag = "hello")

settings.configure()

message.send()

