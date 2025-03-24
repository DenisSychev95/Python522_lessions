# Задание №1
from ipaddress import summarize_address_range
from platform import processor

# print("Выполнил задание:","\n\tСычев Денис Анатольевич", "\n\t\tслушатель группы:", "522")


# student = input("Ваше ФИО: ")
# study_group = int(input("Ваша группа: "))
# print(f"Выполнил задание: \n\t{student} \n\t\tслушатель группы {study_group}")

# Задание №2
# a = 5
# b = 7
# c = 3
# numbers = [a, b, c]
# summ = sum(numbers)
# multiplication = a * b * c
# arithmetic_mean = sum(numbers) / len(numbers)
# print(summ, multiplication, arithmetic_mean)

# Задание №3
# a = 9753
# reverse_a = int(str(a)[::- 1])
# print(reverse_a)


# 26.01.25 Воскресенье практика
# Задание №1
# name = input("Введите ваше ФИО: ")
# balance = float(input("Ведите ваш баланс: "))
# if balance >= 0:
#     print(f"Добро пожаловать, {name}. \nВаш баланс: {balance:.2f}. ")
# else:
#     print(f"Добро пожаловать, {name}. Произошла ошибка: Баланс не может быть отрицательным!")

# Задание №2
# number = int(input("Введите № вашей скидочной карты: "))
# discount = float(input("Введите размер вашей скидки: "))
# if (discount > 0 and discount <= 100):
#     print(f"Здравствуйте, № вашей скидочной карты: {number}", end="\n")
#     print(f"Ваша скидка составляет: {discount:.1f}%")
# else:
#     print(f"Здравствуйте, № вашей скидочной карты: {number}", end="\n")
#     print(f"Произошла ошибка: Некорректно введен процент скидки")
#
# # Задание №3
# study_material = input("Введите тип учебного материала (книга, видео и т.д.): ")
# price = float(input("Введите стоимость материала: "))
# category_material = input("Введите категорию материала: ")
# if price > 0:
#     print(f"Тип - {study_material}, Стоимость - {price:.2f}, Категория - {category_material} ")
# else:
#     print("Ошибка: цена не может быть меньше нуля")

# a = input("Введите первое число:")  # 5 5 a a
# b = input("Введите второе число:")  # 7 a a 5
# try:
#     a = int(a)
#     b = int(b)
# except ValueError:
#     a = str(a)
# print(a + b)

#
# i = 1
# while i <= 20:
#     if i % 2: # для нечетных
#         print(i)
#     i += 1

#  Практическая работа №3
#  Задание №1
#
# s = [input("Введите любимый фильм: ") for i in range(int(input("Укажите количество любимых фильмов: ")))]
# for i in s:
#     print(i, end="\n")

#  Задание №2


# ЗАдание на уроке
# def multiply(arg):
#     def wrap(fn):
#         def wrapper(x):
#             print("Результат:", arg * fn(x))
#         return wrapper
#     return wrap
#
#
# @multiply(3)
# def return_num(a):
#     return a
#
#
# return_num(5)

# Практическая работа 4
# Задание 1
# name = input("Введите ваше имя:")
# print(name.upper())

# Задание 2
# my_str = input("Введите символы:")
# print(my_str[::-1])

# Задание 3
# my_p = input("Введите абзац:")
# symbols = (
# "A", "a", "E", "e" "I", "i", "O", "o", "U", "u", "Y", "y", "А", "а", "Е", "е", "Ё", "ё", "И", "и", "Ы", "ы", "О", "о",
# "У", "у", "Э", "э", "Ю", "ю", "Я", "я")
# symbols1 = []
# symbols2 = []
# for i in my_p:
#     if i in symbols:
#         symbols1.append(i)
#     else:
#         symbols2.append(i)
# print("Количество гласных в абзаце:", len(symbols1))
# print("Количество согласных в абзаце:", len(symbols2))

# # Практическая работа №5. Множества
# # Задание 1
# my_str = input("Введите символы:")
# # my_set = set(my_str)
# print("Kоличество уникальных символов в строке", len(set(my_str)))

# # Задание 2
# my_lst = [(int(input("Введите числа:"))) for i in range(10)]
# lst_dupl = [i for i in my_lst if my_lst.count(i) > 1]
# print("Дубликаты:", lst_dupl if len(lst_dupl) > 0 else "Дубликатов нет")
# my_lst = [(int(input("Введите числа:"))) for i in range(10)]
# my_set = set(my_lst)
# # # len_my = (len(my_lst)-len(my_set))
# print("Дубликаты есть, их количество: " + str(len(my_lst)-len(my_set)) if len(my_lst) > len(
#     my_set) else "Дубликатов нет")

# # Задание 3
# Доделать!
# lst = ["пила", "кукареку", "мод", "липа", "дом", "пила","кукуруза"]
# print(lst)  # список
# lst_ = list(set(lst))
# lst0 = []
# my_dict = {}
# # print(lst_)  # список без дубликатов
# for i in lst_: # # исправить кусок кода
#     my_dict[i] = [] ## кусок до сюда работает не так------------------
#     for e in lst_:
#         if sorted(i) == sorted(e):
#             if e not in my_dict[i]:
#                 my_dict[i].append(e)
# # print(my_dict)  # словарь : ключ слово, значение- его анаграммы
# for key, value in my_dict.items():
#     if len(my_dict[key]) < 2:
#         continue
#     else:
#         print(f"Для {key} aнаграммы: {value}")

    #     if sorted(i) in key:
    #         continue
    # my_dict[i] = []

    # print("Для", key, "aнаграммы:", ",".join(value))


# text1 = ["Замена строки в текстовом файле;\n", "изменить строку в списке;\n", "записать список в файл;\n"]
# file_n1 = "file_start1.txt"
# with open(file_n1, "w") as fw:
#     fw.writelines(text1)
# fw.writelines(lst1)