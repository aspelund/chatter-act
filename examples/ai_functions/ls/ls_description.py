ls_description = {
    'name': 'ls',
    'description': 'List the files in a specified directory.',
    'parameters': {
        'type': 'object',
        'properties': {
            'path': {
                'type': 'string',
                'description': 'The path of the directory. Can be empty. Cannot start with . or .. or / or ~. Project root is added to the path automatically.'
            }
        }
    }
}