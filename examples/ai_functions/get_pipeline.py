from function_handler import prepare_pipeline
from ai_functions.code_summary.code_summary_description import code_summary_description
from ai_functions.run_pytest.run_pytest_description import run_pytest_description
from ai_functions.ls.ls_description import ls_description
from ai_functions.mkdir.mkdir_description import mkdir_description
from ai_functions.write_to_file.write_to_file_description import write_to_file_description
from ai_functions.cat.cat_description import cat_description
from ai_functions.mv.mv_description import mv_description
from ai_functions.rm.rm_description import rm_description
from ai_functions.epic.get_epics.get_epics_description import get_epics_description
from ai_functions.epic.get_epic.get_epic_description import get_epic_description
from ai_functions.epic.set_epic_completed.set_epic_completed_description import set_epic_completed_description
from ai_functions.epic.update_epic.update_epic_description import update_epic_description
from ai_functions.epic.create_epic.create_epic_description import create_epic_description
from ai_functions.task.get_tasks.get_tasks_description import get_tasks_description
from ai_functions.task.get_task.get_task_description import get_task_description
from ai_functions.task.set_task_done.set_task_done_description import set_task_done_description
from ai_functions.task.update_task.update_task_description import update_task_description
from ai_functions.task.create_task.create_task_description import create_task_description
from ai_functions.project.get_projects.get_projects_description import get_projects_description
from ai_functions.code_summary.code_summary_process import code_summary_process
from ai_functions.run_pytest.run_pytest_process import run_pytest_process
from ai_functions.ls.ls_process import ls_process
from ai_functions.cat.cat_process import cat_process
from ai_functions.write_to_file.write_to_file_process import write_to_file_process
from ai_functions.mkdir.mkdir_process import mkdir_process
from ai_functions.mv.mv_process import mv_process
from ai_functions.rm.rm_process import rm_process
from ai_functions.epic.get_epics.get_epics_process import get_epics_process
from ai_functions.epic.get_epic.get_epic_process import get_epic_process
from ai_functions.epic.set_epic_completed.set_epic_completed_process import set_epic_completed_process
from ai_functions.epic.update_epic.update_epic_process import update_epic_process
from ai_functions.epic.create_epic.create_epic_process import create_epic_process
from ai_functions.task.get_tasks.get_tasks_process import get_tasks_process
from ai_functions.task.get_task.get_task_process import get_task_process
from ai_functions.task.set_task_done.set_task_done_process import set_task_done_process
from ai_functions.task.update_task.update_task_process import update_task_process
from ai_functions.task.create_task.create_task_process import create_task_process
from ai_functions.project.get_projects.get_projects_process import get_projects_process


def get_pipeline():
    ai_functions = [
        (code_summary_process, code_summary_description),
        (run_pytest_process, run_pytest_description),
        (ls_process, ls_description),
        (cat_process, cat_description),
        (write_to_file_process, write_to_file_description),
        (mkdir_process, mkdir_description),
        (mv_process, mv_description),
        (rm_process, rm_description),
        (get_epics_process, get_epics_description),
        (get_epic_process, get_epic_description),
        (set_epic_completed_process, set_epic_completed_description),
        (update_epic_process, update_epic_description),
        (create_epic_process, create_epic_description),
        (get_tasks_process, get_tasks_description),
        (get_task_process, get_task_description),
        (set_task_done_process, set_task_done_description),
        (update_task_process, update_task_description),
        (create_task_process, create_task_description),
        (get_projects_process, get_projects_description)
    ]

    pipeline = prepare_pipeline(ai_functions)
    return pipeline
