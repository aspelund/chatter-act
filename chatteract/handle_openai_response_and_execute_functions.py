import json
from send_api_request import send_api_request


def is_function_call(response):
    if response["role"] == "assistant" and "function_call" in response and response["function_call"] is not None:
        return True
    else:
        return False


def handle_openai_response_and_execute_functions(messages, pipeline, api_settings):
    new_messages = []
    max_retries = api_settings.get("max_retries", 3)
    while True:
        for i in range(max_retries):
            try:
                with (open("logs/messages.txt", "w")) as f:
                    f.write(json.dumps(messages, indent=2))
                o_response = send_api_request(
                    messages, api_settings, pipeline['descriptions'])
                o_response['content'] = "" if o_response['content'] is None else o_response['content']
                messages.append(o_response)
                new_messages.append(o_response)
                o_response = json.loads(json.dumps(o_response))
                if is_function_call(o_response):
                    try:
                        result = execute_function_call(
                            o_response, pipeline['processes'])
                        messages.append(result)
                        new_messages.append(result)
                    except FunctionExecutionError as fee:
                        raise fee  # Re-raise the exception to be handled by the caller
                else:
                    break
            except json.JSONDecodeError:
                if i < max_retries - 1:  # i is zero indexed
                    # Add a new message to inform the AI about the error
                    error_message = {
                        "name": "system",
                        "content": "Malformed JSON for arguments for function_call[arguments]. Double check for escaping all new lines etc and try again.",
                        "role": "user"
                    }
                    messages.append(error_message)
                    continue
                else:
                    raise OpenAIResponseError(
                        f"OpenAI response processing failed after {max_retries} attempts.")
        if not is_function_call(o_response):
            break
    return new_messages


def execute_function_call(response, process_pipeline):
    try:
        function_call = response["function_call"]
        function_call["arguments"] = json.loads(function_call["arguments"])
        function_name = function_call["name"]
        function_call, result = run_process_pipeline(
            process_pipeline, function_call, None)
        if result is None:
            raise FunctionResultNoneError(
                function_name, f"Function {function_name} did not complete successfully. Result is None.")
        result['content'] = "" if result['content'] is None else result['content']
        return result
    except json.JSONDecodeError as e:
        # Re-raise the exception to be handled in `process_openai_response`
        raise e
    except Exception as e:
        raise FunctionExecutionError(function_name, e)


def prepare_pipeline(ai_functions):
    pipeline = {
        "descriptions": [],
        "processes": [],
    }
    for ai_function_process, ai_function_description in ai_functions:
        pipeline["descriptions"].append(ai_function_description)
        pipeline["processes"].append(ai_function_process)

    return pipeline


def run_process_pipeline(pipeline, message_dict, res):
    for process_func in pipeline:
        message_dict, res = process_func(message_dict, res)
        if res is not None:
            break
    return message_dict, res


class FunctionExecutionError(Exception):
    """
    Custom exception for function execution errors.
    """

    def __init__(self, function_name, original_exception):
        self.function_name = function_name
        self.original_exception = original_exception
        super().__init__(
            self, f"An error occurred while executing function {function_name}.")


class FunctionResultNoneError(Exception):
    """
    Custom exception for when the result of a function execution is None.
    """

    def __init__(self, function_name):
        super().__init__(self,
                         f"Function call did not complete successfully. Result is None for function {function_name}.")


class OpenAIResponseError(Exception):
    """Custom exception to indicate an error in the OpenAI response."""
    pass