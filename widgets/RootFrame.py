import tkinter
from tkinter import *
from tkinter.ttk import *
from globals import *
from widgets.ParentFrame import ParentFrame
from widgets.TaskInfo import TaskInfo
from widgets.TaskList import TaskList


class RootFrame(Frame):
    """Class that controls all window content. Uses a child 'parent-frame' and deletes and
    recreates it to simulate a dynamic GUI though Tkinter doesn't really support it.
    Is a singleton and is the single point of contact for most information necessary for the
    program to run."""
    __instance = None
    parent_frame = None
    selected_task_stringvar = StringVar(ROOT, "0")
    scroll_index = 0

    @staticmethod
    def get_instance():
        """Returns the singleton of RootFrame"""
        if RootFrame.__instance is None:
            RootFrame()
        return RootFrame.__instance

    @staticmethod
    def gi():
        """Shorthand version of getinstance"""
        return RootFrame.get_instance()

    def __init__(self):
        """RootFrame Constructor. Sets up 'parent_frame'"""
        if RootFrame.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            RootFrame.__instance = self
        super(RootFrame, self).__init__(master=ROOT, width=DEFAULT_WIDTH_X, height=DEFAULT_HEIGHT_Y)
        self.parent_frame = ParentFrame()
        self.parent_frame.place(x=0,y=0)

    def update_gui(self):
        """Destroys and recreates parent_frame to simulate a dynamic GUI"""
        self.parent_frame.destroy()
        self.parent_frame = ParentFrame()
        self.parent_frame.place(x=0, y=0)

    def button_save(self):
        """Abstracted save method for a button. Means save code is implemented here
        And not in the creation of the widget, which would be awkward."""
        try:
            self.set_selected_task(self.parent_frame.t_info.get_form_task())
            TASK_HELPER.save()
            self.update_gui()
        except Exception:
            print("Invalid task entered in TaskInfo")

    def button_new_task(self, task):
        """Abstracted new task method for a button."""
        TASK_HELPER.new_task(task)
        self.selected_task_stringvar.set(len(TASK_HELPER.loaded_tasks)-1)
        self.update_gui()

    def button_delete_task(self):
        """Abstracted delete task method for a button.
        Produces an error if there are no tasks in the loaded tasks array."""
        try:
            sel_index = int(self.selected_task_stringvar.get())
            tsk_index = TASK_HELPER.loaded_tasks.index(self.get_selected_task())
            TASK_HELPER.delete_task(self.get_selected_task())
            if sel_index >= tsk_index and sel_index > 0:
                self.selected_task_stringvar.set(str(sel_index-1))
            self.update_gui()
        except ValueError:
            from tkinter import messagebox
            messagebox.showerror("Error", "There are no tasks to delete")

    def button_browse(self):
        """Makes browse popup with filetypes for .exe .bat and .*
        Currently used to select target file"""
        from tkinter import filedialog
        filename = filedialog.askopenfilename(
            title='Select Target',
            initialdir='/',
            filetypes=(('Executable Files (.exe)', '*.exe'),('Script Files (.bat)', '*.bat'),('All Files (*.*)', '*.*')))
        self.parent_frame.t_info.task_target_entry.delete(0, END)
        self.parent_frame.t_info.task_target_entry.insert(0, filename)

    def get_tasks(self):
        """Task Helper abstraction: gets tasks. .-."""
        return TASK_HELPER.get_tasks()

    def get_task_by_index(self, index):
        """Task Helper abstraction: gets task by index. .-."""
        return TASK_HELPER.get_task_by_index(index)

    def get_selected_task(self):
        """Task Helper abstraction: gets selected task. .-."""
        return TASK_HELPER.get_task_by_index(int(self.selected_task_stringvar.get()))

    def set_selected_task(self, new_task):
        """Task Helper abstraction: sets selected task. .-."""
        TASK_HELPER.set_task_by_index(int(self.selected_task_stringvar.get()), new_task)