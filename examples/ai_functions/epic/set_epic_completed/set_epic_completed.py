from mongo_models.epic import Epic


def set_epic_completed(epic_id):
    # sets a epic as completed
    try:
        epic = Epic.objects.get(id=epic_id)
        epic.completed = True
        epic.save()
    except Epic.DoesNotExist:
        return {'role': 'function', 'name': 'set_epic_completed', 'content': f'Epic with id {epic_id} not found.'}
    return {'role': 'function', 'name': 'set_epic_completed', 'content': f'Epic {epic.name} marked as completed.'}
