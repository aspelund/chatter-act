from mongo_models.epic import Epic


def update_epic(epic_id, name, description):
    # updates an epic
    epic = Epic.objects.get(id=epic_id)
    epic.description = description
    epic.name = name
    epic.save()
    return {'role': 'function', 'name': 'update_epic', 'content': f'Epic {epic.name} updated successfully.'}
