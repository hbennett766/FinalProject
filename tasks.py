
from datetime import datetime
from operator import itemgetter
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
        for i in self.tasks:
            object_data = []
            if i.completed != True:
                #id
                object_data.append(i.unique_id)
                #calculate age
                time_now = datetime.now()
                age = time_now - i.created
                object_data.append(age.days)
                #due
                object_data.append(i.due_date)
                #priority
                object_data.append(i.priority)
                #task
                object_data.append(i.name)
                #add to list
                data.append(object_data)
        print(data)
        #order data before tabulating 
        #first by due date
        #then by priority
        data = sorted(data, key=itemgetter(2))
        data = sorted(data, key=itemgetter(3))
        print (tabulate(data, headers=["ID", "Age", "Due Date", "Priority", "Task"]))

    def report(self):
        data = []
        for i in self.tasks:
                object_data = []
                #id
                object_data.append(i.unique_id)
                #calculate age
                time_now = datetime.now()
                age = time_now - i.created
                object_data.append(age.days)
                #due
                object_data.append(i.due_date)
                #priority
                object_data.append(i.priority)
                #task
                object_data.append(i.name)
                #created
                object_data.append(i.created)
                #completed
                object_data.append(i.completion_time)
                #add to list
                data.append(object_data)
        print(data)
        
        print (tabulate(data, headers=["ID", "Age", "Due Date", "Priority", "Task", "Created", "Completed"]))


    def done(self, task_id):
        #change completed from false to true and save to data
        for i in self.tasks:
             if int(i.unique_id) == task_id:
                i.completed = True
                i.completion_time = datetime.now()
                print(i)
        with open('.todo.pickle', 'wb') as f:
              pickle.dump(self.tasks, f)
                        
    def delete(self, task_id):
        for i in self.tasks:
             if int(i.unique_id) == task_id:
                self.tasks.pop(self.tasks.index(i))
        with open('.todo.pickle', 'wb') as f:
              pickle.dump(self.tasks, f)

    def query(self, query_terms):
            data = []
            for task in self.tasks:
                object_data = []
                for term in query_terms:
                        if term in task.name and task.completed != True:
                                object_data.append(task.unique_id)
                                #calculate age
                                time_now = datetime.now()
                                age = time_now - task.created
                                object_data.append(age.days)
                                #due
                                object_data.append(task.due_date)
                                #priority
                                object_data.append(task.priority)
                                #task
                                object_data.append(task.name)
                                #add to list
                                data.append(object_data)
                                print(data)
            print (tabulate(data, headers=["ID", "Age", "Due Date", "Priority", "Task"]))


    def add(self, task):
            self.tasks.append(task)
            return task.unique_id

