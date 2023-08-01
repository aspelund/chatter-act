set_task_done_description = {
    'name': 'set_task_done',
    'description': 'Mark a task as completed.',
    'parameters': {
        'type': 'object',
        'properties': {
            'task_id': {
                'type': 'string',
                'description': 'The id of the task.'
            }
        }
    }
}
