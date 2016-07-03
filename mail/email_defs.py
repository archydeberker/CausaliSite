# This sends an email to a newly signed up User, confirming their signup and adding them to the database.
# This supercedes the template archyEmail.py

import os
from postmark import PMMail

def confirm_signup_meditation(name="Tester", email="a@deberker.com"):
	"""Sends a welcome message to a user.
	Called by signup_meditation.py. Make sure to use a valid email address, otherwise Postmark gets angry.

	"""
	message = PMMail(api_key = os.environ.get('POSTMARK_API_TOKEN'),
	                 subject = "Welcome to Causali!" ,
	                 sender = "a@deberker.com",
	                 to = email,
	                 # html_body = "Hey %s! <br><br>Welcome to your very own science lab. You've signed up for the meditation experiment.<br><em>We'll send you your first trial tomorrow!</em>" % name,
	                 html_body = """
	                 <h2p>Hey %s!</h2>
	                 <p>Welcome to your very own <b>science lab</b>. You've signed up for the <b>meditation experiment</b>.</p>
	                 <p><em>We'll send you your first trial tomorrow at your requested time!</em></p>
	                 <p>Warmly,</p>
	                 <p>The Causali team</p>
	                 """ % name,
	                 tag = "welcome"
             	)
	result = message.send()
	return result

def probe_meditation(userName,userEmail,trialHash):
	"""sends a probe email to a specified user using a trial hash.

	Inputs
		Name
		Email
		Hash for that trial
	Returns
		result 		should contain info about whether message was successfully sent. Not sure what is in it
	"""

	mostofpath= '<a href="https://zapscience.herokuapp.com/sendresults.php?trialhash=' + trialHash + '&rating='
	restofpath= '><img src="https://zapscience.herokuapp.com/views/star.png"></a>'
	bodyText = ('<html><body> Hi %s,<br><br>It''s time to report back how you''ve been feeling today.<br>' % userName) +\
		mostofpath + '1"'  + restofpath +\
		mostofpath + '2"'  + restofpath +\
		mostofpath + '3"'  + restofpath +\
		mostofpath + '4"'  + restofpath +\
		mostofpath + '5"'  + restofpath +\
		"<br><p>Warmly,<br><br>Your friends at Causali</p>" +\
		"</body> </html>"

	#print bodyText

	message = PMMail(api_key = os.environ.get('POSTMARK_API_TOKEN'),
		#,'4322111a-0d75-4777-8111-2d83f0664762'
	                 subject = userName + ", how are you feeling?" ,
	                 sender = "a@deberker.com",
	                 to = userEmail,
	                 html_body = bodyText,
	                 tag = "response")

	result = message.send()
	return result

def instruct_meditation(userName,userEmail,condition):
	"""Instructs a user to do condition.

	Inputs
		Name
		Email
		string which represents this trial's condition
	Returns
		result 		should contain info about whether message was successfully sent. Not sure what is in it
	"""

	message = PMMail(api_key = os.environ.get('POSTMARK_API_TOKEN'),
		#,'4322111a-0d75-4777-8111-2d83f0664762'
	                 subject = userName + ", today's the day for SCIENCE!" ,
	                 sender = "a@deberker.com",
	                 to = userEmail,
	                 html_body = """
	                 <h2p>Hey %s!</h2>
	                 <p>Hope you're having a great day. As part of your meditation experiment with Causali, today you should:</p>
	                 <h1>%s</h1>
	                 <p><br>Warmly,</p>
	                 <p>The Causali team</p>
	                 """ % (userName, condition.upper()),
	                 tag = "instruction")

	result = message.send()
	return result