from tkinter import *
from tkinter.ttk import *
from TaskHelper import *

"""Globals file for important variables used by all/many modules.
Tends to initialize but not populate them."""

WINDOW_NAME = "Taskmaster"
SCHTASKS_FOLDER = f"\\${WINDOW_NAME}\\"
DEFAULT_WIDTH_X = "600"
DEFAULT_HEIGHT_Y = "400"
DEFAULT_DIMENSIONS = f'{DEFAULT_WIDTH_X}x{DEFAULT_HEIGHT_Y}'
ROOT = Tk()
ROOT.geometry(DEFAULT_DIMENSIONS)
TASK_HELPER = TaskHelperImpl()
ROOT_FRAME = "Not valid as a string constant."
INPUT_SANITIZATION = True
NAME_MAXLENGTH = 15
TARGET_MAXLENGTH = 255