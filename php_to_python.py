"""This script takes arguments from PHP and runs the required script. 

The first argument is a string with the function to execute, the following strings will be passed on as they are

This helped script is necessary because otherwise everything becomes a mess of single and double quotes

This script does not do error/input checking, this is all handled in the respective functions that execute meaningful code.
"""

import sys

def register_user_experiment(args):
	from db_utils import register_user_experiment
	# run the function with each argument passed as-is
	eval('register_user_experiment(' + ', '.join(args) + ')'




# if this script is being ran on its own (rather than, say, being imported)
if __name__ == "__main__":
	# run the requested function and pass an array with all arguments, but only if it exists
	if sys.argv[0]:
		eval(sys.argv[0] + '(sys.argv[1:])')

