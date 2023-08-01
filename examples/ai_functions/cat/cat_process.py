from ..process import process
from .cat import cat


def arg_process(arguments):
    return arguments.get('path', ''),

cat_process = process('cat', cat, arg_process)