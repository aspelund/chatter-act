from utils.Config import Config
import os


def write_to_file(path: str, content: str):
    try:
        file_path = os.path.join(Config().project_path, path)
        print(f"Writing to file: {file_path}")
        with open(file_path, 'w') as file:
            file.write(content)
        return {"role": "function", "name": "write_to_file", "content": "File written successfully."}
    except Exception as e:
        return {"role": "function", "name": "write_to_file", "content": f"Error writing file: {str(e)}"}
