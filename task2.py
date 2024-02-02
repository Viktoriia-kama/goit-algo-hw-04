# розробити функцію, яка читає файл та повертає список словників з інформацією про кожного кота
def get_cats_info(path: str) -> list:
    with open(path, "r") as file:
        all_info = file.readlines()                     # зчитуємо вміст файлу
        # перевіряємо чи файл містить якусь інформацію
        if all_info == []:
            print("Ваш файл не містить жодної інформації!")
        list = []
        for cat in all_info:
            one_cat_info = cat.split(',')               # розділяємо дані про кожного працівника по ","
            one_cat_info = tuple(one_cat_info)          # перетворюємо список на кортеж
            i, j, k = one_cat_info                      # використовуємо розпакування для присвоєння значень ключам
            k = k.rstrip("\n")                          # видаляємо зайвий символ "\n"
            dict = {"id": i,"name": j,"age": k}         # заповнюємо словник даними про кота
            list.append(dict)
    return list

while True:
    try:
        # Отримання шляху до файлу
        path = input("Введіть шлях до файлу: ")
        list = get_cats_info(path)
        print(f"Інформація про котів: {list}")
        break
    except FileNotFoundError:
        print("Файл не знайдено!")