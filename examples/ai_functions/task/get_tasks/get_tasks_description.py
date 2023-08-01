get_tasks_description = {
    'name': 'get_tasks',
    'description': 'Get all tasks associated with a particular epic that are not yet completed.',
    'parameters': {
        'type': 'object',
        'properties': {
            'epic_id': {
                'type': 'string',
                'description': 'The id of the epic.'
            }
        }
    }
}