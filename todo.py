import json
import os

FILE_NAME = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

# Show tasks
def show_tasks(tasks):
    print("\n📋 Your Tasks:")
    if not tasks:
        print("No tasks available.\n")
    else:
        for i, task in enumerate(tasks):
            status = "✅" if task["done"] else "❌"
            print(f"{i + 1}. {task['title']} [{status}]")
    print()

# Add task
def add_task(tasks):
    title = input("Enter task: ")
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("Task added successfully!\n")

# Mark task as done
def mark_done(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to mark done: "))
        tasks[num - 1]["done"] = True
        save_tasks(tasks)
        print("Task marked as done!\n")
    except:
        print("Invalid input!\n")

# Delete task
def delete_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: "))
        tasks.pop(num - 1)
        save_tasks(tasks)
        print("Task deleted successfully!\n")
    except:
        print("Invalid input!\n")

# Main program
def main():
    tasks = load_tasks()

    while True:
        print("====== TO-DO LIST MENU ======")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task Done")
        print("4. Delete Task")
        print("5. Exit")
        print("=============================")

        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice!\n")

if __name__ == "__main__":
    main()