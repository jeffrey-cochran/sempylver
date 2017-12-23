import argparse
from os.path import isfile
import re



def main():
    #
    # Define an argument parser for commit-msg.py
    parser = argparse.ArgumentParser(description='Check commit message for flags.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('msg-path', metavar='mmm', type=str, help='the path to the commit message')
    #
    # Get args as dict
    args_dict = vars(parser.parse_args())
    msg_path = args_dict['msg-path']
    print(msg_path)

if __name__ == "__main__":
    main()
