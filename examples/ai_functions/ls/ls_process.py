from ..process import process
from .ls import ls


def arg_process(arguments):
    return arguments.get('path', ''),

ls_process = process('ls', ls, arg_process)