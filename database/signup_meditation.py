# First point of contact after a user has signed up for the meditation experiment.

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.join(os.path.realpath(__file__))), os.pardir)))
import db_utils as db
from SignUpConfirmEmail import confirm_signup_meditation

name = sys.argv[1]
email = sys.argv[2]
print(name, email)

# store the user
user = db.store_user(name, email)
user_id = user.inserted_id

# initalise a new version of the experiment. Not ideal but works for now. (should just have one instance of the experiment which everyone signs up to, but I'm not sure how to hardcode that experiment in reliably.)
exp = db.init_experiment_meditation()
exp_id = exp.inserted_id

# initialise trials
trials = db.init_trials(user_id, exp_id)
trial_ids = [str(trials.inserted_id) for foo in trials]

# send an email to the user 
confirm_signup_meditation(name, email)