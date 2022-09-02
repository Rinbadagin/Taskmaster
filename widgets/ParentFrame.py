from tkinter import Frame
from globals import *

from widgets.TaskInfo import TaskInfo
from widgets.TaskList import TaskList


class ParentFrame(Frame):
    """Child frame of rootframe, is parent of all other window widgets.
    Should not hold any stateful information as is often destroyed and recreated
    To mimic a dynamic GUI"""
    t_info = None
    t_list = None
    def __init__(self):
        from widgets.RootFrame import RootFrame
        super(ParentFrame, self).__init__(master=RootFrame.gi(), width=DEFAULT_WIDTH_X, height=DEFAULT_HEIGHT_Y)
        self.t_list = TaskList(self)
        self.t_info = TaskInfo(self)
