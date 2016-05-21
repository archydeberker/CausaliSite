import os
from postmark import PMMail
from django.conf import settings


message = PMMail(api_key = os.environ.get('POSTMARK_API_TOKEN'),
                 subject = "Hello from Postmark",
                 sender = "a@deberker.com",
                 to = "a@deberker.com",
                 text_body = "Hello",
                 tag = "hello")

settings.configure()

message.send()

print 'Email Sent Successfully'