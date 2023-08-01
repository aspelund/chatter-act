mkdir_description = {
    'name': 'mkdir',
    'description': 'Create a directory at the specified path.',
    'parameters': {
        'type': 'object',
        'properties': {
            'path': {
                'type': 'string',
                'description': 'The path for the new directory. Cannot start with . or .. or / or ~. Project root is added to the path automatically.'
            }
        }
    }
}