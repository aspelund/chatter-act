from ..process import process
from .rm import rm


def arg_process(arguments):
    return arguments.get('path', ''),

rm_process = process('rm', rm, arg_process)