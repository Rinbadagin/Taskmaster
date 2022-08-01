from tkinter import *
from tkinter.ttk import *
from globals import *


class TaskInfo(Frame):
    def __init__(self, root_frame):
        from widgets.RootFrame import RootFrame
        super(TaskInfo, self).__init__(master=root_frame, width="100", height="50")
        Label(master=self, text="Task Info").grid(row=0,column=0)
        Label(master=self, text=TASK_HELPER.selected_task.task_name).grid(row=1,column=0)
        Button(master=self, text="Save", command=lambda: RootFrame.gi().button_save()).grid(row=2, column=0)
        Button(master=self, text="Delete", command=lambda: RootFrame.gi().button_delete_task(TASK_HELPER.loaded_tasks[-1])).grid(row=2, column=1)