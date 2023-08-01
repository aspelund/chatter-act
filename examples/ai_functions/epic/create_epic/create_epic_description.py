create_epic_description = {
    'name': 'create_epic',
    'description': 'Create a new epic',
    'parameters': {
        'type': 'object',
        'properties': {
            'name': {
                'type': 'string',
                'description': 'The name of the epic.'
            },
            'description': {
                'type': 'string',
                'description': 'The description of the epic.'
            },
            'slug': {
                'type': 'string',
                'description': 'The slug of the epic.'
            },
            'path': {
                'type': 'string',
                'description': 'The path of the epic. Cannot start with . or .. or / or ~. Project root is added to the path automatically.'
            },
            'project_id': {
                'type': 'string',
                'description': 'The id of the project.'
            }
        }
    }
}