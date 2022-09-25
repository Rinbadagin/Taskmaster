from Task import *
from TaskHelperTest import *
import subprocess


class TaskHelperImpl(TaskHelper):
    """Implementation of TaskHelper with interaction with the real schtasks instead of
    an abstraction for testing. This should always be used in production."""
    loaded_tasks = []
    deleted_tasks = []

    def __init__(self):
        print("Running Task Helper, interaction with actual schtasks")
        self.loaded_tasks = []
        self.schtasks_loaded_tasks = []
        self.get_tasks()

    def log(self, *content):
        """Logs content with information specifying it comes from the task helper"""
        print("(TASK HELPER [prod]): ", str(*content).replace('\\n','\n'))

    def run_command_with_output(self, command,shell=True):
        self.log("Running command: "+str(command))
        return subprocess.check_output(command,shell=shell)

    def save(self):
        """Saves loaded tasks"""
        self.log("TODO: SAVE LOADED TASKS")
        for task in self.deleted_tasks:
            try:
                sample_command = f"schtasks /f /delete /tn \"\\task master\\{task.hash_inclusive_name}\""
                task_delete_output = str(self.run_command_with_output(sample_command, shell=True))
                self.log(task_delete_output)
            except subprocess.CalledProcessError as e:
                print(e)
                continue
        for task in self.loaded_tasks:
            print(f'Task: name {task.name} h_inc {task.hash_inclusive_name} in_db {task.name_in_database} trigger {task.trigger} target {task.target}')
            if not task.name_in_database == task.hash_inclusive_name:
                try:
                    sample_command = f"schtasks /f /delete /tn \"\\task master\\{task.name_in_database}\""
                    task_delete_output = str(self.run_command_with_output(sample_command, shell=True))
                    self.log(task_delete_output)
                except subprocess.CalledProcessError as e:
                    print(e)
                    continue
        for task in self.loaded_tasks:
            sample_command = f"schtasks /f /create /tn taskname /tr taskrun /sc taskschedule"
            if task.trigger is Trigger.NONE:
                """Literal garbage. There's no way to make a disabled task directly from the command line
                So it's necessary to make it a scheduled one with an impossible time range.
                Schtasks doesn't need a wrapper, it needs to be abandoned. The code I'm interacting with
                Was written before the sample range I'm using. Honestly annoyed. 02/09/2022"""
                sample_command += " /ST 00:00 /SD 01/01/1900 /ED 02/01/1900"
                sample_command = sample_command.replace("taskschedule", "MONTHLY")
            else:
                sample_command = sample_command.replace("taskschedule", task.trigger.name)
            sample_command = sample_command.replace("taskname",f"\"\\task master\\{task.hash_inclusive_name}\"")\
                .replace("taskrun",task.target if task.target else '/')
            task_create_output = str(self.run_command_with_output(sample_command, shell=True)).replace(":\\", ";\\").replace("\\\\", "\\")
            self.log(task_create_output)
        self.deleted_tasks=[]

    def new_task(self, task):
        """Appends a new task to the loaded tasks. Does not save."""
        self.loaded_tasks.append(task)
        self.log("TODO: ADD TASK")

    def delete_task(self, task):
        """Removes a task from the loaded tasks. Does not save."""
        self.deleted_tasks.append(task)
        self.loaded_tasks.remove(task)
        self.log("TODO: DELETE TASK")

    def delete_task_by_index(self, index):
        """Removes a task from the loaded tasks by array index. Does not save."""
        del self.loaded_tasks[index]

    def get_tasks(self):
        """Returns loaded tasks.
        Eldritch arbitrary output format parsing code. Requires a wizard at the helm."""
        self.log("TODO: RETURN SAVED TASKS")
        task_query_output = ""
        try:
            task_query_output = str(self.run_command_with_output("schtasks /query /tn \"\\task master\"\\ /fo list /v", shell=True)).replace(":\\",";\\").replace(":/",";/").replace("\\\\","\\")
        except subprocess.CalledProcessError as exc:
            print("Schtasks query failed. Assuming no tasks - query fails when no tasks are found."+str(exc.returncode)+str(exc.output))
        task_query_output = [dict([j.strip() for j in i.split(":")[:2]] if len(i.split(":")[:2])==2 else ["key", "value"] for i in task.split("\\r\\n")) for task in task_query_output.split("HostNam")]
        self.log([i for i in task_query_output])
        temporary_tasks = []
        for task_dict in task_query_output:
            if task_dict.get("TaskName"):
                temporary_task = Task(name=task_dict.get("TaskName").replace("\\task master\\", "").replace("\\\\", ""), new = False)
                temporary_task.target=task_dict.get("Task To Run").replace(";\\",":\\").replace(";/",":/")
                temporary_task.trigger=Trigger(task_dict.get("Schedule Type"))
                temporary_tasks.append(temporary_task)
        self.loaded_tasks=self.schtasks_loaded_tasks=temporary_tasks
        return self.loaded_tasks

    def get_task_by_index(self, index):
        """Returns loaded task by index, returning an empty task if it doesn't exist"""
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
