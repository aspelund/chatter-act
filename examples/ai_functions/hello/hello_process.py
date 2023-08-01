from ..process import process
from .hello import hello


def arg_process(arguments):
    return {}


hello_process = process('hello', hello, arg_process)
