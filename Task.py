from enum import Enum


class Trigger(Enum):
    LOGIN = "ONLOGIN"
    #TODO: IMPLEMENT ALL TRIGGERS

class Task:
    def __init__(self, task_name="Task", task_trigger=Trigger.LOGIN, executable="C:\Windows\System32\calculator.exe"):
        if not isinstance(task_trigger, Trigger):
            print("TODO: HANDLE INVALID ENUM")
        self.task_name = task_name
        self.task_trigger = task_trigger
        self.executable=executable

    @staticmethod
    def get_task_from_query_output(query_output):
        print("Very bad. TODO: Implement Task Creation from Query Output")
        raise Exception