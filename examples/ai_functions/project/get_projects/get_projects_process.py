from ...process import process
from .get_projects import get_projects


def arg_process(arguments):
    # There are no arguments to process for this function
    return ()


get_projects_process = process('get_projects', get_projects, arg_process)