from mongo_models.task import Task


def get_task(task_id):
    # returns a task
    task = Task.objects(id=task_id).first()
    return {'role': 'function', 'name': 'get_task', 'content': str({'id': str(task.id), 'name': task.name, 'description': task.description}) if task else 'No task found for this id'}
