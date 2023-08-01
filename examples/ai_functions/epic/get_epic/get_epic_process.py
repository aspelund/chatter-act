from ...process import process
from .get_epic import get_epic


def arg_process(arguments):
    # Processing the arguments.
    epic_id = arguments.get('epic_id')
    return (epic_id, )


get_epic_process = process('get_epic', get_epic, arg_process)