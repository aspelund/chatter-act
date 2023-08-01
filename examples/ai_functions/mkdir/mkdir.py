import os
import shutil
from utils.Config import Config

def mkdir(path):
    if path == None or path == '.':
        path = ''
    if path.startswith('./'):
        path = path[2:]

    if path.startswith('.') or path.startswith('..') or path.startswith('/') or path.startswith('~'):
        return {'role': 'user', 'name': 'mkdir', 'content': 'Invalid path.'}

    full_path = os.path.join(Config.project_path, path)
    try:
        os.makedirs(full_path, exist_ok=True)
        return {'role': 'user', 'name': 'mkdir', 'content': 'Directory created successfully.'}
    except Exception as e:
        return {'role': 'user', 'name': 'mkdir', 'content': 'Error creating directory: ' + str(e)}