from tkinter import *
from tkinter.ttk import *
from TaskHelperTest import *

WINDOW_NAME = "Taskmaster"
SCHTASKS_FOLDER = f"\\${WINDOW_NAME}\\"
DEFAULT_DIMENSIONS = "400x250"
ROOT = Tk()
ROOT.geometry(DEFAULT_DIMENSIONS)
TASK_HELPER = TaskHelper()
LOADED_TASKS = TASK_HELPER.get_tasks()
SELECTED_TASK = "Unselected"
