from ...process import process
from .update_epic import update_epic


def arg_process(arguments):
    # Processing the arguments.
    epic_id = arguments.get('epic_id')
    name = arguments.get('name')
    description = arguments.get('description')
    return (epic_id, name, description)


update_epic_process = process('update_epic', update_epic, arg_process)
