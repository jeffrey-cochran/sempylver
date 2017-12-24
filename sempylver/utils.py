from shutil import copy2
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


def write_commit_msg_hook(git_hook_directory):
    #
    copy2(join(this_dir, 'commit-msg'), git_hook_directory)
    copy2(join(this_dir, 'commit_msg.py'), git_hook_directory)
    #
    return
