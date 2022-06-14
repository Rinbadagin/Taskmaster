import PySimpleGUI as sg
from globals import *


class TaskInfo(sg.Column):
    def __init__(self):
        layout =[[sg.Text('Task Info')],
                    [sg.Button('Save', key="TIsave"),
                    sg.Button('Delete', key="TLdelete"),
                    sg.Button('Trigger', key="TLtrigger")]]
        super(TaskInfo, self).__init__(layout, key='-TASKINFO-')