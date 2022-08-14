from genericpath import exists
from venv import create
from task import Task
import pickle


class Tasks:

    
    def __init__(self):
            """Read pickled tasks file into a list"""
            # List of Task objects
            self.new_tasks = [] 
            try:
                self.tasks = pickle.load(open(".todo", "wb"))
            except (OSError) as e:
                self.tasks = open(".todo", "wb")

    def pickle_tasks(self):
            """Pickle your task list to a file"""
            pickle.dump(self.new_tasks, self.tasks)
            self.tasks.close()

        # Complete the rest of the methods, change the method definitions as needed
    def list(self):
        self.tasks.close()
        objects = []
        file_name = ".todo"

        with (open(file_name, "rb")) as f:
            while True:
                try:
                    objects.append(pickle.load(f))
                    for s in objects:
                        print(s)
                except EOFError:
                    print("ssss")
                    break
        return objects
    def report(self):
            pass

    def done(self):
            pass

    def query(self):
            pass

    def add(self, task:Task):
            self.new_tasks.append(task)
            return task.unique_id

