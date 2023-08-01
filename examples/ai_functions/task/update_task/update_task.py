from mongo_models.task import Task


def update_task(task_id, name, description, completed):
    # updates a task
    task = Task.objects.get(id=task_id)
    task.name = name
    task.description = description
    task.completed = completed
    task.save()
    return {'role': 'function', 'name': 'update_task', 'content': f'Task {task.name} updated successfully.'}