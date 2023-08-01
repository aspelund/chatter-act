from mongo_models.epic import Epic


def get_epic(epic_id):
    # returns epic with the specified id
    epic = Epic.objects(id=epic_id).first()
    return {'role': 'function', 'name': 'get_epic', 'content': str({'id': str(epic.id), 'name': epic.name}) if epic else 'No epic found for this id'}
