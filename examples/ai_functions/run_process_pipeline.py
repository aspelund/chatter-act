def run_process_pipeline(pipeline, message_dict, res):
    for process_func in pipeline:
        message_dict, res = process_func(message_dict, res)
        if res is not None:
            break
    return message_dict, res