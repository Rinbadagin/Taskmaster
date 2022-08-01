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
        super(RootFrame, self).__init__(master=ROOT, width="400", height="400")
        self.parent_frame = ParentFrame()
        self.parent_frame.place(x=0,y=0)

    def update_gui(self):
        print("UPDATING GUI")
        self.parent_frame.destroy()
        self.parent_frame = ParentFrame()
        self.parent_frame.place(x=0, y=0)

    def button_save(self):
        print(f'loaded: ${TASK_HELPER.loaded_tasks} selected: ${TASK_HELPER.selected_task}')
        TASK_HELPER.save()
        self.update_gui()

    def button_new_task(self, task):
        TASK_HELPER.new_task(task)
        self.update_gui()

    def button_delete_task(self, task):
        TASK_HELPER.delete_task(task)
        self.update_gui()

    def get_tasks(self):
        return TASK_HELPER.get_tasks()

    def get_task_by_index(self, index):
        return TASK_HELPER.get_task_by_index(index)
