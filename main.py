import PySimpleGUI as sg

from widgets.TaskList import *
from widgets.TaskInfo import *
import globals as gb


def main():
    sg.theme(gb.THEME)
    task_list, task_info = (TaskList(), TaskInfo())
    gb.WINDOW = sg.Window(gb.WINDOW_NAME, [[task_list, task_info]])
    while True:  # Event Loop
        event, values = gb.WINDOW.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event.startswith('TL'):
            #Funky method I made that dynamically grabs the relevant method from associated class
            #Honestly quite proud of it haha
            getattr(task_list,event[2::],lambda: print(f":// No relevant method found: {event} | {values} | {event[2::]}"))()
        if event.startswith('TI'):
            getattr(task_info,event[2::],lambda: print(f":// No relevant method found: {event} | {values} | {event[2::]}"))()
        if event == 'refresh':
            print(TASK_HELPER.number_checked)
            task_list = TaskList()
            task_info = TaskInfo()
    gb.WINDOW.close()


if __name__ == "__main__":
    main()
