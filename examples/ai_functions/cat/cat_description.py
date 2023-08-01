cat_description = {
    'name': 'cat',
    'description': 'Read the contents of a specified file.',
    'parameters': {
        'type': 'object',
        'properties': {
            'path': {
                'type': 'string',
                'description': 'The path to the file. Cannot start with . or .. or / or ~. Project root is added to the path automatically.'
            }
        }
    }
}