import json                                                                                             # Import json module to store and load tasks from a file
import os                                                                                               # Import os to check if the file exis
from colorama import Fore                                                                               # Import Fore from colorama to print colored text in terminal

file_name = "todo_list.json"                                                                            # File where tasks will be saved

def load_tasks():
    """
    Loads tasks from the JSON file.
    If the file does not exist or is broken,
    it creates a new file with an empty task list.
    """
    try:
        with open(file_name, "r") as file:                                                              # Open file in read mode
            return json.load(file)                                                                      # Convert JSON data into Python dictionary
    except:                                     
        if not os.path.exists(file_name):                                                               # If file does not exist, create it
            with open(file_name, "w") as file:
                json.dump({"tasks": []}, file)                                                          # Initialize file with empty tasks list
        return {"tasks": []}                                                                            # Return empty structure to avoid crashes

def save_tasks(tasks):                                                                                  # Saves the current tasks dictionary into the JSON file.
    try:
        with open(file_name, "w") as file:                                                              # Open file in write mode (overwrites existing data)
            json.dump(tasks, file)                                                                      # Convert Python dictionary to JSON and save
    except:
        print(Fore.RED + "Failed to save.")                                                             # Error message if saving fails

def view_tasks(tasks):                                                                                  #Displays all tasks with their status.
    task_list = tasks["tasks"]
    if len(task_list) == 0:                                                                             # If there are no tasks
        print(Fore.RED + "\nNo task to display.")
    else:
        print(Fore.LIGHTYELLOW_EX + "\nYour To-Do List:")
        for idx, task in enumerate(task_list):                                                          # enumerate gives index + value
            status = "[Complete]" if task["complete"] else "[Pending]"                                  # Determine task status
            print(f"{idx+1}. {task['description']} | {status}")

def add_task(tasks):                                                                                    # Adds a new task to the list.
    description = input("\nEnter the task description: ").strip()                                       # Take task description from user
    if description:                                                                                     # Prevent empty input
        tasks["tasks"].append({"description": description, "complete": False})                          # Add new task as a dictionary
        save_tasks(tasks)                                                                               # Save updated tasks
        print(Fore.GREEN + "Task added.")
    else:
        print(Fore.RED + "Description cannot be empty!")

def complete_task(tasks):                                                                               # Marks a selected task as completed.
    view_tasks(tasks)
    if len(tasks["tasks"]) == 0:                                                                        # If no tasks exist, exit function
        return
    try:
        task_number = int(input(Fore.WHITE + "Enter the task number to mark as complete: ").strip())    # Ask user for task number
        if 1 <= task_number <= len(tasks["tasks"]):                                                     # Validate task number range
            tasks["tasks"][task_number-1]["complete"] = True                                            # Mark task as complete
            save_tasks(tasks)                                                                           # Save changes
            print(Fore.GREEN + "The task marked as compolete.")
        else:
            print(Fore.RED + "Invalid task number!!!")
    except:
        print(Fore.RED + "Enter a valid number!!!")

def delete_task(tasks):                                                                                 # Deletes a selected task.
    view_tasks(tasks)
    if len(tasks["tasks"]) == 0:                                                                        # Exit if no tasks
        return
    try:
        task_number = int(input(Fore.WHITE + "Enter the task number to delete: ").strip())              # Ask user for task number
        if 1 <= task_number <= len(tasks["tasks"]):                                                     # Validate input range
            tasks["tasks"].pop(task_number-1)                                                           # Remove task from list
            save_tasks(tasks)                                                                           # Save updated list
            print(Fore.GREEN + "The task deleted.")
        else:
            print(Fore.RED + "Invalid task number!!!")
    except:
        print(Fore.RED + "Enter a valid number!!!")

def edit_task(tasks):                                                                                   # Edits the description of an existing task.
    view_tasks(tasks)
    if len(tasks["tasks"]) == 0:                                                                        # Exit if task list is empty
        return
    try:
        task_number = int(input(Fore.WHITE + "Enter the task number to edit: ").strip())                # Ask for task number
        if 1 <= task_number <= len(tasks["tasks"]):                     
            tasks["tasks"][task_number-1]["description"] = input("Enter new task description: ").strip()# Update description
            save_tasks(tasks)                                                                           # Save changes
            print(Fore.GREEN + "The task edited.")
        else:
            print(Fore.RED + "Invalid task number!!!")
    except:
        print(Fore.RED + "Enter a valid number!!!")


def main():                                                                                             # Main program loop.
    tasks = load_tasks()                                                                                # Load tasks from file
    while True:                                                                                         # Run menu until user exits
        print(Fore.BLUE + "\nTo-Do List Manager")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Edit Task")
        print("6. Exit" + Fore.WHITE)

        choice = input("Enter your choice: ").strip()                                                   # Get user choice
        # Menu handling
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            edit_task(tasks)
        elif choice == "6":
            print(Fore.YELLOW + "\nGoodbye!!!" + Fore.WHITE)
            break
        else:
            print(Fore.RED + "Invalid choice!!! Please, try again.")

main()                                                                                                  # Start the program