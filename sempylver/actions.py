from sempylver.utils import config_parser


def set_config(config_name, value):
    z = config_parser()
    z.set(config_name, value).write()

actions = {
    'config': set_config
}
