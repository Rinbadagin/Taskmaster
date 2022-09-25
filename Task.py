from enum import Enum
from time import time_ns


class Trigger(Enum):
    """Enum for task triggers in schtasks."""
    NONE = "Monthly"
    ONSTART = "At system start up"
    ONLOGON = "At logon time"
    #TODO: IMPLEMENT ALL TRIGGERS

class Task:
    """Task abstraction for the wrapper to deal with. Will be constructed from
    GUI input and SchTasks output"""
    def __init__(self, name="New Task", trigger=Trigger.NONE, target="", new=True):
        if not isinstance(trigger, Trigger):
            print("TODO: HANDLE INVALID ENUM")
        self.created_time = time_ns()
        self.name_in_database = name
        self.generate_hash_inclusive_name(name)
        self.trigger = trigger
        self.target = target
        self.new = new

    @staticmethod
    def get_task_from_query_output(query_output):
        print("Very bad. TODO: Implement Task Creation from Query Output")
        raise Exception

    def hash(self, n):
        """Returns first n characters of a base64-encoded hash of this task
        and the current time in nanoseconds. Using 8 characters there is a 1/280 trillion chance
        of any two hashes colliding. Used to uniquely identify tasks in taskmaster allowing
        Multiple to have the same name even though the task scheduler doesn't."""
        if hasattr(self, 'hash_inclusive_name'):
            return self.hash_inclusive_name[:n]
        from hashlib import sha256
        from time import time_ns
        from base64 import b64encode
        #using b64: hash_value = b64encode(sha256(f'{self.name}{self.target}{self.trigger}{self.created_time}'.encode('utf-8')).digest()).decode()
        hash_value = sha256(f'{self.created_time}'.encode('utf-8')).hexdigest()
        return hash_value[:n]

    def generate_hash_inclusive_name(self, name):
        try:
            self.name = name.split("I",1)[1]
            self.hash_inclusive_name = name
        except IndexError as e:
            self.name = name
            self.hash_inclusive_name = f"{self.hash(8)}I{self.name}"
            print(f"Index error in Task {self.name} {self.hash_inclusive_name}")
class EmptyTask(Task):
    """This is used in the task info panel when there are no loaded tasks. It should never be saved."""
    def __init__(self, name="No Task Selected", trigger=Trigger.NONE, target="?"):
        if not isinstance(trigger, Trigger):
            print("TODO: HANDLE INVALID ENUM")
        self.name = name
        self.trigger = trigger
        self.target = target