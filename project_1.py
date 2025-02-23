import os

# Load tasks from file
def load_tasks(filename="tasks.txt"):
    tasks = []
    if os.path.exists(filename):
        with open(filename, "r") as file:
            for line in file:
                task, status = line.strip().rsplit("|", 1)
                tasks.append((task, status == "Done"))
    return tasks

# Save tasks to file
def save_tasks(tasks, filename="tasks.txt"):
    with open(filename, "w") as file:
        for task, completed in tasks:
            file.write(f"{task}|{'Done' if completed else 'Pending'}\n")

# Display tasks
def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    print("\nTo-Do List:")
    for i, (task, completed) in enumerate(tasks, 1):
        status = "[*]" if completed else "[ ]"
        print(f"{i}. {status} {task}")

# Add a new task
def add_task(tasks, task):
    tasks.append((task, False))  
    print(f"Task '{task}' added.")

# Remove a task
def remove_task(tasks, index):
    if 0 <= index < len(tasks):
        removed_task = tasks.pop(index)
        print(f"Removed task: {removed_task[0]}")
    else:
        print("Invalid task number.")

# Mark a task as complete
def mark_complete(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index] = (tasks[index][0], True)
        print(f"Marked '{tasks[index][0]}' as complete.")
    else:
        print("Invalid task number.")

# Main Program
tasks = load_tasks() 
while True:
    print("\nOptions: 1. View  2. Add  3. Remove  4. Complete  5. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        display_tasks(tasks)
    elif choice == "2":
        task = input("Enter task: ")
        add_task(tasks, task)
    elif choice == "3":
        display_tasks(tasks)
        index = int(input("Enter task number to remove: ")) - 1  
        remove_task(tasks, index)
    elif choice == "4":
        display_tasks(tasks)
        index = int(input("Enter task number to mark complete: ")) - 1  
        mark_complete(tasks, index)
    elif choice == "5":
        save_tasks(tasks) 
        print("Tasks saved. Exiting.")
        break
    else:
        print("Invalid choice. Try again.")
