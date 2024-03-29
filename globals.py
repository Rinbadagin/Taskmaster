from tkinter import *
from tkinter.ttk import *
from TaskHelper import *

"""Globals file for important variables used by all/many modules.
Tends to initialize but not populate them."""

WINDOW_NAME = "Taskmaster"
DEFAULT_WIDTH_X = "600"
DEFAULT_HEIGHT_Y = "400"
DEFAULT_DIMENSIONS = f'{DEFAULT_WIDTH_X}x{DEFAULT_HEIGHT_Y}'
ROOT = Tk()
ROOT.geometry(DEFAULT_DIMENSIONS)
TASK_HELPER = TaskHelperImpl()
ROOT_FRAME = "Not valid as a string constant."
INPUT_SANITIZATION = True
HASH_PREFIX_LENGTH = 8
SCHTASKS_MAXIMUM_NAME_LENGTH=236-HASH_PREFIX_LENGTH
NAME_MAXLENGTH = 15
TARGET_MAXLENGTH = 255
RUN_AS_ADMIN = True