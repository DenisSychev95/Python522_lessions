# Работа через экземпляры класса(вариативность работы с данными и именами файлов)
import json


class Country:
    def __init__(self, data=None, filename=None):
        self.data = {} if data is None else data
        self.filename = "default_file_name" if filename is None else filename

    # Метод генерации имени файла.json
    def json_name(self):
        return f"{self.filename}.json"

    # Интерфейс цикла.
    @staticmethod
    def interface():
        print(
            f"{"*" * 30}\nВыбор действия:\n1 - добавление данных\n2 - удаление данных\n3 - поиск данных\n"
            f"4 - редактирование данных\n5 - просмотр данных\n6 - завершение работы")

    # Метод десериализации(считывания/распаковки) данных из файла:
    # возвращает данные в self.data(словарь страна:столица) текущего экземпляра класса.
    def load(self):
        try:
            with open(self.json_name()) as fr:
                self.data = json.load(fr)
        except FileNotFoundError:
            pass
        return self.data

    # Метод сериализации(записи/упаковки) данных в файл:
    # ничего не возвращает, записывает данные в файл из self.data.
    def dump(self):
        with open(self.json_name(), "w") as fw:
            json.dump(self.data, fw, indent=2, ensure_ascii=False)
            print("Файл сохранен")

    # Метод добавления данных: считывает данные из файла, проверяет на наличие ключа с таким именем,
    # если вводимый ключ не существует:
    # создаст элемент словаря страна: столица, запишет данные в файл.
    def update_data(self, country, capital):
        self.load()
        if self.search(country):
            print(f"У страны {country} уже есть столица! Воспользуйтесь методом редактирования данных"
                  f"(пункт №4 в интерактивном меню)")
        else:
            self.data.update({country: capital})
            print(f"В данные успешно добавлен элемент:\n{{{country}: {self.data[country]}}}")
            self.dump()

    # Метод редактирования данных: считывает данные из файла, проверяет на наличие ключа с таким именем,
    # если вводимый ключ существует:
    # изменит значение(столицу) для указанного ключа(страны), запишет данные в файл.
    def edit_data(self, country, new_capital):
        self.load()
        if self.search(country):
            print(f"Для страны: {country} -имя столицы: {self.data[country]} "
                  f"успешно изменено на {new_capital}.")
            self.data[country] = new_capital
            self.dump()
        else:
            print(f"Пожалуйста воспользуйтесь методом добавления данных(пункт №1 в интерактивном меню).")

    # Метод удаления данных по ключу(стране): считывает данные, удаляет значение выбранного ключа, записывает данные.
    def remove_data(self, country):
        self.load()
        if self.search(country):
            dict_to_print = {"страна": country, "столица": self.data[country]}
            print(f"Элемент {dict_to_print} удален.")
            del self.data[country]
            self.dump()
        else:
            print("Невозможно произвести удаление.")

    # Метод для поиска данных, принимает страну(ключ) и выводит ее столицу(значение), если такой ключ есть в словаре.
    def search_data(self, country):
        if self.search(country):
            print(f"Элемент при считывании данных из файла найден:\n"
                  f"{{страна: {country}, столица: {self.data[country]}}}")

    # Метод поиска ключа, считывает данные из файла, ищет принимаемое имя ключа в словаре данных, возвращает ключ
    def search(self, country):
        self.load()
        if country in self.data:
            return country
        else:
            print(f"Страна: {country} в считанных из файла данных не найдена.")

    # Метод просмотра всех данных из файла, считывает и выводит данные из файла, ничего не возвращает.
    def show_data(self):
        print(f"Распаковка данных из файла:\n{self.load()}")


file_name_example = "my_file_name"
my_data = {"Минск": "Беларусь"}
c1 = Country()
print(c1.__dict__)

c2 = Country(data=my_data)
print(c2.__dict__)
c3 = Country(my_data, file_name_example)
print(c3.__dict__)


while True:
    Country.interface()
    try:
        num = int(input("Ввод: "))
        if num == 1:
            c1.update_data(input("Введите название страны (с заглавной буквы): "),
                           input("Введите название столицы страны (с заглавной буквы): "))
        elif num == 2:
            c1.remove_data(input("Введите название удаляемой страны (с заглавной буквы): "))
        elif num == 3:
            c1.search_data(input("Для поиска столицы укажите название страны(с заглавной буквы): "))
        elif num == 4:
            c1.edit_data(input("Введите название страны (с заглавной буквы): "),
                         input("Введите новое название столицы страны (с заглавной буквы): "))
        elif num == 5:
            c1.show_data()
        elif num == 6:
            print("Завершение работы")
            break
        else:
            print("Для корректной работы программы укажите число от 1 до 6(включительно)")
    except ValueError:
        print("Некорректный тип данных для ввода")
