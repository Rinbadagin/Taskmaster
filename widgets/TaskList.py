import PySimpleGUI as sg
from globals import *


class TaskList(sg.Column):
    def __init__(self):
        task_radios = []
        for task in TASK_HELPER.get_tasks():
            task_radios.append(sg.Radio(task.task_name, "TASKSEL"))
        layout =[[sg.Text('Task List')],
                *[task_radios],
                [sg.Button('Refresh', key="refresh"),
                sg.Button('New', key="TLnew")]]
        super(TaskList, self).__init__(layout, key='-TASKLIST-')

    def get_selected_task(self):
        return LOADED_TASKS[int(self.selected_task.get())]

    def update_selected_task(self):
        global SELECTED_TASK
        SELECTED_TASK=self.get_selected_task()

    def new(self):
        print("TODO: Implement actual new functionality.")