# ai_functions/ls/ls.py
import os
from utils.Config import Config


def ls(path):
    if path == None or path == '.':
        path = ''
    if path.startswith('./'):
        path = path[2:]
    if path.startswith('.') or path.startswith('..') or path.startswith('/') or path.startswith('~'):
        return {"role": "function", "name": "ls", "content": "Invalid path."}

    full_path = os.path.join(Config.project_path, path)
    if os.path.isfile(full_path):
        return {"role": "function", "name": "ls", "content": ', '.join([os.path.basename(full_path)])}
    elif os.path.isdir(full_path):
        return {"role": "function", "name": "ls", "content": ', '.join(os.listdir(full_path))}
    else:
        return {"role": "function", "name": "ls", "content": "The path does not exist."}
