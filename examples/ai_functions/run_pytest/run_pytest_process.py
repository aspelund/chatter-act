from ..process import process
from .run_pytest import run_pytest


def arg_process(arguments):
    return {},


run_pytest_process = process('run_pytest', run_pytest, arg_process)
