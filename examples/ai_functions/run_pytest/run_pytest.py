import os
import subprocess
from utils.Config import Config


def run_pytest(*args):

    current_dir = Config.project_path
    if (current_dir == ""):
        current_dir = os.getcwd()
    print(f'Running pytest in directory: {current_dir}')
    pytest_command = 'pytest'
    process = subprocess.Popen(
        pytest_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stdout = ""
    stderr = ""
    for line in process.stdout:
        stdout += line.decode()
    for line in process.stderr:
        stderr += line.decode()
    process.wait()  # wait for the process to finish
    if process.returncode == 0:
        pytest_output = stdout + stderr
    else:
        pytest_output = stdout + stderr  # Use stderr directly without checking stdout
    return_message = {'role': 'function',
                      'name': 'run_pytest', 'content': pytest_output}
    return return_message
