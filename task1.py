# Розробити функцію total_salary(path), яка аналізує файл і повертає загальну та середню суму заробітної плати всіх розробників


def total_salary(path: str) -> tuple:
    with open(path, "r") as file:
        content = file.readlines()  # зчитуємо вміст файлу
        # перевіряємо чи файл містить якусь інформацію
        if content == []:
            print("Ваш файл не містить жодної інформації!")
        quantity_of_workers = 0
        sum_salary = 0
        # перебираємо кожного працівника
        for worker in content:
            quantity_of_workers += 1
            info = worker.split(",")  # розділяємо дані про кожного працівника по ","
            # перебираємо дані про працівника
            for i in info:
                i = i.rstrip("\n")  # видаляємо зайвий символ "\n"
                if i.isdigit():  # перевіряємо чи дані це сума з\п
                    sum_salary += int(i)  # додаємо до суми
        average_salary = int(sum_salary / quantity_of_workers)
    return sum_salary, average_salary



while True:
    try:
        # Отримання шляху до файлу
        path = input("Введіть шлях до файлу: ")
        total_salary, average_salary = total_salary(path)
        print(f"Загальна сума заробітної плати: {total_salary}, Середня заробітна плата: {average_salary}")
        break
    except FileNotFoundError:
        print("Файл не знайдено!")
