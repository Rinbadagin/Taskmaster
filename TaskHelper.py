from Task import *
from TaskHelperTest import *


class TaskHelperImpl(TaskHelper):
    """Implementation of TaskHelper with interaction with the real schtasks instead of
    an abstraction for testing. This should always be used in production."""
    loaded_tasks = []

    def __init__(self):
        print("Running Task Helper, interaction with actual schtasks")
        self.loaded_tasks = []

    def log(self, *content):
        """Logs content with information specifying it comes from the task helper"""
        print("(TASK HELPER [prod]): ", *content)

    def save(self):
        """Saves loaded tasks"""
        self.log("TODO: SAVE LOADED TASKS")

    def new_task(self, task):
        """Appends a new task to the loaded tasks. Does not save."""
        self.loaded_tasks.append(task)
        self.log("TODO: ADD TASK")

    def delete_task(self, task):
        """Removes a task from the loaded tasks. Does not save."""
        self.loaded_tasks.remove(task)
        self.log("TODO: DELETE TASK")

    def delete_task_by_index(self, index):
        """Removes a task from the loaded tasks by array index. Does not save."""
        del self.loaded_tasks[index]

    def get_tasks(self):
        """Returns loaded tasks."""
        self.log("TODO: RETURN SAVED TASKS")
        return self.loaded_tasks

    def get_task_by_index(self, index):
        """Returns loaded task by index, returning an empty task if it doesn't exist"""
        self.log("TODO: GET TASK BY INDEX")
        try:
            return self.loaded_tasks[index]
        except IndexError:
            return EmptyTask()

    def set_task_by_index(self, index, new_task):
        """Sets task by index, producing an error message if the task at given index does not exist."""
        self.log("TODO: SET TASK BY INDEX")
        try:
            self.loaded_tasks[index] = new_task
        except IndexError:
            self.log("User has attempted to edit nonetask")
            from tkinter import messagebox
            messagebox.showerror("Error", "Please create a task first.")
