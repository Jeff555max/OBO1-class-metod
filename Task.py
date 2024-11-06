class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_as_completed(self):
        """Отметить задачу как выполненную."""
        self.completed = True

    def __str__(self):
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"Описание: {self.description}, Срок: {self.deadline}, Статус: {status}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        """Добавить новую задачу."""
        task = Task(description, deadline)
        self.tasks.append(task)
        print(f"Задача '{description}' добавлена.\n")

    def mark_task_as_completed(self, index):
        """Отметить задачу с указанным индексом как выполненную."""
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_as_completed()
            print(f"Задача '{self.tasks[index].description}' отмечена как выполненная.\n")
        else:
            print("Некорректный индекс задачи.\n")

    def remove_task(self, index):
        """Удалить задачу с указанным индексом."""
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f"Задача '{removed_task.description}' удалена.\n")
        else:
            print("Некорректный индекс задачи.\n")

    def list_current_tasks(self):
        """Вывести список всех задач."""
        print("Список всех задач:")
        for i, task in enumerate(self.tasks):
            print(f"{i}: {task}")
        print()

def main():
    manager = TaskManager()

    while True:
        print("Выберите действие:")
        print("1: Добавить задачу")
        print("2: Отметить задачу как выполненную")
        print("3: Удалить задачу")
        print("4: Показать все задачи")
        print("5: Выход")

        choice = input("Введите номер действия: ")

        if choice == "1":
            description = input("Введите описание задачи: ")
            deadline = input("Введите срок выполнения (например, 2023-10-15): ")
            manager.add_task(description, deadline)
        elif choice == "2":
            manager.list_current_tasks()
            index = input("Введите индекс задачи, чтобы отметить как выполненную: ")
            if index.isdigit():
                manager.mark_task_as_completed(int(index))
            else:
                print("Введите правильный номер!\n")
        elif choice == "3":
            manager.list_current_tasks()
            index = input("Введите индекс задачи, чтобы удалить: ")
            if index.isdigit():
                manager.remove_task(int(index))
            else:
                print("Введите правильный номер!\n")
        elif choice == "4":
            manager.list_current_tasks()
        elif choice == "5":
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.\n")

if __name__ == "__main__":
    main()