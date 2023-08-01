from ..process import process
from .mv import mv


def arg_process(arguments):
    return arguments.get('source', ''), arguments.get('destination', '')

mv_process = process('mv', mv, arg_process)