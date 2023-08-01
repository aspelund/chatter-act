mv_description = {
    'name': 'mv',
    'description': 'Move or rename a file or folder.',
    'parameters': {
        'type': 'object',
        'properties': {
            'source': {
                'type': 'string',
                'description': 'The current path of the file or directory.'
            },
            'destination': {
                'type': 'string',
                'description': 'The new path for the file or directory.'
            }
        }
    }
}