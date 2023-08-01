create_task_description = {
    'name': 'create_task',
    'description': 'Create a new task.',
    'parameters': {
        'type': 'object',
        'properties': {
            'epic': {
                'type': 'string',
                'description': 'The id of the epic the task belongs to.'
            },
            'name': {
                'type': 'string',
                'description': 'The name of the task.'
            },
            'description': {
                'type': 'string',
                'description': 'The description of the task.'
            },
            'order': {
                'type': 'number',
                'description': 'The order of the task within the epic.'
            }
        }
    }
}