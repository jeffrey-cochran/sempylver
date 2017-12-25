from shutil import copyfileobj
from os.path import join
import yaml
from sempylver.constants import global_config, this_dir


class config_parser(object):

    def __init__(
        self,
        config_file=global_config
    ):
        #
        # Set destination for config file
        self.config_file = config_file
        #
        # Parse config yml
        with open(config_file, 'r') as cf:
            config_opts_string = cf.read()
            self.config_opts = yaml.load(config_opts_string)
        #
        return

    def set(
        self,
        config_name,
        value,
    ):
        #
        # Set config dict value
        self.config_opts[config_name] = value
        #
        return self

    def write(self):
        with open(self.config_file, 'w') as cf:
            yaml.dump(self.config_opts, cf, default_flow_style=False)
        #
        return


def copy_with_newlines(orig_dir, tgt_dir, file_name, newline='\r\n'):
    with open(join(orig_dir, file_name), 'r') as orig_file:
        with open(join(tgt_dir, file_name), 'w', newline=newline) as tgt_file:
            copyfileobj(orig_file, tgt_file)


def write_commit_msg_hook(git_hook_directory):
    #
    copy_with_newlines(this_dir, git_hook_directory, 'commit-msg', newline='\n')
    copy_with_newlines(this_dir, git_hook_directory, 'commit_msg.py')
    #
    return
