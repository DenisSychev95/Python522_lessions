import json


class Country:
    # Статическое свойство содержащее имя файла
    __filename = "my_countries.json"
    # Статическое свойство содержащее пустой словарь
    __countries = {}

    # Интерфейс цикла.
    @staticmethod
    def interface():
        print(
            f"{"*" * 30}\nВыбор действия:\n1 - добавление данных\n2 - удаление данных\n3 - поиск данных\n"
            f"4 - редактирование данных\n5 - просмотр данных\n6 - завершение работы")

    # Метод десериализации(считывания/распаковки) данных из файла, возвращает Country.countries(словарь страна:столица).
    @staticmethod
    def load():
        try:
            with open(Country.__filename) as fr:
                Country.countries = json.load(fr)
        except FileNotFoundError:
            pass
        return Country.countries

    # Метод сериализации(записи/упаковки) данных в файл, ничего не возвращает.
    @staticmethod
    def dump():
        with open(Country.__filename, "w") as fw:
            json.dump(Country.__countries, fw, indent=2, ensure_ascii=False)
            print("Файл сохранен")

    # Метод добавления данных: считывает данные из файла, проверяет на наличие ключа с таким именем,
    # если вводимый ключ не существует:
    # создаст элемент словаря страна: столица, запишет данные в файл.
    @staticmethod
    def update_data(country, capital):
        Country.load()
        if Country.search(country):
            print(f"У страны {country} уже есть столица! Воспользуйтесь методом редактирования данных"
                  f"(пункт №4 в интерактивном меню)")
        else:
            Country.__countries.update({country: capital})
            print(f"В данные успешно добавлен элемент:\n{{{country}: {Country.__countries[country]}}}")
            Country.dump()

    # Метод редактирования данных: считывает данные из файла, проверяет на наличие ключа с таким именем,
    # если вводимый ключ существует:
    # изменит значение(столицу) для указанного ключа(страны), запишет данные в файл.
    @staticmethod
    def edit_data(country, new_capital):
        Country.load()
        if Country.search(country):
            print(f"Для страны: {country} -имя столицы: {Country.__countries[country]} "
                  f"успешно изменено на {new_capital}.")
            Country.__countries[country] = new_capital
            Country.dump()
        else:
            print(f"Пожалуйста воспользуйтесь методом добавления данных(пункт №1 в интерактивном меню).")

    # Метод удаления данных по ключу(стране): считывает данные, удаляет значение выбранного ключа, записывает данные.
    @staticmethod
    def remove_data(country):
        Country.load()
        if Country.search(country):
            dict_to_print = {"страна": country, "столица": Country.__countries[country]}
            print(f"Элемент {dict_to_print} удален.")
            del Country.__countries[country]
            Country.dump()
        else:
            print("Невозможно произвести удаление.")

    # Метод для поиска данных, принимает страну(ключ) и выводит ее столицу(значение), если такой ключ есть в словаре.
    @staticmethod
    def search_data(country):
        if Country.search(country):
            print(f"Элемент при считывании данных из файла найден:\n"
                  f"{{страна: {country}, столица: {Country.__countries[country]}}}")

    # Метод поиска ключа, считывает данные из файла, ищет принимаемое имя ключа в словаре данных, возвращает ключ
    @staticmethod
    def search(country):
        Country.load()
        if country in Country.__countries:
            return country
        else:
            print(f"Страна: {country} в считанных из файла данных не найдена.")

    # Метод просмотра всех данных из файла, считывает и выводит данные из файла, ничего не возвращает.
    @staticmethod
    def show_data():
        print(f"Распаковка данных из файла:\n{Country.load()}")


while True:
    Country.interface()
    try:
        num = int(input("Ввод: "))
        if num == 1:
            Country.update_data(input("Введите название страны (с заглавной буквы): "),
                                input("Введите название столицы страны (с заглавной буквы): "))
        elif num == 2:
            Country.remove_data(input("Введите название удаляемой страны (с заглавной буквы): "))
        elif num == 3:
            Country.search_data(input("Для поиска столицы укажите название страны(с заглавной буквы): "))
        elif num == 4:
            Country.edit_data(input("Введите название страны (с заглавной буквы): "),
                              input("Введите новое название столицы страны (с заглавной буквы): "))
        elif num == 5:
            Country.show_data()
        elif num == 6:
            print("Завершение работы")
            break
        else:
            print("Для корректной работы программы укажите число от 1 до 6(включительно)")
    except ValueError:
        print("Некорректный тип данных для ввода")
