from mongo_models.epic import Epic


def get_epics(project_id):
    # returns all epics that are not completed
    epics = Epic.objects(completed=False, project=project_id)
    return {'role': 'function', 'name': 'get_epics', 'content': str([{'id': str(epic.id), 'name': epic.name} for epic in epics])}