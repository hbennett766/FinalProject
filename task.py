import random
import uuid
from datetime import datetime

class Task():
  """Representation of a task
  
  Attributes:
              - created - date
              - completed - bool
              - completion_time - datetime
              - name - string
              - unique id - number
              - priority - int value of 1, 2, or 3; 1 is default
              - due date - date, this is optional
  """
  def __init__(self, name, priority = 1, dueDate = "" ):
      self.name = name
      self.priority = priority
      self.unique_id = random.randint(1,1000)
      self.created = datetime.now()
      self.due_date= dueDate
      self.completed = False
      self.completion_time = None
      print(self)
      print(type(self.due_date))
  def __str__(self):
     name = self.name
     priority = self.priority
     unique_id = self.unique_id
     created = self.created
     due_date = self.due_date
     completed = self.completed
     completion_time = self.completion_time
     string = f"{name}\n {priority}\n {unique_id}\n {created}\n {due_date}\n {completed}"
     return string