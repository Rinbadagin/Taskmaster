from tkinter import *
from tkinter.ttk import *
from globals import *


class TaskList(Frame):
    button_array = []

    def __init__(self, root_frame):
        from widgets.RootFrame import RootFrame
        super(TaskList, self).__init__(master=root_frame, width="100", height="50")
        Label(master=self, text="Task List").grid(row=0, column=0)
        self.button_array = []
        for i, z in zip(range(len(TASK_HELPER.loaded_tasks)), TASK_HELPER.loaded_tasks):
            self.button_array.append(
                Radiobutton(master=self, text=z.name, variable=RootFrame.gi().selected_task, value=i,
                            command=self.update_selected_task))
            self.button_array[i].grid(row=i + 1, column=0)
        Label(master=self, textvariable=RootFrame.gi().selected_task).grid(row=0, column=1)
        self.place(anchor="nw")
        self.buttons = TaskListButtons(root_frame)

    def get_selected_task(self):
        from widgets.RootFrame import RootFrame
        RootFrame.gi().selected_task.set(RootFrame.gi().selected_task.get())
        return TASK_HELPER.loaded_tasks[int(RootFrame.gi().selected_task.get())]

    def update_selected_task(self):
        from widgets.RootFrame import RootFrame
        TASK_HELPER.selected_task = self.get_selected_task()
        RootFrame.gi().update_gui()


class TaskListButtons(Frame):
    def __init__(self, root_frame):
        from widgets.RootFrame import RootFrame
        super(TaskListButtons, self).__init__(master=root_frame, width="100", height="50")
        Button(master=self, text="Refresh", command=lambda: RootFrame.gi().get_tasks()).grid(
            row=len(TASK_HELPER.loaded_tasks) + 1, column=0)
        Button(master=self, text="New", command=lambda: RootFrame.gi().button_new_task(Task())).grid(
            row=len(TASK_HELPER.loaded_tasks) + 1, column=1)
        self.place(anchor="sw", relx=0, rely=1)
