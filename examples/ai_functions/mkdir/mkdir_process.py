from ..process import process
from .mkdir import mkdir


def arg_process(arguments):
    return arguments.get('path', ''),

mkdir_process = process('mkdir', mkdir, arg_process)