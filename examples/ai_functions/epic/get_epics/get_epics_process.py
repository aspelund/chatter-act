from ...process import process
from .get_epics import get_epics


def arg_process(arguments):
    # processing arguments
    return (arguments['project_id'],)


get_epics_process = process('get_epics', get_epics, arg_process)