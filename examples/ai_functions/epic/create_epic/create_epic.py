from validation.schemas.create_epic_schema import CreateEpicSchema
from mongo_models.epic import Epic
from mongo_models.project import Project


def create_epic(data: dict):
    try:
        # Validate the data using the Pydantic Model
        epic_data = CreateEpicSchema(**data)
    except ValueError as e:
        # Return error message if validation fails
        return {'role': 'function', "name": "create_epic", 'content': f'Invalid input: {str(e)}'}

    # Fetch project and add it to the epic
    project = Project.objects.get(id=data['project_id'])

    new_epic = Epic(
        name=epic_data.name,
        description=epic_data.description,
        slug=epic_data.slug,
        path=epic_data.path,
        project=project,
        completed=False
    )
    try:
        new_epic.save()
        # Return the newly created epic object, converted to dictionary
        return {'role': 'function', 'name': 'create_epic', 'content': str(new_epic.to_mongo().to_dict())}
    except Exception as e:
        return {'role': 'function', 'name': 'create_epic', 'content': f'Error creating epic: {str(e)}'}