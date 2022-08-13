from tkinter import *
from tkinter.ttk import *

from widgets.TaskList import *
from widgets.TaskInfo import *
from widgets.RootFrame import *
from globals import *

def main():
    global ROOT_FRAME
    ROOT.title(WINDOW_NAME)
    ROOT_FRAME = RootFrame()
    ROOT_FRAME.place(x=0,y=0)
    ROOT.resizable(False, False)
    # Process: Load Tasks For Taskmaster
    # Generate Widgets
    # Load Widgets
    # Let them interact
    ROOT.mainloop()


if __name__ == "__main__":
    main()
