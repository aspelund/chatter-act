rm_description = {
    'name': 'rm',
    'description': 'Remove a file or a directory.',
    'parameters': {
        'type': 'object',
        'properties': {
            'path': {
                'type': 'string',
                'description': 'The path to the file or directory. Cannot start with . or .. or / or ~. Project root is added to the path automatically.'
            }
        }
    }
}