import argparse
import pickle 
import uuid
import tasks
import task
import os

def main():
    """main code that runs program"""

parser = argparse.ArgumentParser(description="Update your to do list")
parser.add_argument("--add", type=str, required=False, help='a task string to add to your list')
parser.add_argument("--priority", type=int, required=False, default=1, help='priority of task; default value is 1')
parser.add_argument("--due", type=str, required=False, default = " ", help='due date in DD/MM/YYYY format')
parser.add_argument("--query", type=str, required=False, nargs= "+" , help='priority of task; default value is 1')
parser.add_argument("--list", action="store_true", required=False, help='lists all tasks that have not been completed')


#Parse the argument
args= parser.parse_args()

new_tasks_instance = tasks.Tasks()

if args.add:

    if (args.add).replace(" ", "").isalpha():
        print(f"add {args.add} with priority of {args.priority} and due date {args.due}")
        create_task = task.Task(args.add, args.priority, args.due)
        new_task = new_tasks_instance.add(create_task)
        print(f"Created task {new_task}")
        new_tasks_instance.pickle_tasks()

    else:
        print(f"There was an error in creating your task. Run 'todo -h' for usage instructions.")
elif args.list:
    list = new_tasks_instance.list()
    print(list)
    #os.remove(PICKLE_FILE)
#do something with the data

exit()

if __name__ == "__main__":
    main()