tasks = []

def add_task(task):
    tasks.append(task)
    print(f'Task "{task}" added!')

def view_tasks():
    if tasks:
        print("\nYour Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("\nNo tasks found!")

def remove_task(task_number):
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f'Task "{removed_task}" removed!')
    else:
        print("Invalid task number!")

while True:
    print("\nOptions:\n1. Add Task\n2. View Tasks\n3. Remove Task\n4. Exit")
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        view_tasks()
        task_number = int(input("Enter task number to remove: "))
        remove_task(task_number)
    elif choice == "4":
        print("Exiting... Have a great day!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 4.")
