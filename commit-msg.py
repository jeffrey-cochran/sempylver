import argparse
from os.path import isfile
import re

if __name__ == "__main__":
	#
    # Define an argument parser for commit-msg.py
	parser = argparse.ArgumentParser(description='Check commit message for flags.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument('msg-path', metavar='mmm', type=str, help='the path to the commit message')
	#
	# Get args as dict
	args_dict = vars(parser.parse_args())
	msg_path = args_dict['msg-path']
	#
	# Grab message
	with open(msg_path, 'r') as f:
		msg = f.read().strip()
	#
	# Parse the msg
	flag_regex = re.compile(".*(-[mM]).*")
	found = flag_regex.search(msg)
	flag = None
	if found:
		flag = re.sub('-', '', found.group(1))
	if isfile("__version__"):
		#
		# Write message
		with open("__version__", "r") as f:
			version = f.read().strip()
			symver = [int(j) for j in version.split('.')]
	else:
		symver = [0, 0, 0]
	#
	# Condition on flag
	if flag == 'M':
		symver[0] += 1
	elif flag == 'm':
		symver[1] += 1
	else:
		symver[2] += 1
	#
	# Concat
	symver = [str(i) for i in symver]
	version = '.'.join(symver)
	#
	with open("__version__","w") as f:
		f.write(version)