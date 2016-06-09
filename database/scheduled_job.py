#!/usr/bin/python

"""This script is ran on a regular basis to do basic housekeeping.

"""
print("Running scheduled_job.py")

import database.db_utils as db_utils


db_utils.send_outstanding_instructions()
db_utils.send_outstanding_response_prompts()
db_utils.update_results()
print("Total number of completed trials in collection: %d" % (db_utils.trials_completed()))
