import os
import shutil
from utils.Config import Config


def cat(path):
    if path == None or path == '.':
        path = ''
    if path.startswith('./'):
        path = path[2:]

    if path.startswith('.') or path.startswith('..') or path.startswith('/') or path.startswith('~'):
        return {'role': 'user', 'name': 'cat', 'content': 'Invalid path.'}

    full_path = os.path.join(Config.project_path, path)
    if os.path.isfile(full_path):
        with open(full_path, 'r') as file:
            file_content = file.read()
        return {'role': 'user', 'name': 'cat', 'content': file_content}
    elif os.path.isdir(full_path):
        return {'role': 'user', 'name': 'cat', 'content': 'The path is a directory and cannot be read as a file.'}
    else:
        return {'role': 'user', 'name': 'cat', 'content': 'The path does not exist.'}