update_epic_description = {
    'name': 'update_epic',
    'description': 'Update the content of a specific epic.',
    'parameters': {
        'type': 'object',
        'properties': {
            'epic_id': {
                'type': 'string',
                'description': 'The id of the epic.'
            },
            'description': {
                'type': 'string',
                'description': 'The new description for the epic.'
            },
            'name': {
                'type': 'string',
                'name': 'The new name of the epic.'
            }
        }
    }
}
