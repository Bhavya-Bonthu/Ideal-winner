class ToDoList:
    def __init__(self):
        self.tasks = []

    def display_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty.")
        else:
            for idx, task in enumerate(self.tasks, start=1):
                status = "Completed" if task['completed'] else "Pending"
                print(f"{idx}. {task['name']} - {status}")

    def add_task(self):
        task_name = input("Enter the task name: ")
        self.tasks.append({"name": task_name, "completed": False})
        print(f"Task '{task_name}' has been added.")

    def mark_task_completed(self):
        self.display_tasks()
        if self.tasks:
            try:
                task_number = int(input("Enter the task number to mark as completed: "))
                if 1 <= task_number <= len(self.tasks):
                    self.tasks[task_number - 1]['completed'] = True
                    print(f"Task '{self.tasks[task_number - 1]['name']}' marked as completed.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    def remove_task(self):
        self.display_tasks()
        if self.tasks:
            try:
                task_number = int(input("Enter the task number to remove: "))
                if 1 <= task_number <= len(self.tasks):
                    removed_task = self.tasks.pop(task_number - 1)
                    print(f"Task '{removed_task['name']}' has been removed.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    def run(self):
        while True:
            print("\n1. Display To-Do List")
            print("2. Add a Task")
            print("3. Mark a Task as Completed")
            print("4. Remove a Task")
            print("5. Quit")

            choice = input("Enter your choice: ")
            if choice == '1':
                self.display_tasks()
            elif choice == '2':
                self.add_task()
            elif choice == '3':
                self.mark_task_completed()
            elif choice == '4':
                self.remove_task()
            elif choice == '5':
                print("Exiting the application. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    todo_list = ToDoList()
    todo_list.run()
