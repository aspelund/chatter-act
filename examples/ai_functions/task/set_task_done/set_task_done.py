from mongo_models.task import Task


def set_task_done(task_id):
    # sets a task as completed
    try:
        task = Task.objects.get(id=task_id)
        task.completed = True
        task.save()
    except Task.DoesNotExist:
        return {'role': 'function', 'name': 'set_task_done', 'content': f'Task with id {task_id} not found.'}
    return {'role': 'function', 'name': 'set_task_done', 'content': f'Task {task.name} marked as completed.'}
