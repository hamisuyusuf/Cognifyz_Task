#!/usr/bin/env python3

import pandas as pd
import os


class TaskManager:
    """A class to manage tasks using pandas and persist them in a CSV file."""

    def __init__(self, file_name="tasks.csv"):
        self.file_name = file_name
        self.columns = ["Task", "Category", "Deadline"]
        self.tasks_df = self.load_tasks()

    def load_tasks(self):
        """Load tasks from a CSV file into a pandas DataFrame."""
        if os.path.exists(self.file_name):
            return pd.read_csv(self.file_name)
        else:
            # Create an empty DataFrame if the file doesn't exist
            return pd.DataFrame(columns=self.columns)

    def save_tasks(self):
        """Save the current DataFrame to the CSV file."""
        self.tasks_df.to_csv(self.file_name, index=False)

    def display_tasks(self):
        """Display all tasks in the DataFrame."""
        if self.tasks_df.empty:
            print("No tasks available.")
        else:
            print("\nTasks:")
            print(self.tasks_df.to_string(index=False))
        print()

    def create_task(self):
        """Create a new task to the DataFrame."""
        task = input("Enter the task description: ").strip()
        category = input("Enter the task category: ").strip()
        deadline = input("Enter the task deadline (YYYY-MM-DD): ").strip()

        # Append the new task to the DataFrame
        new_task = pd.DataFrame([[task, category, deadline]],
                                columns=self.columns)
        self.tasks_df = pd.concat([self.tasks_df, new_task],
                                  ignore_index=True)
        self.save_tasks()
        print("Task added successfully!")

    def delete_task(self):
        """Delete a task by its index in the DataFrame."""
        self.display_tasks()
        try:
            task_index = int(input("Enter the task number to delete: ")) - 1
            if 0 <= task_index < len(self.tasks_df):
                print(f"Task'{self.tasks_df.iloc[task_index]['Task']}'deleted successfully!")
                self.tasks_df = self.tasks_df.drop(
                        index=task_index).reset_index(drop=True)
                self.save_tasks()
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def update_task(self):
        """Update an existing task in the DataFrame."""
        self.display_tasks()
        try:
            task_index = int(input("Enter the task number to update: ")) - 1
            if 0 <= task_index < len(self.tasks_df):
                print(f"Updating task: {self.tasks_df.iloc[task_index]['Task']}")
                new_task = input("Enter the updated task description: ").strip()
                new_category = input("Enter the updated category: ").strip()
                new_deadline = input("Enter the updated deadline (YYYY-MM-DD): ").strip()
                
                self.tasks_df.loc[task_index, "Task"] = new_task
                self.tasks_df.loc[task_index, "Category"] = new_category
                self.tasks_df.loc[task_index, "Deadline"] = new_deadline
                
                self.save_tasks()
                print("Task updated successfully!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    """Main function to interact with the TaskManager."""
    print("Welcome to the Task Manager!")
    task_manager = TaskManager()

    while True:
        print("\nMenu:")
        print("1. Display Tasks")
        print("2. Create Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            task_manager.display_tasks()
        elif choice == "2":
            task_manager.create_task()
        elif choice == "3":
            task_manager.update_task()
        elif choice == "4":
            task_manager.delete_task()
        elif choice == "5":
            print("Exiting the Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
