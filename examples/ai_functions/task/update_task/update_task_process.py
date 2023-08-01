from ...process import process
from .update_task import update_task


def arg_process(arguments):
    # Processing the arguments.
    task_id = arguments.get('task_id')
    name = arguments.get('name')
    description = arguments.get('description')
    completed = arguments.get('completed')
    return (task_id, name, description, completed)


update_task_process = process('update_task', update_task, arg_process)