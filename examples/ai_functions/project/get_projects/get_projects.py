from mongo_models.project import Project


def get_projects():
    # returns a list of all available projects with their id, name and path
    projects = Project.objects.all()
    return {'role': 'function', 'name': 'get_projects', 'content': str([{'id': project.id, 'name': project.name, 'path': project.path} for project in projects])}
