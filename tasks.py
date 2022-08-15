import time
import datetime
from task import Task
import pickle
from tabulate import tabulate
class Tasks:

    
    def __init__(self):
            """Read pickled tasks file into a list"""
            try: 
                with open('.todo.pickle', 'rb') as f:
                    self.tasks = pickle.load(f)
            except:
                    self.tasks = []
            # List of Task objects
            #self.new_tasks = [] 
            #try:
                #self.tasks = pickle.load(open(".todo", "wb"))
            #except (OSError) as e:
                #self.tasks = open(".todo", "wb")

    def pickle_tasks(self):
            """Pickle your task list to a file"""
            with open('.todo.pickle', 'wb') as f:
                pickle.dump(self.tasks, f)

        # Complete the rest of the methods, change the method definitions as needed
    def list(self):
        data = []
        object_data = []
        for i in self.tasks:
            object_data.append(i.unique_id)
            #calculate age
            print(i.created)
            now = time.ctime(int(i.created))
            print("the now time is " + str(now))
        
            now = time.time()
            print(now)
            age = now - i.created
            seconds_in_day = age / (60*60*24)
            print(seconds_in_day)
            object_data.append(i.due_date)
            object_data.append(i.priority)
            object_data.append(i.name)
            
            object_data.append(i.created)
            object_data.append(i.completed)
            data.append(object_data)
        print(data)
        print (tabulate(data, headers=["ID", "Age", "Due Date", "Priority", "Task"]))

    def report(self):
            pass

    def done(self):
            pass

    def query(self):
            pass

    def add(self, task):
            self.tasks.append(task)
            return task.unique_id

