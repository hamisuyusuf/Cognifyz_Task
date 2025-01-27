#!/usr/bin/python3

class Task:
    """Class to represent a task."""
    def __init__(self, task_id, title, description):
        self.task_id = task_id
        self.title = title
        self.description = description

    def __str__(self):
        return f"ID: {self.task_id}, Title: {self.title}, Description: {self.description}"

class TaskManager:
    """Class to manage tasks."""
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def create_task(self, title, description):
        task = Task(self.next_id, title, description)
        self.tasks.append(task)
        self.next_id += 1
        print("Task created successfully!")

    def read_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        print("\nList of Tasks:")
        for task in self.tasks:
            print(task)

    def update_task(self, task_id, new_title, new_description):
        for task in self.tasks:
            if task.task_id == task_id:
                task.title = new_title
                task.description = new_description
                print("Task updated successfully!")
                return
        print("Task not found!")

    def delete_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                print("Task deleted successfully!")
                return
        print("Task not found!")

def main():
    """Main function to run the console application."""
    manager = TaskManager()

    while True:
        print("\nTask Manager:")
        print("1. Create Task")
        print("2. Read Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            manager.create_task(title, description)
        elif choice == "2":
            manager.read_tasks()
        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to update: "))
                new_title = input("Enter new task title: ")
                new_description = input("Enter new task description: ")
                manager.update_task(task_id, new_title, new_description)
            except ValueError:
                print("Invalid input! Task ID must be a number.")
        elif choice == "4":
            try:
                task_id = int(input("Enter task ID to delete: "))
                manager.delete_task(task_id)
            except ValueError:
                print("Invalid input! Task ID must be a number.")
        elif choice == "5":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()

