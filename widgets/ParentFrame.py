from tkinter import Frame
from globals import *

from widgets.TaskInfo import TaskInfo
from widgets.TaskList import TaskList


class ParentFrame(Frame):
    t_info = None
    t_list = None
    def __init__(self):
        from widgets.RootFrame import RootFrame
        super(ParentFrame, self).__init__(master=RootFrame.gi(), width=DEFAULT_WIDTH_X, height=DEFAULT_HEIGHT_Y)
        self.t_list = TaskList(self)
        self.t_info = TaskInfo(self)
