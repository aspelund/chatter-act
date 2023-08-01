# This is the function to be executed
def hello_world(name):
    return {'role': 'function', 'name': 'hello_world', 'content': f"Hello, {name}!"}

# This is the description of the function
hello_world_description = {
    'name': 'hello_world',
    'description': 'A function to greet a user.',
    'parameters': {
        'type': 'object',
        'properties': {
            'name': {
                'type': 'string',
                'description': 'The name of the user.'
            }
        }
    }
}

# This is the process function
def hello_world_process(arguments):
    name = arguments.get('name')
    return (name, )
