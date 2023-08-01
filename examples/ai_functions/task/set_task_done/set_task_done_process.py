from ...process import process
from .set_task_done import set_task_done


def arg_process(arguments):
    # Processing the arguments.
    task_id = arguments.get('task_id')
    return (task_id, )


set_task_done_process = process('set_task_done', set_task_done, arg_process)
