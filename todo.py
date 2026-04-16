import json
import os

FILE_NAME = "tasks.json"

# Load tasks
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save tasks
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

# Show tasks
def show_tasks(tasks):
    print("\n📋 Your Tasks:")
    if not tasks:
        print("No tasks available.\n")
        return

    for i, task in enumerate(tasks):
        status = "✅" if task["done"] else "❌"
        priority = task.get("priority", "Medium")
        print(f"{i + 1}. {task['title']} [{status}] (Priority: {priority})")
    print()

# Add task
def add_task(tasks):
    title = input("Enter task: ")

    print("Select Priority:")
    print("1. High")
    print("2. Medium")
    print("3. Low")

    choice = input("Choose priority (1-3): ")

    if choice == "1":
        priority = "High"
    elif choice == "2":
        priority = "Medium"
    elif choice == "3":
        priority = "Low"
    else:
        print("Invalid choice! Default set to Medium.")
        priority = "Medium"

    tasks.append({
        "title": title,
        "done": False,
        "priority": priority
    })

    save_tasks(tasks)
    print("✅ Task added successfully!\n")

# Mark task as done
def mark_done(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to mark done: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            save_tasks(tasks)
            print("✅ Task marked as done!\n")
        else:
            print("Invalid task number!\n")
    except ValueError:
        print("Please enter a valid number!\n")

# Delete task
def delete_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"🗑️ Deleted: {removed['title']}\n")
        else:
            print("Invalid task number!\n")
    except ValueError:
        print("Please enter a valid number!\n")

# Main menu
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
