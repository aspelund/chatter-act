from ...process import process
from .get_task import get_task


def arg_process(arguments):
    # Processing the arguments.
    task_id = arguments.get('task_id')
    return (task_id, )


get_task_process = process('get_task', get_task, arg_process)