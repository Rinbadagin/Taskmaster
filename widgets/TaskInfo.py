from tkinter import *
from tkinter.ttk import *
from globals import *


class TaskInfo(Frame):
    task_name_entry = None
    task_target_entry = None
    task_trigger_variable = None
    task_trigger_entry = None

    def __init__(self, root_frame):
        from widgets.RootFrame import RootFrame
        super(TaskInfo, self).__init__(master=root_frame, width="100", height="50")
        self.initialize_form()
        self.place(anchor="ne", relx=1)
        self.buttons = TaskInfoButtons(root_frame)

    def initialize_form(self):
        from widgets.RootFrame import RootFrame
        Label(master=self, text="Task Info").grid(row=0, column=0)

        Label(master=self, text="Name").grid(row=1, column=0)
        self.task_name_entry = Entry(master=self, width=15)
        self.task_name_entry.grid(row=1, column=1, sticky=W)
        self.task_name_entry.insert(10, RootFrame.gi().get_selected_task().name)

        # TODO: Add file dialog
        Label(master=self, text="Target").grid(row=2, column=0)
        self.task_target_entry = Entry(master=self, width=40)
        self.task_target_entry.grid(row=2, column=1, sticky=W)
        self.task_target_entry.insert(10, RootFrame.gi().get_selected_task().target)
        self.task_target_browse = Button(master=self, text="Browse", command=lambda: RootFrame.gi().button_browse()).grid(row=2, column=2, sticky=W)

        Label(master=self, text="Trigger").grid(row=3, column=0)
        self.task_trigger_variable = StringVar(value=RootFrame.gi().get_selected_task().trigger.name)
        self.task_trigger_entry = OptionMenu(self, self.task_trigger_variable, self.task_trigger_variable.get(),
                                             *[i.name for i in Trigger])
        self.task_trigger_entry.grid(row=3, column=1, sticky=W)

    def validate_form(self):
        from os.path import exists
        name, trigger, target = (
            self.task_name_entry.get(), Trigger[self.task_trigger_variable.get()], self.task_target_entry.get())
        message = ""
        if len(TASK_HELPER.loaded_tasks)>0:
            if len(target) > TARGET_MAXLENGTH:
                message += f"Target exceeds maximum length ({TARGET_MAXLENGTH} chars)\n"
            if not trigger in Trigger:
                message += f"Trigger must be valid\n"
            if not exists(target) and target != "":
                message += f"Target file does not exist/cannot be read by Taskmaster"
            if not message:
                return True
        else:
            message += f"There are no tasks to save"
        from tkinter import messagebox
        messagebox.showerror("Error", "Task has not been saved. Here's why:\n"+message)
        return False

    def get_form_task(self):
        if not self.validate_form():
            raise Exception
        # Return content of entry values.
        return Task(name=self.task_name_entry.get(),
                    trigger=Trigger[self.task_trigger_variable.get()],
                    target=self.task_target_entry.get())


class TaskInfoButtons(Frame):
    def __init__(self, root_frame):
        from widgets.RootFrame import RootFrame
        super(TaskInfoButtons, self).__init__(master=root_frame, width="200", height="50")
        Button(master=self, text="Save Task", command=lambda: RootFrame.gi().button_save()).grid(row=2, column=0, padx=40)
        Button(master=self, text="Delete", command=lambda: RootFrame.gi().button_delete_task()).grid(row=2, column=1)
        self.place(anchor="se", relx=1, rely=1)
