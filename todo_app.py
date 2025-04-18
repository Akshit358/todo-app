"""

Project todo_app.py

We want a console app that can:
    Add a new task
    View all tasks
    Mark a task as completed
    Delete a task
    Save tasks to a file
    Load tasks when the app starts
"""

# Write the pseudocode of this project








# Name all the concepts that have been used in this project
'''
Concept: File Handling

This lets you save data permanently. Without this
everytime you close the app, your tasks will be lost

'''

# Load and save tasks

def load_tasks(filename="tasks.txt"):
    tasks = []
    try: # try...except avoids the error if the file doesn't exist
        with open(filename, "r") as file: # Opens a file in read mode
            for line in file:
                task, status = line.strip().split("|") # Splits each line into task and status
                tasks.append({"task":task, "done":status=="done"}) # Add it to a list so we can use it in the program
    except FileNotFoundError:
        pass
    return tasks


# def save_tasks
# This saves all of your tasks in a text file before you exit the loop
# It converts our task list into plain text format so it can be reloaded next time
def save_tasks(tasks, filename = "tasks.txt"):
    with open(filename, "w") as file:
        for task in tasks:
            status = "done" if task["done"] else "not done"
            file.write(f"{task['task']}|{status}\n")


# Part 2: Display Menu

def show_menu():
    print("\n=== TO-DO LIST MENU ===")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

# Part 3: Handle Options

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["done"] else "✗"
        print(f"{i}. {task['task']} [{status}]")

def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append({"task": task, "done": False})

def mark_done(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to mark as done: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
    except ValueError:
        print("Invalid input.")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num - 1)
    except ValueError:
        print("Invalid input.")

# Part 4: Main App Loop

def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
