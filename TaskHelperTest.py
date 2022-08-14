from Task import *


class TaskHelper:
    loaded_tasks = []
    def __init__(self):
        print("Running TEST Task Helper, no interaction with actual schtasks")
        self.loaded_tasks = [Task("Task 1"), Task("Task 3", target="C:\\demo.exe"), Task(name="Different")]

    def log(self, *content):
        print("(TASK HELPER [test]): ", *content)

    def save(self):
        self.log("TODO: SAVE LOADED TASKS")

    def new_task(self, task):
        self.loaded_tasks.append(task)
        self.log("TODO: ADD TASK")

    def delete_task(self, task):
        self.loaded_tasks.remove(task)
        self.log("TODO: DELETE TASK")

    def delete_task_by_index(self, index):
        del self.loaded_tasks[index]

    def get_tasks(self):
        self.log("TODO: RETURN SAVED TASKS")
        return self.loaded_tasks

    def get_task_by_index(self,index):
        self.log("TODO: GET TASK BY INDEX")
        try:
            return self.loaded_tasks[index]
        except IndexError:
            return EmptyTask()

    def set_task_by_index(self, index, new_task):
        self.log("TODO: SET TASK BY INDEX")
        try:
            self.loaded_tasks[index] = new_task
        except IndexError:
            self.log("User has attempted to edit nonetask")
            from tkinter import messagebox
            messagebox.showerror("Error", "Please create a task first.")