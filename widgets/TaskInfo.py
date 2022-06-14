from tkinter import *
from tkinter.ttk import *
from globals import *


class TaskInfo(Frame):
    def __init__(self):
        super(TaskInfo, self).__init__(master=ROOT, width="100", height="50")
        Label(master=self, text="Task Info").grid(row=0,column=0)
        Label(master=self, text=SELECTED_TASK).grid(row=1,column=0)
        Button(master=self, text="Save", command=lambda: TASK_HELPER.add_task_to_schedule(Task())).grid(row=2, column=0)
        Button(master=self, text="Delete", command=lambda: TASK_HELPER.delete_task(Task())).grid(row=2,column=1)