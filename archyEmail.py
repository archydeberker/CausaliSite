import os
from postmark import PMMail

message = PMMail(api_key = os.environ.get('POSTMARK_API_TOKEN'),
                 subject = "Hello from Postmark",
                 sender = "a@deberker.com",
                 to = "a@deberker.com.com",
                 text_body = "Hello",
                 tag = "hello")

message.send()