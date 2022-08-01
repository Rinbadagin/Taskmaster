from tkinter import *
from tkinter.ttk import *
from TaskHelperTest import *

WINDOW_NAME = "Taskmaster"
SCHTASKS_FOLDER = f"\\${WINDOW_NAME}\\"
DEFAULT_DIMENSIONS = "400x250"
ROOT = Tk()
ROOT.geometry(DEFAULT_DIMENSIONS)
TASK_HELPER = TaskHelper()
ROOT_FRAME = "Not valid as a string constant."