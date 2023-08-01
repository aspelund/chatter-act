import os
from ai_functions.process import process
from ai_functions.write_to_file.write_to_file import write_to_file
from utils.Config import Config


def arg_process(arguments):
    path = arguments.get('path', '')
    content = arguments.get('content', '')

    if path == None or path == ".":
        path = ""
    if path.startswith("./"):
        path = path[2:]

    if path.startswith(".") or path.startswith("..") or path.startswith("/") or path.startswith("~"):
        raise ValueError("Invalid path.")

    full_path = os.path.join(Config.project_path, path)
    return full_path, content


write_to_file_process = process('write_to_file', write_to_file, arg_process)
