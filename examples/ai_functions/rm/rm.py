import os
import shutil
from utils.Config import Config


def rm(path):
    if path == None or path == '.':
        path = ''
    if path.startswith('./'):
        path = path[2:]

    if path.startswith('.') or path.startswith('..') or path.startswith('/') or path.startswith('~'):
        return {"role": "user", "name": "rm", "content": "Invalid path."}

    full_path = os.path.join(Config.project_path, path)

    try:
        if os.path.isfile(full_path):
            os.remove(full_path)
        elif os.path.isdir(full_path):
            shutil.rmtree(full_path)
        else:
            return {"role": "user", "name": "rm", "content": "The path does not exist."}

        return {"role": "user", "name": "rm", "content": "Removed successfully."}
    except Exception as e:
        return {"role": "user", "name": "rm", "content": "Error removing file or directory: " + str(e)}