import json


class Country:
    # Статическое свойство содержащее имя файла
    filename = "my_countries.json"
    # Статическое свойство содержащее словарь
    countries = {}

    # Интерфейс цикла.
    @staticmethod
    def interface():
        print(
            f"{"*" * 30}\nВыбор действия:\n1 - добавление данных\n2 - удаление данных\n3 - поиск данных\n"
            f"4 - редактирование данных\n5 - просмотр данных\n6 - завершение работы")

    # Метод десериализации(считывания/распаковки) данных из файла, возвращает Country.countries(словарь страна:столица).
    @staticmethod
    def load_from_file():
        try:
            with open(Country.filename) as fr:
                Country.countries = json.load(fr)
        except FileNotFoundError:
            pass
        return Country.countries

    # Метод сериализации(записи/упаковки) данных в файл, ничего не возвращает.
    @staticmethod
    def dump_to_file():
        with open(Country.filename, "w") as fw:
            json.dump(Country.countries, fw, indent=2, ensure_ascii=False)
            print("Файл сохранен")

    # Метод добавления данных: считывает данные из файла, проверяет на наличие ключа с таким именем,
    # если вводимый ключ не существует:
    # создаст элемент словаря страна: столица, запишет данные в файл.
    @staticmethod
    def add_data(country, capital):
        Country.load_from_file()
        if Country.search_data(country):
            print(f"У {country} уже есть столица! Воспользуйтесь методом редактирования данных"
                  f"(пункт №4 в интерактивном меню)")
        else:
            Country.countries.update({country: capital})
            printed_dict = {country: Country.countries[country]} #???
            print(f"В словарь данных успешно добавлен элемент: {printed_dict}") # ???
            Country.dump_to_file()

    # _Метод редактирования данных: считывает данные из файла, проверяет на наличие ключа с таким именем,
    # если вводимый ключ существует:
    # изменит значение(столицу) для указанного ключа(страны), запишет данные в файл.
    @staticmethod
    def change_data(country, new_capital):
        Country.load_from_file()
        if Country.search_data(country):
            print(f"Для страны: {country} -имя столицы: {Country.countries[country]} успешно изменено на {new_capital}")
            Country.countries[country] = new_capital
            Country.dump_to_file()
        else:
            print(f"{country} не найдена в словаре данных. Пожалуйста воспользуйтесь методом добавления данных"
                  f"(пункт №1 в интерактивном меню)")

    # _Метод удаления данных по ключу(стране): считывает данные, удаляет значение выбранного ключа, записывает данные._
    @staticmethod
    def remove_data(country):
        Country.load_from_file()
        if Country.search_data(country):
            dict_to_print = {"Страна": country, "Столица": Country.countries[country]}
            print(f"Элемент {dict_to_print} удален.")
            del Country.countries[country]
            Country.dump_to_file()

    @staticmethod
    def search_and_print_data(key):
        # dict_to_print = {"Страна": key, "Столица": Country.countries[key]}
        print(f"Страна: {key}; Столица: {Country.countries[key]}")

    # Метод для поиска данных, принимает страну(ключ) и выводит ее столицу(значение), если такой ключ есть в словаре.
    @staticmethod
    def search_data(country):
        Country.load_from_file()
        if country in Country.countries:
            return country
        # else:
        #     print(f"Страна: {country} в словаре данных не найдена ")

    # _Метод просмотра данных, ничего не возвращает, считывает и выводит данные из файла._
    @staticmethod
    def show_data():
        print(Country.load_from_file())


# Country.load_from_file()
# Country.dump_to_file()
# Country.add_data(input("Введите название страны (с заглавной буквы):"),
#                  input("Введите название столицы страны (с заглавной буквы):"))
# Country.add_data("Russia", "Moskow")
# Country.add_data("Great Britain", "London")
# Country.remove_data("Great Britain")
# Country.add_data("France", "Paris")
# Country.change_data(Country.search_data("France"),"Agaragudju")
# Country.search_data("Россия")
# Country.remove_data("Great Britain")
# Country.add_data("Russia", "Saint-Petersburg")
# Country.remove_data("Venesuella")
Country.add_data("France", "Paris")
Country.change_data(Country.search_data("France"),"PARK")
Country.add_data("Egypt", "Cair")
Country.search_and_print_data(Country.search_data("Egypt"))
Country.add_data("111", "222")
Country.add_data("1211", "2222")
Country.add_data("33211", "222222")
Country.add_data("33222211", "222222222")
# Country.remove_data("France")
# Country.add_data("France", "Paris")
# print(Country.search_data("Russia"))
# Country.show_data()
# Country.interface()

# while True:
#     Country.interface()
#     try:
#         num = int(input("Ввод: "))
#         if num == 1:
#             Country.add_data(input("Введите название страны (с заглавной буквы): "),
#                              input("Введите название столицы страны (с заглавной буквы): "))
#         elif num == 2:
#             Country.remove_data(input("Введите название удаляемой страны (с заглавной буквы): "))
#         elif num == 3:
#             Country.search_data(input("Для поиска столицы укажите название страны(с заглавной буквы): "))
#         elif num == 4:
#             Country.change_data(input("Введите название страны (с заглавной буквы): "),
#                                 input("Введите новое название столицы страны (с заглавной буквы): "))
#         elif num == 5:
#             Country.show_data()
#         elif num == 6:
#             print("Завершение работы")
#             break
#         else:
#             print("Для корректной работы программы укажите число от 1 до 6(включительно)")
#     except ValueError:
#         print("Некорректный тип данных для ввода")

