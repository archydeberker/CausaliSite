import cgi
from database.db_utils import register_user_experiment 

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
register_user_experiment(
	form.getvalue('name'),
	form.getvalue('email'),
	form.getvalue('timezone'),
	form.getvalue('exp_name'),
	form.getvalue('condition1'),
	form.getvalue('nTrials1'),
	form.getvalue('condition2'),
	form.getvalue('nTrials2'),
	form.getvalue('dependent'),
	form.getvalue('ITI'),
	form.getvalue('instruction_time'),
	form.getvalue('response_time')
	)