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
