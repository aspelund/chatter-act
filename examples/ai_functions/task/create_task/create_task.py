from mongo_models.task import Task


def create_task(data: dict):
    new_task = Task(
        epic=data.get('epic'),
        name=data.get('name'),
        description=data.get('description'),
        order=data.get('order'),
        completed=False
    )
    new_task.save()
    return {'role': 'function', 'name': 'create_task', 'content': str({'id': str(new_task.id)}) if new_task else 'Could not create task'}