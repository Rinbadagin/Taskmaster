from tkinter import *
from tkinter.ttk import *
from globals import *


class TaskInfo(Frame):
    def __init__(self, root_frame):
        from widgets.RootFrame import RootFrame
        super(TaskInfo, self).__init__(master=root_frame, width="100", height="50")
        self.initialize_form()
        self.place(anchor="ne",relx=0.95)
        self.buttons = TaskInfoButtons(root_frame)

    def initialize_form(self):
        Label(master=self, text="Task Info").grid(row=0, column=0)

        Label(master=self, text="Name").grid(row=1, column=0)
        self.task_name_entry = Entry(master=self)
        self.task_name_entry.grid(row=1, column=1)
        self.task_name_entry.insert(10, TASK_HELPER.selected_task.name)

        #TODO: Add file dialog
        Label(master=self, text="Target").grid(row=2, column=0)
        self.task_target_entry = Entry(master=self)
        self.task_target_entry.grid(row=2, column=1)
        self.task_target_entry.insert(10, TASK_HELPER.selected_task.target)

        Label(master=self, text="Trigger").grid(row=3, column=0)
        self.task_trigger_entry = Listbox(self, height=len(Trigger), listvariable=StringVar(value=[i.name for i in Trigger]))
        self.task_trigger_entry.grid(row=3,column=1)

    def get_form_task(self):
        #Return content of entry values.
        return Task(name=self.task_name_entry.get(),
                    trigger=self.task_trigger_entry.get(),
                    target=self.task_target_entry)

class TaskInfoButtons(Frame):
    def __init__(self, root_frame):
        from widgets.RootFrame import RootFrame
        super(TaskInfoButtons, self).__init__(master=root_frame, width="100", height="50")
        Button(master=self, text="Save", command=lambda: RootFrame.gi().button_save()).grid(row=2, column=0)
        Button(master=self, text="Delete", command=lambda: RootFrame.gi().button_delete_task(TASK_HELPER.loaded_tasks[-1])).grid(row=2, column=1)
        self.place(anchor="se",relx=1,rely=1)