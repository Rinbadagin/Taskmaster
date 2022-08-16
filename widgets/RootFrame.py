import tkinter
from tkinter import *
from tkinter.ttk import *
from globals import *
from widgets.ParentFrame import ParentFrame
from widgets.TaskInfo import TaskInfo
from widgets.TaskList import TaskList


class RootFrame(Frame):
    __instance = None
    parent_frame = None
    selected_task_stringvar = StringVar(ROOT, "0")
    scroll_index = 0

    @staticmethod
    def get_instance():
        if RootFrame.__instance is None:
            RootFrame()
        return RootFrame.__instance

    @staticmethod
    def gi():
        """Shorthand version"""
        return RootFrame.get_instance()

    def __init__(self):
        if RootFrame.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            RootFrame.__instance = self
        super(RootFrame, self).__init__(master=ROOT, width=DEFAULT_WIDTH_X, height=DEFAULT_HEIGHT_Y)
        self.parent_frame = ParentFrame()
        self.parent_frame.place(x=0,y=0)

    def update_gui(self):
        self.parent_frame.destroy()
        self.parent_frame = ParentFrame()
        self.parent_frame.place(x=0, y=0)

    def button_save(self):
        self.set_selected_task(self.parent_frame.t_info.get_form_task())
        TASK_HELPER.save()
        self.update_gui()

    def button_new_task(self, task):
        TASK_HELPER.new_task(task)
        self.selected_task_stringvar.set(len(TASK_HELPER.loaded_tasks)-1)
        self.update_gui()

    def button_delete_task(self):
        sel_index = int(self.selected_task_stringvar.get())
        tsk_index = TASK_HELPER.loaded_tasks.index(self.get_selected_task())
        TASK_HELPER.delete_task(self.get_selected_task())
        if sel_index >= tsk_index and sel_index > 0:
            self.selected_task_stringvar.set(str(sel_index-1))
        self.update_gui()

    def get_tasks(self):
        return TASK_HELPER.get_tasks()

    def get_task_by_index(self, index):
        return TASK_HELPER.get_task_by_index(index)

    def get_selected_task(self):
        return TASK_HELPER.get_task_by_index(int(self.selected_task_stringvar.get()))

    def set_selected_task(self, new_task):
        TASK_HELPER.set_task_by_index(int(self.selected_task_stringvar.get()), new_task)