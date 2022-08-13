from enum import Enum


class Trigger(Enum):
    LOGIN = "ONLOGIN"
    #TODO: IMPLEMENT ALL TRIGGERS

class Task:
    def __init__(self, name="Task", trigger=Trigger.LOGIN, target="C:\Windows\System32\calculator.exe"):
        if not isinstance(trigger, Trigger):
            print("TODO: HANDLE INVALID ENUM")
        self.name = name
        self.trigger = trigger
        self.target = target

    @staticmethod
    def get_task_from_query_output(query_output):
        print("Very bad. TODO: Implement Task Creation from Query Output")
        raise Exception