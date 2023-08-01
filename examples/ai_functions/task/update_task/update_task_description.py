update_task_description = {
    'name': 'update_task',
    'description': 'Update the details of a specific task.',
    'parameters': {
        'type': 'object',
        'properties': {
            'task_id': {
                'type': 'string',
                'description': 'The id of the task.'
            },
            'name': {
                'type': 'string',
                'description': 'The new name of the task.'
            },
            'description': {
                'type': 'string',
                'description': 'The new description of the task.'
            },
            'completed': {
                'type': 'boolean',
                'description': 'Completion status of the task.'
            }
        }
    }
}