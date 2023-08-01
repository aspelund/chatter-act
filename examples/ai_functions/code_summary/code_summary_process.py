from ..process import process
from .code_summary import code_summary

def arg_process(arguments):
    return arguments.get('path', ''),

code_summary_process = process('code_summary', code_summary, arg_process)