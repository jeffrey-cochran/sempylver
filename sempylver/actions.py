from sempylver.utils import config_parser


def set_config(**kwargs):
    z = config_parser()
    for key, value in kwargs.items():
        z.set(key, value)
    z.write()

actions = {
    'config': set_config
}
