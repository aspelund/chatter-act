get_epics_description = {
    'name': 'get_epics',
    'description': 'Get a list of all epics that are not completed for a particular project.',
    'parameters': {
        'type': 'object',
        'properties': {
            'project_id': {'type': 'string', 'description': 'Project ID'}
        }
    }
}