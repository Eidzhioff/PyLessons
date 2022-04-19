import json

file = "tasks.json"

def open_tasks():
    with open(file, "r") as f:
        tasks = json.load(f)
    return tasks

def load(tasks):
    try:
        with open(file, 'w') as f:
            tasks = json.dump(tasks, f)
        print("Задачи сохранены в файл")
    except Exception as e:
        print(e)

def add(tasks):
    name = input("Сформулируйте задачу: ")
    category = input("Добавьте категорию к задаче: ")
    time = input("Добавьте время к задаче: ")
    tasks.append({'name': name, 'category': category, 'time': time})

if __name__ == "__main__":  
    tasks = open_tasks()

    print("Текущие задачи из файла: ", tasks)

    while True:
        print("""Простой todo: 
        1. Добавить задачу.
        2. Вывести список задач.
        3. Выход.""")
        print("Сверху команды")
        command = int(input("Укажите число: "))
        if command == 1:
            add(tasks)
        elif command == 2:
            for task in tasks:
                print(f"Задача: {task['name']} Категория: {task['category']} Дата: {task['time']}")
            if len(tasks) == 0:
                print("В списке нет задач.")
        elif command == 3:
            load(tasks)
            break
