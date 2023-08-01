from ...process import process
from .create_epic import create_epic

def arg_process(arguments):
    # Processing the arguments.
    data = arguments.get('data')
    data['project_id'] = arguments.get('project_id')
    return (data, )


create_epic_process = process('create_epic', create_epic, arg_process)