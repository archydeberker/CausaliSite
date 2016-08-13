# This sends an email to a newly signed up User, confirming their signup and adding them to the database.
# This supercedes the template archyEmail.py

import os
from postmark import PMMail

# get domain, which will be different depending on staging vs production
domain = os.getenv('DOMAIN', 'http://www.causali.me/')

unsubscribe_string = '<p><small>To unsubscribe and END all experiments associated with %(email)s, click <a href="%(domain)sunsubscribe.php?email=%(email)s" target="_blank">here</a>. Warning: this action cannot be undone.</small></p>' 

def verify_user_by_email(email, user_id, exp_id, name="Tester"):
	"""Sends an email to the user asking them to click a link to verify.
	Called by signup_meditation.py.

	Args:
		email: string with email of user
		user_id: ObjectId of the user_id
		exp_id: ObjectId with exp_id that the user has signed up for. needs to be passed on so once confirmed, we know what exp to activate

	"""
	message = PMMail(api_key = os.environ.get('POSTMARK_API_TOKEN'),
	                 subject = "[Causali] Please confirm your email" ,
	                 sender = "a@deberker.com",
	                 to = email,
	                 html_body = """
	                 <h2p>Hi %(name)s!</h2>
	                 <p>We're getting ready to start you on your first Causali experiment. Before we get started though, <a href="%(confirm_URL)s" target="_blank"><em>please click here to confirm your signup</em></a>.</p>
	                 <p>You can also copy this link into your browser: %(confirm_URL)s
	                 <p>See you soon,</p>
	                 <p>The Causali team</p>
	                 </body></html>
	                 """ % {'name': name, 'confirm_URL': domain + 'verify_signup.php?email=%s&user_id=%s&exp_id=%s' % (email, str(user_id), str(exp_id))},
	                 tag = "verify"
             	)
	result = message.send()
	return result


def confirm_signup_meditation(email="a@deberker.com", name=""):
	"""Sends a welcome message to a user.
	Called by signup_meditation.py. Make sure to use a valid email address, otherwise Postmark gets angry.

	"""
	message = PMMail(api_key = os.environ.get('POSTMARK_API_TOKEN'),
	                 subject = "Welcome to Causali!" ,
	                 sender = "a@deberker.com",
	                 to = email,
	                 # html_body = "Hey %s! <br><br>Welcome to your very own science lab. You've signed up for the meditation experiment.<br><em>We'll send you your first trial tomorrow!</em>" % name,
	                 html_body = """
	                 <h2p>Hi %s</h2>
	                 <p>Welcome to your very own <b>science lab</b>. You've signed up for the <b>meditation experiment</b>.</p>
	                 <p><em>We'll send you your first trial tomorrow at your requested time!</em></p>
	                 <p>Warmly,</p>
	                 <p>The Causali team</p>
	                 <br><br>
	                 %s
	                 </body></html>
	                 """ % (name, unsubscribe_string) % {'email': email, 'domain': domain},
	                 tag = "welcome"
             	)
	result = message.send()
	return result


def probe_meditation(name, email, trialHash):
	"""sends a probe email to a specified user using a trial hash.

	Inputs
		Name
		Email
		Hash for that trial
	Returns
		result 		should contain info about whether message was successfully sent. Not sure what is in it
	"""

	resp 	= '<a href="%(domain)ssendresults.php?trialhash=' % {'domain': domain} + trialHash + '&rating=%(rating)d"><img src="http://www.petersmittenaar.com/media/rating%(rating)d.png"></a>'
	noresp 	=  '<a href="%(domain)ssendresults.php?trialhash=' % {'domain': domain} + trialHash + '&rating=0"> click here to skip today </a><br>'

	bodyText = "<html><body>Hi %s,<br><br>It''s time to report back how you''ve been feeling today.<br>" % name + \
		resp % {'rating': 1} + \
		resp % {'rating': 2} + \
		resp % {'rating': 3} + \
		resp % {'rating': 4} + \
		resp % {'rating': 5} + \
		"<br><br>" + \
		noresp + \
		"<br><p>Warmly,<br><br>Your friends at Causali</p>" + \
		"<br><br>%s" % unsubscribe_string % {'email': email, 'domain': domain} + \
		"</body></html>"

	message = PMMail(api_key = os.environ.get('POSTMARK_API_TOKEN'),
		#,'4322111a-0d75-4777-8111-2d83f0664762'
	                 subject = name + ", how are you feeling?" ,
	                 sender = "a@deberker.com",
	                 to = email,
	                 html_body = bodyText,
	                 tag = "response")

	result = message.send()
	return result


def instruct_meditation(name, email, condition):
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
	                 subject = "%s, today you should: %s" % (name, condition.upper()),
	                 sender = "a@deberker.com",
	                 to = email,
	                 html_body = """
	                 <html><body>
	                 <h2p>Hey %s!</h2>
	                 <p>Hope you're having a great day. As part of your meditation experiment with Causali, today you should:</p>
	                 <h1>%s</h1>
	                 <p><br>Warmly,</p>
	                 <p>The Causali team</p>
	                 <br><br>
	                 %s
	                 </body></html>
	                 """ % (name, condition.upper(), unsubscribe_string) % {'email': email, 'domain': domain},
	                 tag = "instruction")

	result = message.send()
	return result


def alert_zap(info=''):
	"""Generic email alert that something might be serious amiss.
	For example, user asked to unsubscribe but we could not find him in user database
	"""
	message = PMMail(api_key = os.environ.get('POSTMARK_API_TOKEN'),
	#,'4322111a-0d75-4777-8111-2d83f0664762'
                 subject = "Causali admin alert",
                 sender = "a@deberker.com",
                 to = ['petersmittenaar@gmail.com', 'a@deberker.com', 'zebkurthnelson@gmail.com'],
                 html_body = """
                 <p>Something went wrong that might require our attention, here is some info that might help:</p>
                 %s
                 """ % (info),
                 tag = "zap_alert")

	result = message.send()
	return result