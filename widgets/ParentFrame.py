from tkinter import Frame

from widgets.TaskInfo import TaskInfo
from widgets.TaskList import TaskList


class ParentFrame(Frame):
    def __init__(self):
        from widgets.RootFrame import RootFrame
        super(ParentFrame, self).__init__(master=RootFrame.gi(), width="400", height="400")
        t_list = TaskList(self)
        t_list.grid(row=0, column=0)
        t_info = TaskInfo(self)
        t_info.grid(row=0, column=1)
