# ChatterAct

ChatterAct is a Python package that ...

## A simple example

Let's start by exposing a simple hello_world function to openai:

```python
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

```

All functions that we expose requires three things - the function that executes whatever we are exposing to the AI, a description of the function and a process function in order for us to pick it up with the chatter-act package.

A corresponding main function could look like this:

```python
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

from chatter_act import prepare_pipeline, process_openai_response
from ai_functions.hello_world import hello_world_description, hello_world_process

# Prepare the AI pipeline
def get_pipeline():
    ai_functions = [
        (hello_world_process, hello_world_description),
    ]
    pipeline = prepare_pipeline(ai_functions)
    return pipeline

# Start conversation with a system message
messages = [
    {
        'role': 'system',
        'content': 'This is a system message to start the conversation.'
    },
    {
        'role': 'user',
        'content': 'Can you greet Alice for me?'
    }
]

# OpenAI settings
openai_settings = {
    "model": "gpt-4-0613",
    "url": "https://api.openai.com/v1/chat/completions",
    "max_retries": 3,
    "retry_delay": 3,
    "max_tokens": 8000,
    "headers": {
        "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}",
    }
}

def main():
    pipeline = get_pipeline()
    response = process_openai_response(messages, pipeline, openai_settings)
    print(response[-1]['content'])

if __name__ == "__main__":
    main()

```

This script defines a simple function hello_world that takes a name and returns a greeting, along with a function description and a process function to process arguments.

The get_pipeline() function prepares the AI pipeline with the hello_world function and its description and process function.

In the main() function, we simulate a message from the OpenAI GPT model that requests a call to the hello_world function with 'Alice' as the argument.

The main() function then calls process_openai_response() with the message and the pipeline, which should process the function call and print the greeting.

## Function Structure

Each function in ChatterAct has three main components:

1. The description file: Contains metadata about the function, including its name, description, and the parameters it accepts. This is used for generating documentation and providing context about the function to the user.

2. The process file: Handles the processing of arguments for the function and invokes the function with these arguments.

3. The function file: This is where the actual work of the function happens.

### Example

Let's take a look at the `get_tasks` function to see how these parts work together:

1. Description file (`get_tasks_description.py`):

```python
get_tasks_description = {
    'name': 'get_tasks',
    'description': 'Get all tasks associated with a particular epic that are not yet completed.',
    'parameters': {
        'type': 'object',
        'properties': {
            'epic_id': {
                'type': 'string',
                'description': 'The id of the epic.'
            }
        }
    }
}
```

Process file (get_tasks_process.py):

```python

from ...process import process
from .get_tasks import get_tasks

def arg_process(arguments):
    epic_id = arguments.get('epic_id')
    return (epic_id, )

get_tasks_process = process('get_tasks', get_tasks, arg_process)
```

Function file (get_tasks.py):

```python

from mongo_models.task import Task

def get_tasks(epicId):
    tasks = Task.objects(epic=epicId, completed=False)
    return {'role': 'function', 'name': 'get_tasks', 'content': str([{'id': str(task.id), 'name': task.name} for task in tasks])}
```

In this example, the description file provides metadata about the get_tasks function. The process file uses this metadata to handle the processing of arguments and to call the function. The function file contains the logic that retrieves the tasks from the database.
