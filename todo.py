import argparse
import pickle  
import uuid
from tasks import Tasks
from task import Task
import os

def main():
    """main code that runs program"""

parser = argparse.ArgumentParser(description="Update your to do list")
parser.add_argument("--add", type=str, required=False, help='a task string to add to your list')
parser.add_argument("--priority", type=int, required=False, default=1, help='priority of task; default value is 1')
parser.add_argument("--due", type=str, required=False, default = "", help='due date in DD/MM/YYYY format')
parser.add_argument("--query", type=str, required=False, nargs= "+" , help='search for tasks')
parser.add_argument("--list", action="store_true", required=False, help='lists all tasks that have not been completed')
parser.add_argument("--done", type=int, required=False, help= 'follow with task ID to mark task as completed')
parser.add_argument("--delete", type=int, required=False, help= 'follow with task ID to remove from list')
parser.add_argument("--report", action="store_true", required=False, help= 'shows all completed and uncompleted tasks')
#Parse the argument
args= parser.parse_args()

new_tasks_instance = Tasks()

if args.add:

    if (args.add).replace(" ", "").isalpha():
        if args.priority >= 1 and args.priority <= 3:
            created_task = Task(args.add, args.priority, args.due)
            new_task = new_tasks_instance.add(created_task)
            print(f"Created task {new_task}")
            new_tasks_instance.pickle_tasks()
        else:
            print("Priority must have a value of 1, 2, or 3. 1 being the highest. Try again")

    else:
        print("There was an error in creating your task. Run 'todo -h' for usage instructions.")

elif args.list:
    list = new_tasks_instance.list()

elif args.done:
    mark_done = new_tasks_instance.done(args.done)
    print(f"Completed task {args.done}")

elif args.delete:
    delete_task = new_tasks_instance.delete(args.delete)
    print(f"Deleted task {args.delete}")

elif args.report:
    new_tasks_instance.report()

elif args.query:
    new_tasks_instance.query(args.query)


exit()

if __name__ == "__main__":
    main()