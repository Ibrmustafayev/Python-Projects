📝 To-Do List Manager (Python CLI)
A simple yet functional command-line To-Do List Manager written in Python.
This program allows users to add, view, edit, complete, and delete tasks, with all data stored persistently in a JSON file.
Colored terminal output is used to improve readability and user experience.

🚀 Features
  📂 Persistent Storage
    Tasks are saved in a todo_list.json file, so your data is not lost after closing the program.
  👀 View Tasks
    Displays all tasks with their current status:
      -[Pending]
      -[Complete]
  ➕ Add Tasks
    Add new tasks with input validation to prevent empty entries.
  ✅ Mark Tasks as Complete
    Select a task by number and mark it as completed.
  ✏️ Edit Tasks
    Modify the description of any existing task.
  🗑 Delete Tasks
    Remove tasks safely by selecting their number.
  🎨 Colored Terminal Output
    Uses colorama to clearly distinguish messages, errors, and statuses.
  🛡 Error Handling
    Prevents crashes caused by:
      -Missing or corrupted JSON files
      -Invalid user input

🛠 Technologies Used
Python 3:
  JSON – for task storage
  os – file existence checks
  colorama – colored terminal output
