import yaml
from sempylver.constants import global_config


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

    def set(
        self,
        config_name,
        value,
    ):
        #
        # Set config dict value
        self.config_opts[config_name] = value
        return self

    def write(self):
        with open(self.config_file, 'w') as cf:
            cf.write(yaml.dump(self.config_opts))
