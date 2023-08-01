from mongo_models.task import Task


def get_tasks(epicId):
    # This function returns all tasks associated with a particular epic that are not yet completed.
    # It takes a parameter 'epicId' which is the ID of the epic for which tasks are to be retrieved.
    # It returns a list of task objects.
    tasks = Task.objects(epic=epicId, completed=False)
    return {'role': 'function', 'name': 'get_tasks', 'content': str([{'id': str(task.id), 'name': task.name} for task in tasks])}