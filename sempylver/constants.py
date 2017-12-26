from os.path import dirname, join, abspath
from re import compile

this_dir = dirname(abspath(__file__))
global_config = join(this_dir, "global_config.yml")

setup_file_replacement_string = """with open('__version__', 'rb') as f:
    version = f.read().strip()


setup(
"""

version_pattern = 'version\s*=\s*\w+,'
version_regex = compile(version_pattern)
