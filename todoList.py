# To-Do List Application

# Function to display the menu
def display_menu():
    print("\n=== To-Do List ===")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Remove a task")
    print("5. Exit")
    print("===================")

# Function to add a task
def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append({"task": task, "completed": False})
    print(f'Task "{task}" added!')

# Function to view tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("\nTasks:")
        for i, task in enumerate(tasks):
            status = "✓" if task["completed"] else "✗"
            print(f"{i + 1}. [{status}] {task['task']}")

# Function to mark a task as completed
def mark_completed(tasks):
    view_tasks(tasks)
    task_number = int(input("Enter the task number to mark as completed: ")) - 1
    if 0 <= task_number < len(tasks):
        tasks[task_number]["completed"] = True
        print(f'Task "{tasks[task_number]["task"]}" marked as completed!')
    else:
        print("Invalid task number.")

# Function to remove a task
def remove_task(tasks):
    view_tasks(tasks)
    task_number = int(input("Enter the task number to remove: ")) - 1
    if 0 <= task_number < len(tasks):
        removed_task = tasks.pop(task_number)
        print(f'Task "{removed_task["task"]}" removed!')
    else:
        print("Invalid task number.")

# Main function to run the application
def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_completed(tasks)
        elif choice == "4":
            remove_task(tasks)
        elif choice == "5":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")

# Run the application
if __name__ == "__main__":
    main()
