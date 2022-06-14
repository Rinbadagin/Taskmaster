from tkinter import *
from tkinter.ttk import *
from globals import *


class TaskList(Frame):
    def __init__(self):
        super(TaskList, self).__init__(master=ROOT, width="100", height="50")
        self.selected_task = StringVar(self, "Unselected")
        Label(master=self, text="Task List").grid(row=0, column=0)
        for i, z in zip(range(len(LOADED_TASKS)), LOADED_TASKS):
            Radiobutton(master=self, text=z.task_name, variable=self.selected_task, value=i, command=self.update_selected_task).grid(row=i+1, column=0)
        Button(master=self, text="Refresh", command = lambda: TASK_HELPER.get_tasks()).grid(row=len(LOADED_TASKS)+1,column=0)
        Button(master=self, text="New", command=lambda: TASK_HELPER.add_task_to_schedule(Task())).grid(row=len(LOADED_TASKS) + 1, column=1)
        Label(master=self, textvariable=self.selected_task).grid(row=0, column=1)

    def get_selected_task(self):
        return LOADED_TASKS[int(self.selected_task.get())]

    def update_selected_task(self):
        global SELECTED_TASK
        SELECTED_TASK=self.get_selected_task()
