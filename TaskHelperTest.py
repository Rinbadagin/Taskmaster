from Task import *


class TaskHelper:
    def __init__(self):
        print("Running TEST Task Helper, no interaction with actual schtasks")

    def save(self):
        print("TODO: SAVE")

    def add_task_to_schedule(self, task):
        print("TODO: ADD TASK")

    def delete_task(self,task):
        print("TODO: DELETE TASK")

    def get_tasks(self):
        print("TODO: RETURN SAVED TASKS")
        return [Task("Task 1", Trigger.LOGIN), Task("Task 2", Trigger.LOGIN)]

    def get_task_by_index(self,index):
        print("TODO: GET TASK BY INDEX")
        return Task("This is a fake task", Trigger.LOGIN)