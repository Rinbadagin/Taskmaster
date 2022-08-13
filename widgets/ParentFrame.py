from tkinter import Frame
from globals import *

from widgets.TaskInfo import TaskInfo
from widgets.TaskList import TaskList


class ParentFrame(Frame):
    def __init__(self):
        from widgets.RootFrame import RootFrame
        super(ParentFrame, self).__init__(master=RootFrame.gi(), width=DEFAULT_WIDTH_X, height=DEFAULT_HEIGHT_Y)
        t_list = TaskList(self)
        t_info = TaskInfo(self)
