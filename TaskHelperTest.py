from Task import *


class TaskHelper:
    loaded_tasks = []
    selected_task = Task()
    def __init__(self):
        print("Running TEST Task Helper, no interaction with actual schtasks")
        self.loaded_tasks = [Task("Task 1"), Task("Task 3", target="C:\\demo.exe"), Task(name="Different")]

    def save(self):
        print("TODO: SAVE LOADED TASKS")

    def new_task(self, task):
        self.loaded_tasks.append(task)
        print("TODO: ADD TASK")

    def delete_task(self, task):
        self.loaded_tasks.remove(task)
        print("TODO: DELETE TASK")

    def get_tasks(self):
        print("TODO: RETURN SAVED TASKS")
        return self.loaded_tasks

    def get_task_by_index(self,index):
        print("TODO: GET TASK BY INDEX")
        return Task("This is a fake task", Trigger.LOGIN)