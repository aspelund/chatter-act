from ...process import process
from .get_tasks import get_tasks


def arg_process(arguments):
    # Processing the arguments.
    epic_id = arguments.get('epic_id')
    return (epic_id, )


get_tasks_process = process('get_tasks', get_tasks, arg_process)