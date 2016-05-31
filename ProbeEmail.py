# This sends a probe email to a specified user using a trial hash

# Inputs:
	# Name
	# Email
	# Hash for that trial

def ProbeEmail(userEmail,trialHash)

	import os
	import sys
	import logging
	from postmark import PMMail
	from django.conf import settings
	import database.db_utils as db_utils

	mostofpath= """<a href="https://zapscience.herokuapp.com/sendresults.php?trialhash=""" + trialHash + "&rating="
	restofpath= """><img src="https://zapscience.herokuapp.com/star.png"></a>"""
	bodyText = "<html><body> Sup. How'd it go?<br>" +\
		mostofpath + "1\""  + restofpath +\
		mostofpath + "2\""  + restofpath +\
		mostofpath + "3\""  + restofpath +\
		mostofpath + "4\""  + restofpath +\
		mostofpath + "5\""  + restofpath + "</body> </html>"

	print bodyText

	message = PMMail(api_key = os.environ.get('POSTMARK_API_TOKEN'),
		#,'4322111a-0d75-4777-8111-2d83f0664762'
	                 subject = "Welcome to Causali!" ,
	                 sender = "a@deberker.com",
	                 to = userEmail,
	                 html_body = bodyText,
	                 tag = "welcome")

	settings.configure()


	message.send()