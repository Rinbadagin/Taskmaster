from tkinter import *
from tkinter.ttk import *

from widgets.TaskList import *
from widgets.TaskInfo import *
from widgets.RootFrame import *
from globals import *

import ctypes, sys

#Code to elevate to administrator as it is necessary to modify tasks
#Taken from https://stackoverflow.com/questions/130763/request-uac-elevation-from-within-a-python-script
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def main():
    """Creates frame and runs the Tkinter main loop. Entrypoint for program."""
    global ROOT_FRAME
    ROOT.title(WINDOW_NAME)
    ROOT_FRAME = RootFrame()
    ROOT_FRAME.place(x=0, y=0)
    ROOT.resizable(False, False)
    # Process: Load Tasks For Taskmaster
    # Generate Widgets
    # Load Widgets
    # Let them interact
    ROOT.mainloop()

if RUN_AS_ADMIN and __name__ == "__main__":
    if is_admin():
        print("User is an admin.")
        main()
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
elif __name__ == "__main__":
    main()