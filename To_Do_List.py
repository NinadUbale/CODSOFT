


tasks = []

def add_task():
    title = input("Enter Task Title: ")
    description = input("Enter Task Description: ")
    due_date = input("Enter Due Date (YYYY-MM-DD): ")
    priority = input("Enter priority (High/Medium/Low): ")
    tasks.append({
        "title": title,
        "description": description,
        "due_date": due_date,
        "priority": priority,
        "completed": False
    })
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No Tasks available.")
        return
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task['title']} (Due: {task['due_date']}, Priority: {task['priority']}, Completed: {task['completed']})")

def update_task():
    if not tasks:
        print("No Tasks available to update.")
        return
    view_tasks()
    task_idx = int(input("Enter the Task number to update: ")) - 1
    if 0 <= task_idx < len(tasks):
        title = input(f"Enter new Title (Current: {tasks[task_idx]['title']}): ")
        description = input(f"Enter new Description (Current: {tasks[task_idx]['description']}): ")
        due_date = input(f"Enter new Due Date (Current: {tasks[task_idx]['due_date']}): ")
        priority = input(f"Enter new priority (Current: {tasks[task_idx]['priority']}): ")
        tasks[task_idx].update({
            "title": title,
            "description": description,
            "due_date": due_date,
            "priority": priority
        })
        print("Task updated successfully!")
    else:
        print("Invalid Task number.")

def delete_task():
    if not tasks:
        print("No Tasks available to delete.")
        return
    view_tasks()
    task_idx = int(input("Enter the Task number to delete: ")) - 1
    if 0 <= task_idx < len(tasks):
        tasks.pop(task_idx)
        print("Task deleted successfully!")
    else:
        print("Invalid Task number.")

def mark_completed():
    if not tasks:
        print("No Tasks available to mark as completed.")
        return
    view_tasks()
    task_idx = int(input("Enter the Task number to mark as completed: ")) - 1
    if 0 <= task_idx < len(tasks):
        tasks[task_idx]["completed"] = True
        print("Task marked as completed!")
    else:
        print("Invalid Task number.")


while True:
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Completed")
    print("6. Exit")
    choice = input("Enter Your Choice: ")
    
    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        update_task()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        mark_completed()
    elif choice == '6':
        print("Program ended....")
        break
    else:
        print("Invalid option. Please try again.")


