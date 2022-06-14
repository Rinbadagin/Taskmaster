from Task import *


class TaskHelper:
    def __init__(self):
        print("Running TEST Task Helper, no interaction with actual schtasks")
        self.number_checked = 1

    def save(self):
        print("TODO: SAVE")

    def add_task_to_schedule(self, task):
        print("TODO: ADD TASK")

    def delete_task(self,task):
        print("TODO: DELETE TASK")

    def get_tasks(self):
        print("TODO: RETURN SAVED TASKS")
        fake_data = []
        for i in range(self.number_checked):
            fake_data.append(Task(f'Task {i}', Trigger.LOGIN))
        self.number_checked += 1
        return fake_data

    def get_task_by_index(self,index):
        print("TODO: GET TASK BY INDEX")
        return Task("This is a fake task", Trigger.LOGIN)