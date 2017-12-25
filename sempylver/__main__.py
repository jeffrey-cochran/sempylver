import argparse
from sempylver.actions import actions


def main():
    #
    # Define an argument parser for commit-msg.py
    parser = argparse.ArgumentParser(description='Tool for simple semantic versioning.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    subparsers = parser.add_subparsers(
        help="""Possible actions:
- config""",
        dest='action'
    )
    #
    # Config parser
    parser_config = subparsers.add_parser('config', help='Set values in the global config file')
    parser_config.add_argument('--working-directory', metavar='d', type=str, help='the config option to set')
    #
    # Track parser
    parser_config = subparsers.add_parser('track', help='Track a Python git repository')
    parser_config.add_argument('project_directory', metavar='p', type=str, help='the repository to track')
    #
    # Get args
    args_dict = vars(parser.parse_args())
    #
    # Determine action
    action_str = args_dict.pop('action')
    if action_str is not None:
        #
        action = actions[action_str]
        #
        # Perform action
        action(**args_dict)


if __name__ == "__main__":
    main()
