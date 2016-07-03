# This sends an email to a newly signed up User, confirming their signup and adding them to the database.
# This supercedes the template archyEmail.py

import os
import sys
import logging
from postmark import PMMail
from django.conf import settings

def confirm_signup_meditation(name="Tester", email="a@deberker.com"):
	"""Sends a welcome message to a user.
	Called by signup_meditation.py. Make sure to use a valid email address, otherwise Postmark gets angry.

	"""
	message = PMMail(api_key = os.environ.get('POSTMARK_API_TOKEN'),
		#,'4322111a-0d75-4777-8111-2d83f0664762'
	                 subject = "Welcome to Causali!" ,
	                 sender = "a@deberker.com",
	                 to = email,
	                 # html_body = "Hey %s! <br><br>Welcome to your very own science lab. You've signed up for the meditation experiment.<br><em>We'll send you your first trial tomorrow!</em>" % name,
	                 html_body = """
	                 Hey %s!

	                 Welcome to your very own science lab. You've signed up for the meditation experiment.

	                 <em>We'll send you your first trial tomorrow!</em>

	                 Warmly,

	                 The Causali team
	                 """ % name
	                 tag = "welcome")

	settings.configure()
	message.send()