import uuid
import time

class Task():
  """Representation of a task
  
  Attributes:
              - created - date
              - completed - date
              - name - string
              - unique id - number
              - priority - int value of 1, 2, or 3; 1 is default
              - due date - date, this is optional
  """
  def __init__(self, name, priority = 1, dueDate = None ):
      self.name = name
      self.priority = priority
      self.unique_id = uuid.uuid4()
      self.created = time.time()
      self.due_date= dueDate
      self.completed = None 
