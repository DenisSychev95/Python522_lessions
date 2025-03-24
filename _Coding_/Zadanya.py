# Практическая работа №1
# Задание 1
# age = int(input("Введите ваш возраст: "))
# if age >= 16:
#     print("Вы можете получить водительские права")
# elif 0 < age < 16:
#     print("Вы  пока не можете получить водительские права")
# else:
#     print("Ошибка: неверно указан возраст")
from logging import exception

# Задание 2
# age = int(input("Введите ваш возраст: "))
# price_1 = "бесплатно"
# price_2 = 10
# price_3 = 20
# if 0 <= age < 5:
#     print(f"Цена билета: {price_1}")
# elif 5 <= age <= 17:
#     print(f"Цена билета: {price_2}$")
# elif 17 < age <= 120:
#     print(f"Цена билета: {price_3}$")
# else:
#     print("Ошибка: неверно указан возраст")

# Задание 3
# summa = float(input("Введите сумму покупок: "))
# age = int(input("Введите ваш возраст: "))
# discount_0 = 0
# discount_1 = 10
# discount_2 = 5
# discount_3 = discount_1 + discount_2
# if 0 < summa <= 100:
#     if 5 <= age < 65:
#         print(f"Размер скидки составляет: {discount_0}%")
#     elif 65 < age <= 120:
#         print(f"Размер скидки составляет: {discount_2}%")
#     else:
#         print("Некорректно введен возраст покупателя")
# elif 100 < summa:
#     if 5 <= age < 65:
#         print(f"Размер скидки составляет: {discount_1}%")
#     elif 65 < age <= 120:
#         print(f"Размер скидки составляет: {discount_3}%")
#     else:
#         print("Некорректно введен возраст покупателя")
# else:
#     print("Некорректно введена сумма покупок")


# Практическая работа №2
# Задание 3
# Полностью рабочий код
# c = 0
# res = 0
# while True:
#     try:
#         a = int(input("Введите количество дней:"))
#         if a >= 0:
#             break
#         print("Ошибка: количество дней не может быть отрицательным")
#     except ValueError:
#         print("Ошибка: укажите количество дней в виде числа")
# while c <= a:
#     if c == a:
#         break
#     c += 1  # можно попробовать с None?
#     while True:
#         try:
#             b = int(input("Введите количество товаров: "))
#             if b >= 0:
#                 break
#             print("Ошибка: количество товаров не может быть отрицательным")
#         except ValueError:
#             print("Ошибка: укажите количество товаров в виде числа")
#     res += b / a  # можно попробовать с None?
# print(f"Среднее количество товаров, поступивших за день: {res:.0f}")

# Задание 2
# Полностью рабочий код
# res = 0
# while True:
#     try:
#         a = int(input("Введите количество полученного товара: "))
#         if a == 0:
#             break
#         if a > 0:
#             res += a
#         else:
#             print("Ошибка: количество товаров должно быть положительным")
#     except ValueError:
#         print("Ошибка: введите количество товаров числом")
# print("Общее количество принятых товаров:", res)

# Задание 1
# Полностью рабочий код
# res = 0
# while True:
#     a = int(input("Введите число: "))
#     if a == 0:
#         break
#     if a > 0:
#         res += a
# print("Сумма всех положительных чисел:", res)

# numbers = [3, 1, 4, 1, 5]
# numbers.sort()
# print(numbers)

#  Практическая работа №3
#  Задание №1
#
# s = [input("Введите любимый фильм: ") for i in range(int(input("Укажите количество любимых фильмов: ")))]
# for i in s:
#     print(i, end="\n")

#  Задание №2
# пока не ясно
# s = []
# while True:
#     cmd_ = input("Введите команду(add, remove, stop): ")
#     if cmd_ == "add":
#         if len(s) < 20:
#             m = input("Введите  название добавляемого фильма:")
#             if m not in s:
#                 s.append(m)
#                 print(s)
#             else:
#                 print("Такой фильм уже есть в списке")
#         else:
#             print("Список переполнен, чтобы добавить фильм удалите старый")
#     elif cmd_ == "remove":
#         m = input("Введите название удаляемого фильма:")
#         try:
#             s.remove(m)
#             print(s)
#         except ValueError:
#             print("Такого фильма нет в списке")
#     elif cmd_ == "stop":
#         print(s)
#         break
#     else:
#         print("Ошибка: неизвестная команда")


#  Задание №3 # без обработки исключений, код рабочий
# sum_ = 0
# res = 1
# nums = []
# s = [int(input("Введите оценку -->")) for i in range(int(input("Введите количество оценок: ")))]
# for i in s:
#     sum_ += i
#     res = sum_ / len(s)
# nums = [i for i in s if res < i]
# print("Средняя оценка: ", res)
# print("Оценки выше средней: ", nums)

# # С обработкой исключений
# sum_ = 0
# res = 0
# s = []
# while True:
#     try:
#         count_ = int(input("Введите количество оценок: ")) # ввод оценок
#         if count_ < 0 or count_ > 100:
#             raise Exception("Некорректное число оценок")
#         else:
#             break
#     except ValueError as e:  # исключения, когда ввели строку
#         print("Нужно ввести число. А вы ввели строку: ", e)
#     except Exception as e:
#         print(e)
#
# for i in range(count_):
#     while True:
#         try:
#             value_ = int(input("Введите оценку: "))  # ввод оценок
#             if value_ < 2 or value_ > 5:
#                 raise Exception("Некорректная величина оценки")
#             else:
#                 s.append(value_)  # добавляем оценки в список
#                 break
#         except ValueError as e: # исключения, когда ввели строку
#             print("Нужно ввести число. А вы ввели: ", e)
#         except Exception as e:
#             print(e)
# for i in s:
#     sum_ += i
#     res = sum_ / len(s)
# nums = [i for i in s if res < i]
# print("Средняя оценка: ", res)
# print("Оценки выше средней: ", nums)




