import PySimpleGUI as sg
from TaskHelperTest import *

DEBUG = True
THEME = 'Default1'
WINDOW_NAME = "Taskmaster"
SCHTASKS_FOLDER = f"\\${WINDOW_NAME}\\"
DEFAULT_DIMENSIONS = (400,250)
WINDOW = False
TASK_HELPER = TaskHelper()
LOADED_TASKS = TASK_HELPER.get_tasks()
SELECTED_TASK = "Unselected"
LOADED = False
