# ChatterAct

ChatterAct is a Python package developed to streamline the integration of OpenAI's GPT-4 model into your applications. Its primary goal is to provide a simplified, yet flexible mechanism for exposing numerous functions to the AI model with minimal effort. ChatterAct handles the execution and piping, enabling you to start simple with one or two AI functions and expand as the complexity of your project grows.

## Key Functions

ChatterAct primarily exposes two significant functions:

1. `get_ai_function`: This function helps create an AI function object with a specific function, its argument handler, and a function description.

2. `handle_openai_response_and_execute_functions`: This function processes responses from the OpenAI API and manages the execution of the appropriate AI functions.

## A Basic Example

Let's consider a simple example using ChatterAct to expose a `hello_world` function to OpenAI:

```python
from chatteract import handle_openai_response_and_execute_functions, get_ai_function
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# This is the function to be executed
def hello_world(name):
    return f"Hello, {name}!"

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

# This is the function argument handler
def hello_world_arg_process(arguments):
    name = arguments.get('name')
    return (name,)

# Create the AI function
hello_world_ai_function = get_ai_function('hello_world', hello_world, hello_world_arg_process, hello_world_description)

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

# Start the conversation with a system message
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

def main():
    response = handle_openai_response_and_execute_functions(messages, [hello_world_ai_function], openai_settings)
    print(response[-1]['content'])

if __name__ == "__main__":
    main()
```

In this example, `hello_world` is a function that greets a user. It is combined with its description and argument handler using `get_ai_function` to create an AI function. This AI function is then used in `handle_openai_response_and_execute_functions` to process and handle OpenAI's responses.

Adding another function follows a similar process. Just create another AI function and include it in the list of functions passed to `handle_openai_response_and_execute_functions`. This makes it easy to expose multiple functions to the AI.

## AI Function Structure

Each AI function in ChatterAct has three main components:

1. The function: The actual Python function that gets executed.

2. The function argument handler: Processes the arguments that the function requires.

3. The function description: Contains metadata about the function, including its name, description, and the parameters it accepts.

## The get_ai_function

The `get_ai_function` is used to generate an AI function object. This function takes the following parameters:

- `unique_identifier`: A unique identifier for the function.
- `function`: The actual function that should be executed.
- `function_arg_handler`: A handler function that processes the arguments for the `function`.
- `description`: The description of the function.

Here's an example of how to use it:

```python
from chatteract import get_ai_function

# This is the function to be executed
def hello_world(name):
    return f"Hello, {name}!"

# This is the function argument handler
def hello_world_arg_process(arguments):
    name = arguments.get('name')
    return (name,)

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

# Create the AI function
hello_world_ai_function = get_ai_function('hello_world', hello_world, hello_world_arg_process, hello_world_description)
```

This code block creates an AI function `hello_world`, which can be used in `handle_openai_response_and_execute_functions` to process and handle OpenAI's responses.
