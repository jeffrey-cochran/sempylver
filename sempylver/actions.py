import subprocess
from os.path import isdir, join
from sempylver.utils import config_parser, write_commit_msg_hook, write_setup


def set_config(**kwargs):
    z = config_parser()
    for key, value in kwargs.items():
        if value is not None:
            z.set(key, value)
    z.write()


def track_project(project_directory=None, s=False):
    #
    z = config_parser()
    try:
        working_directory = z.config_opts['working_directory']
    except KeyError:
        working_directory = None
    #
    is_relative_path = False
    if working_directory is not None:
        git_hook_directory = join(join(project_directory, '.git'), 'hooks')
        is_relative_path = isdir(join(working_directory, git_hook_directory))
    #
    if is_relative_path:
        git_hook_directory = join(working_directory, git_hook_directory)
    elif not isdir(git_hook_directory):
        raise Exception('The target directory, %s, does not appear to be a git repository.' % project_directory)
    #
    write_commit_msg_hook(git_hook_directory)
    #
    # Create a setup file
    if s:
        write_setup(project_directory)
    #
    return


actions = {
    'config': set_config,
    'track': track_project,
}
