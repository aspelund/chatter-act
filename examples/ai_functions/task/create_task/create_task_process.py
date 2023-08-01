from ...process import process
from .create_task import create_task


def arg_process(arguments):
    return (arguments, )

create_task_process = process('create_task', create_task, arg_process)