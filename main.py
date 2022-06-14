from tkinter import *
from tkinter.ttk import *

from widgets.TaskList import *
from widgets.TaskInfo import *
from globals import *

def main():
    ROOT.title(WINDOW_NAME)
    t_list = TaskList()
    t_list.place(x=0,y=0)
    t_info = TaskInfo()
    t_info.place(x=200,y=0)
    # Process: Load Tasks For Taskmaster
    # Generate Widgets
    # Load Widgets
    # Let them interact
    ROOT.mainloop()


if __name__ == "__main__":
    main()
