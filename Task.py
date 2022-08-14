from enum import Enum


class Trigger(Enum):
    NONE = "None"
    LOGIN = "On login"
    #TODO: IMPLEMENT ALL TRIGGERS

class Task:
    def __init__(self, name="New Task", trigger=Trigger.NONE, target=""):
        if not isinstance(trigger, Trigger):
            print("TODO: HANDLE INVALID ENUM")
        self.name = name
        self.trigger = trigger
        self.target = target

    @staticmethod
    def get_task_from_query_output(query_output):
        print("Very bad. TODO: Implement Task Creation from Query Output")
        raise Exception

class EmptyTask(Task):
    """This is used in the task info panel when there are no loaded tasks. It should never be saved."""
    def __init__(self, name="No Task Selected", trigger=Trigger.NONE, target="?"):
        if not isinstance(trigger, Trigger):
            print("TODO: HANDLE INVALID ENUM")
        self.name = name
        self.trigger = trigger
        self.target = target