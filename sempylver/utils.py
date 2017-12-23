import yaml
from sempylver.constants import global_config


class config_parser(object):

    def __init__(
        self,
        config_file=global_config
    ):
        #
        # Parse config yml
        with open(config_file, 'r') as cf:
            config_opts_string = cf.read()
            config_opts = yaml.load(config_opts_string)
        #
        # print InvalidConfigSet
        print(config_opts)
