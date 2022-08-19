from tkinter import *
from tkinter.ttk import *
from globals import *


class TaskList(Frame):
    button_array = []

    def __init__(self, root_frame):
        from widgets.RootFrame import RootFrame
        super(TaskList, self).__init__(master=root_frame)
        Label(master=self, text="Task List").grid(row=0, column=0, sticky=W)
        Button(master=self, text="Up", command=self.up, width=17).grid(row=1, column=0, sticky=W)
        Button(master=self, text="Down", command=self.down, width=17).grid(row=1, column=1, sticky=E)
        self.button_array = []
        for i, z in zip(range(len(TASK_HELPER.loaded_tasks[RootFrame.gi().scroll_index::])), TASK_HELPER.loaded_tasks[RootFrame.gi().scroll_index::]):
            self.button_array.append(
                Radiobutton(master=self, text=self.convert_string(z.name), variable=RootFrame.gi().selected_task_stringvar, value=i+RootFrame.gi().scroll_index,
                            command=self.update_selected_task,width=17))
            self.button_array[i].grid(row=i + 2, column=0, sticky=W,padx=30, columnspan=2)
        self.place(anchor="nw")
        self.buttons = TaskListButtons(root_frame)

    def get_selected_task(self):
        from widgets.RootFrame import RootFrame
        RootFrame.gi().selected_task_stringvar.set(RootFrame.gi().selected_task_stringvar.get())
        return TASK_HELPER.loaded_tasks[int(RootFrame.gi().selected_task_stringvar.get())]

    def update_selected_task(self):
        from widgets.RootFrame import RootFrame
        TASK_HELPER.selected_task_stringvar = self.get_selected_task()
        RootFrame.gi().update_gui()

    def up(self):
        from widgets.RootFrame import RootFrame
        if RootFrame.gi().scroll_index > 0:
            RootFrame.gi().scroll_index -= 1
            RootFrame.gi().update_gui()

    def down(self):
        from widgets.RootFrame import RootFrame
        if RootFrame.gi().scroll_index < len(TASK_HELPER.loaded_tasks)-1:
            RootFrame.gi().scroll_index += 1
            RootFrame.gi().update_gui()

    def convert_string(self, input_string):
        #Converts a string into a shortened version for display in a thin list
        return input_string if len(input_string)<NAME_MAXLENGTH else input_string[0:NAME_MAXLENGTH-3]+"..."

class TaskListButtons(Frame):
    def __init__(self, root_frame):
        from widgets.RootFrame import RootFrame
        super(TaskListButtons, self).__init__(master=root_frame, width="100", height="50")
        Button(master=self, text="Reload", command=lambda: RootFrame.gi().get_tasks(), width=17).grid(
            row=len(TASK_HELPER.loaded_tasks) + 1, column=0)
        Button(master=self, text="New", command=lambda: RootFrame.gi().button_new_task(Task()), width=17).grid(
            row=len(TASK_HELPER.loaded_tasks) + 1, column=1)
        self.place(anchor="sw", relx=0, rely=1)
