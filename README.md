# ChatterAct

ChatterAct is a Python package designed to streamline and simplify the integration of OpenAI's GPT-4 model into your applications. This package offers a minimalistic yet powerful solution that extends the functionality of OpenAI's function API. It stands as a vital tool for developers who wish to easily harness the capabilities of AI in creative and innovative ways.

ChatterAct provides the necessary tools to convert the AI's understanding of natural language into executable Python commands. It incorporates a built-in mechanism for handling function execution pipelines, making it easier to manage and extend the AI's ability to perform various tasks, such as managing files, running scripts, interacting with web APIs, and more.

Focusing on simplicity and flexibility, ChatterAct allows developers to introduce custom functionality, empowering them to define their own command-action pairs for the AI assistant, tailoring its functionality to suit specific needs.

## Key Functions

ChatterAct mainly exposes three important functions:

1. `process`: Used to define a process function for a specific task.
2. `prepare_pipeline`: Helps in preparing the AI pipeline with your function descriptions and process functions.
3. `handle_openai_response_and_execute_functions`: This is the most important function which handles the execution of your AI pipeline and processes responses from the OpenAI API.

## A Simple Example

Let's start by exposing a simple `hello_world` function to OpenAI:

```python
from chatteract import process, prepare_pipeline, handle_openai_response_and_execute_functions
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

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

# This is the process function, which processes arguments for the hello_world function
def hello_world_arg_process(arguments):
    name = arguments.get('name')
    return (name, )

# Use the process function from ChatterAct to create the hello_world_process function
hello_world_process = process('hello_world', hello_world, hello_world_arg_process)

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
    response = handle_openai_response_and_execute_functions(messages, pipeline, openai_settings)
    print(response[-1]['content'])

if __name__ == "__main__":
    main()

```

This script defines a simple function `hello_world` that takes a name and returns a greeting, along with a function description and a process function to process arguments.

The `get_pipeline()` function prepares the AI pipeline with the `hello_world` function, its description, and process function.

In the `main()` function, we simulate a message from the OpenAI GPT model that requests a call to the `hello_world` function with 'Alice' as the argument.

The `main()` function then calls `handle_openai_response_and_execute_functions()` with the message and the pipeline, which should process the function call and print the greeting.

## Function Structure

Each function in ChatterAct has three main components:

1. The description: Contains metadata about the function, including its name, description, and the parameters it accepts. This is used for generating documentation and providing context about the function to the user.

2. The process function: Handles the processing of arguments for the function and invokes the function with these arguments.

3. The function: This is where the actual work of the function happens.

Please refer to the simple example above to understand how these components work together.

## The Process Function

The `process` function is a key part of preparing your functions for integration with ChatterAct. It is used to wrap your function and create a process function that handles argument processing and function invocation. Here is an example of how to use it:

```python
from chatteract import process
from ai_functions.get_epic import get_epic

def arg_process(arguments):
    # Process the arguments.
    epic_id = arguments.get('epic_id')
    return (epic_id, )

get_epic_process = process('get_epic', get_epic, arg_process)
```

In this example, the `get_epic` function is designed to retrieve an epic (a collection of related tasks) based on its `epic_id`.

The `arg_process` function is a simple function that takes the arguments from the AI's function call, extracts the `epic_id`, and returns it as a tuple.

The `process` function is then used to wrap `get_epic` and `arg_process` together into a new function, `get_epic_process`.

The resulting `get_epic_process` function can be used in the pipeline to handle any function calls from the AI to `get_epic`.

Remember to include this process function when you set up your pipeline with `prepare_pipeline`. This pipeline should be passed as an argument when calling `handle_openai_response_and_execute_functions` to process the AI's function calls.
