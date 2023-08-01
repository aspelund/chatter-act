import os
import shutil
from utils.Config import Config


def mv(source, destination):
    if source is None or destination is None:
        return {'content': 'Source and destination paths are required.', 'status': 'error'}
    if source.startswith('.') or source.startswith('..') or source.startswith('/') or source.startswith('~') or destination.startswith('.') or destination.startswith('..') or destination.startswith('/') or destination.startswith('~'):
        return {'content': 'Invalid path.', 'status': 'error'}

    source_path = os.path.join(Config.project_path, source)
    destination_path = os.path.join(Config.project_path, destination)
    try:
        shutil.move(source_path, destination_path)
        return {'status': 'ok'}
    except Exception as e:
        return {'content': str(e), 'status': 'error'}
