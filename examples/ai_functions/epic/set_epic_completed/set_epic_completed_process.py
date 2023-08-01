from ...process import process
from .set_epic_completed import set_epic_completed


def arg_process(arguments):
    # Processing the arguments.
    epic_id = arguments.get('epic_id')
    return (epic_id, )


set_epic_completed_process = process('set_epic_completed', set_epic_completed, arg_process)