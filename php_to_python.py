#! /usr/bin/Python
"""This script takes arguments from PHP and runs the required script. 

The first argument is a string with the function to execute, the following strings will be passed on as they are

This helped script is necessary because otherwise everything becomes a mess of single and double quotes

This script does not do error/input checking, this is all handled in the respective functions that execute meaningful code.
"""

import sys
print('Number of input arguments: %d' % len(sys.argv))

def register_user_experiment(args):
	from database.db_utils import register_user_experiment
	# replace all NULL with None
	args = [None if arg == 'NULL' else arg for arg in args]

	success = register_user_experiment(args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7], args[8], args[9], args[10], args[11])
	return success


# if this script is being ran on its own (rather than, say, being imported)
if __name__ == "__main__":
	# run the requested function and pass an array with all arguments, but only if it exists
	if sys.argv[1]:
		eval(sys.argv[1] + '(sys.argv[2:])')

