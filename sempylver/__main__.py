import argparse
from sempylver.actions import actions


def main():
    #
    # Define an argument parser for commit-msg.py
    parser = argparse.ArgumentParser(description='Tool for simple semantic versioning.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    subparsers = parser.add_subparsers(
        help="""Possible actions:
- config""",
        dest='command'
    )
    #
    # Config parser
    parser_config = subparsers.add_parser('config', help='Set values in the global config file')
    parser_config.add_argument('-d', metavar='d', type=str, help='the config option to set')
    #
    # Get args
    args_dict = vars(parser.parse_args())
    #
    # Determine action
    action = args_dict.pop('action')
    #
    # Perform action
    action(**args_dict)


if __name__ == "__main__":
    main()
