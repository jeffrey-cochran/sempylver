import argparse
import re

if __name__ == "__main__":
    #
    # Define an argument parser for commit-msg.py
    parser = argparse.ArgumentParser(description='Check commit message for tag flag.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('prev-msg', metavar='ppp', type=str, help='the previous message')
    #
    # Get args as dict
    args_dict = vars(parser.parse_args())
    msg = args_dict['prev-msg']
    #
    # Parse the msg
    flag_regex = re.compile(".*(-[tT]).*")
    flag_found = flag_regex.search(msg)
    if flag_found:
        with open("__version__", "r") as ff:
            version = ff.read().strip()
        return version
    else:
        return "NO"
