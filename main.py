# ПЕРВОЕ ЗАНЯТИЕ
from tokenize import group
from traceback import format_exception_only
from turtledemo.nim import COLOR
from turtledemo.penrose import start

# # name = "admin"
# # print("Hello", name)
# # age = 20.2
# # print(age)
# # print(type(name))
# # print(type(age))
# #
# #
# # print(id(name))
# # print(id(age))
# a = b = c = 10
# a, b, c = 5, "Hello", 7.2
# print(a)
# print(b)
# print(c)
# # Name = "admin"
# # print(Name)


# import keyword
# print(keyword.kwlist)

# PI = 3.14
# print(PI)

# a = 5
# print(a)
# a = "Hello"
# print(a)
# a = 1.2
# print(a)
# a = 5
# b = 20
# print("a:", a)
# print("b:", b)
# c = a # 1
# a = b # 2
# b = c # 1
#
# print("a:", a)
# print("b:", b)
# print("c:", c)
# print("\tстрока "
#       "символов")
# print('\tстрока \nсимволов')

# ВТОРОЕ ЗАНЯТИЕ
# разбор домашки
# a, b = b, a # самый простой вариант

# print("Документ \"file.txt\" находится по пути: \rD:\\folder\\file.txt")

# s1 = "Hello"
# s2 = "Python"
# s3 = s1 + "," + s2 + "!\t\t" #конкатенация(для чисел оператор сложения, для строк конкатенация(сложение строк)
# print(s3)
# s4 = s3 * 3 # умножение строк на число, только на целое число
# print(s4)

# print(6 + 2)
# print(6.8 + 2.4)
# print(6 - 2)
# print(6 / 2)
# print(7 / 2)
#
# print(6 // 2)
# print(7 // 2)
# print(6 ** 2)
# print(7 % 2)

# a = 5
# b = 7
# c = 3
# summa = a + b + c # сумма
# multiple = a * b * # умножение
# arith_mean = summa / 3 # среденнее арифметическое
# # alt = [a, b, c]

# number = (6 + 4) * (5 ** 2 + 7)
# print(number)

# a = 5
# a += 3
# # a = a + 3
# print(a)
#
# a -= 3 #перезаписываем значение переменной
# print(a)
# a *= 4 # a = a * 4
# print(a)

#
# num = 4321
# print("Исходное число:", num)
# a = num % 10
# print("a:", a)
# num = num // 10
# b = num % 10
# print("b:", b)

# res = num % 10 * 1000 #1000
# num = num // 10
# res = res + num % 10 * 100 #  res += num % 10 * 100
# num = num // 10
# res = res + num % 10 * 10
# num //= 10
# res = res + num % 10
# print("Обратное число:", res)

# num1 = "2"
# num2 = 3
# # res = int(num1) + num2
# res = num1 + str(num2)
# print(res)

# print(int(3.981))
# print(type(round(3.599, )))
# print(type(round(3.599, 2)))

# num1 = "2.5"
# num2 = 10
# res = float(num1) + num2 # 2.5 + 10
# print(res)

# name = "Виктор"
# age = 20
# print("Меня зовут", name, ". мне", age, "лет")
# print("Меня зовут " + name + ". мне " + str(age) + " лет")
# print("Меня зовут ", name, ". Мне ", age, " лет", sep="", end="\n\n") # end чаще всего используют, чтобы не было
# # переноса, sep и end стоят только в конце, нет разницы между sep и end нет
# print("Hello Python")

# name = input("Введите имя:")
# print("Hello,", name)

# num = int(input("Ведите число: "))
# power = int(input("Введите степень: "))
# # num = int(num)
# # power = int(power)
# res = num ** power
# print("Число", num, "в степени", power, "равно:", res)

# a = float(input("1: "))
# b = float(input("2: "))
# c = float(input("3: "))
# d = float(input("4: "))
# summ1 = a + b
# summ2 = c + d
# res = (summ1 / summ2)
# print(round(res, 2))

# b1 = True
# b2 = False
# print(type(b1))
# print(type(b2))
#
# print(5 == 5)
# print(5 == 3)
# print(int(b1))
# print(int(b2))
# print(b1 + 5)
# print(b2 + 5)

# print(bool("Python"))
# print(bool(""))
# из строковых значение только ""-False
# из числовых значений(int) только 0- False
# # из числовых значений(float) только 0.0- False
# из None булево значение- False
# test = None
# print(type(test))
# test = 5
# print(test)

# print(2 + 5 == 3 + 4)
# print(2 + 5 != 3 + 4)
# print(8 > 5)
# print(8 > 8)
# print(8 >= 8)
# print(5 < 10)
# print(5 <= 5)
# print("hello" > "Hello")# 104>72
# print("hello" < "Hello")
# print("hello" > "hEllo")

# print(2 < 4 < 9) # True: True= True
# print(2 > 4 < 9) # False: True= False
# print(2 * 5 > 7 >= 4 + 3) # 10>7(True)>=7(True)= True
# print(3 * 3 <= 7 >= 2) #True имеет общий результат, когда все элементы True

# print(5 - 3 == 2 and 1 + 3 == 4) # 2 == 2 and 4 ==4 (True and True)=> True
# print(5 - 3 == 2 and 1 + 3 < 4) # True and False==> False
# print(5 - 3 > 2 and 1 + 3 == 4) # False and True ==> False
# print(5 - 3 > 2 and 1 + 3 < 4) # False and False==> False

# print(5 - 3 == 2 or 1 + 3 == 4) # 2 == 2 and 4 ==4 (True and True)=> True
# print(5 - 3 == 2 or 1 + 3 < 4) # True and False==> True
# print(5 - 3 > 2 or 1 + 3 == 4) # False and True ==> True
# print(5 - 3 > 2 or 1 + 3 < 4) # False and False==> False

# print(not 9 - 5) # False(4==>True(not True)==> False
# print(not 7 - 7) # True(0==> False==>not False==>True


# a = 10
# b = 10
# if a > b:
#      print(a, ">", b)
# if b > a:
#     print(b, ">", a)
# if b == a:
#     print(b, "==", a)

# cnt = 5
# if cnt < 10:
#     cnt += 1
# else: cnt -= 1
# print(cnt)

# a = 40
# b = 50
# if a > b:
#      print(a, ">", b)
# elif b == a: # else if
#      print(b, "==", a)
# else:
#     print(b, ">", a)

# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешен")
#     print("Приятного просмотра")
# else:
#     print("Доступ запрещен")

# a = int(input("Введите  первую сторону: "))
# b = int(input("Введите  вторую сторону: "))
# c = int(input("Введите  третью сторону: "))
# if a == b == c:
#     print("Треугольник равносторонний")
# elif a == b or a == c or b == c:
#     print("Треугольник равнобедренный")
# else:
#     print("Треугольник разносторонний")

# day = int(input("Введите день недели(цифрой):"))
# if 1 <= day <= 5: # if (day >= 1) and (day <= 5):
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("понедельник")
#     if day == 2:
#         print("вторник")
#     if day == 3:
#         print("среда")
#     if day == 4:
#         print("четверг")
#     if day == 5:
#         print("пятница")
# elif day == 6 or day == 7:
#     print("Выходной день - ", end="")
#     if day == 6:
#         print("суббота")
#     if day == 7:
#         print("воскресенье")
# else:
#     print("Такого дня недели не существует")

# month = int(input("Введите номер месяца: "))
# if 1 <= month <= 12:
#     print("Время года: ", end="")
#     if (1 <= month <= 2) or month == 12:
#         print("Зима")
#     if 3 <= month <= 5:
#         print("Весна")
#     if 6 <= month <= 8:
#         print("Лето")
#     if 9 <= month <= 11:
#         print("Осень")
# else:
#     print("Ошибка ввода данных")


# month = int(input("Введите номер месяца: "))
# if 1 <= month <= 12:
#     print("Время года: ", end="")
# if 1 <= month <= 2 or month == 12:
#         print("Зима")
# elif 3 <= month <= 5:
#         print("Весна")
# elif 6 <= month <= 8:
#         print("Лето")
# elif 9 <= month <= 11:
#     print("Осень")
# else:
#     print("Ошибка ввода данных")

# n = int(input("Введите количество ворон: "))
# if 0 <= n <= 9:
#     print("На ветке ", end="")
#     if n == 1:
#         print(n, "ворона")
#     if 2 <= n <= 4:
#         print(n, "вороны")
#     if 5 <= n <= 9 or n ==0:
#         print(n, "ворон")
# else:
#     print("Ошибка ввода данных")

# n = int(input("Введите количество ворон: "))
# if 0 <= n <= 9:
#     print("На ветке ", end="")
#     if n == 1:
#         print(n, "ворона")
#     elif 2 <= n <= 4:
#         print(n, "вороны")
#     else:
#         print(n, "ворон")
# else:
#     print("Ошибка ввода данных")


# match выражение:
#     case шаблон_1:
#         действие_1
#     case _:
#     действие по умолчанию

# password = "qwerty"
#
# match password:
#     case 'admin':
#         print("Администратор")
#     case 'user':
#         print("Пользователь")
#     case _:
#         print("Пароль не верен")


# day = 'понедельник'
# time = 13
#
# match day:
#     case 'понедельник' | 'вторник' | 'среда' | 'четверг' | 'пятница' if 9 <= time <= 12 or 14 <= time <= 17:
#         print("Рабочий день")
#     case 'суббота' | 'воскресенье':
#         print("Выходной день")
#     case _:
#         print("Такого дня недели не существует или не рабочее время")
# #

# Торнарное выражение

# a, b = 30, 20
# print(a if a < b else b)

# a, b = 20, 20
# print("a == b" if a == b else "a > b" if a > b else "b > a")

# a = 5
# b = 0
# print(a / b)

# try: # попытаться
#     n = int(input("Введите целое число: "))
#     print(n * 2)
# except ValueError: # указать какое конкретно исключение обрабатываем
#     print("Что-то пошло не так")


# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except ValueError:
#      print("Нельзя вводить строки")
# except ZeroDivisionError:
#     print("Нельзя делить на ноль")

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#      print("Нельзя вводить строки или Нельзя делить на ноль")
# else: # когда в блоке  try не возникло исключения, не существует без except!
#     print("Все нормально. Вы ввели числа", n, "и", m)
#
# finally: # выполняется в любом случае, как  используется для закрытия чего либо(может быть без else  и except), всегда
#     print("Конец программы")# finally только в конце
# #всегда порядок try except else finally
# # в пайтон только стандартные исключения

# n = input("Введите первое значение: ") # 2 #qqq # qqq #10
# m = input("Введите второе значение: ") # 5 #www # 2 # qqq
# try:
#     n = int(n)
#     m = int(m)
# except ValueError:
#     # pass # или ... временно отключить
#     n = str(n)
# finally:
#     print(n + m)

# Циклы!

# while условие: пока условие будет давать True
#   блок инструкций

# i = 0 #переменная счетчик
# while i < 5: # условие
#     print("i =",i)
#     i += 1 # изменение счетчика(может быть увеличение или уменьшение)
#
# итерация = один шаг цикла или одно повторяющееся действие цикла

# i = 1
# while i < 100:
#     print("i =", i)
#     i *= 10

# i = 10
# while i > 0:
#     print("i =", i)
#     i -= 1

# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print("i=", i, end=" ")
#     i += 1
#
# i = 2
# while i <= 20:
#     print("i=", i, end=" ")
#     i += 2
#
# вариант для нечетных
# i = 1
# while i <= 20:
#     if i % 2 != 0:
#         print("i=", i, end=" ")
#     i += 1
# второй вариант для нечетных
# i = 1
# while i <= 20:
#     if i % 2 == 1:
#         print("i=", i, end=" ")
#     i += 1

# i = 2
# while i <= 20:
#     if i % 2:
#         print("i=", i, end=" ")
#     i += 1


# n = int(input("Количество символов: "))
# # print("*" * n)
# i = 0
# while i < n:
#     print("*", end="")
#     i += 1
# +-+-+-
# n = int(input("Количество символов: "))
# i = 0
# while i < n:
#     if i % 2 == 0:
#         print("+", end="")
#     else:
#         print("-", end="")
#         i += 1

# n = int(input("Количество символов: "))
# while n > 0:
#     print("*", end="")
#     n -= 1


# a = int(input("Введите начало диапазона: "))
# b = int(input("Введите конец диапазона: "))
# i = a
# while i <= b:
#     print(i, end=" ")
#     i += 1

#
#
# a = int(input("Введите начало диапазона: "))
# b = int(input("Введите конец диапазона: "))
# res = 0
# while a <= b:
#     print(a, end=" ")
#     res = res + a
#     a += 1
# print("Сумма", res)


# a = int(input("Введите начало диапазона: "))
# b = int(input("Введите конец диапазона: "))
# res = 0
# while a <= b:
#     if a % 2:
#         print(a, end=" ")
#         res = res + a
#     a += 1
# print("Сумма", res)

# n = input("Введите число: ") # "5"
# while type(n) is not int:     #type(n) != int
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое")
#         n = input("Введите целое число")
#
#
# if n % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")

# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue #перенаправит на проверку условия(прерывает текущую итерацию)
#     print(i, end=" ")
#     if i == 5:
#         break # служебное слово для прерывания цикла в какой-то момент- полностью прервал ликл и вышел за пределы
#     i += 1
# print("\nЦикл завершен")
# # перед continue должен увеличиваться счетчик!

# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1

# while True: # выход из цикла при вводе отриц числа
#     n = int(input("Введите положительное число: "))
#     if n < 0:
#         break

# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:    # отрабатывает только если цикл отрабатывает полностью
#     print("Цикл окончен i= ", i)
# # while и else цельная конструкция
#
# i = 0
# while i < 10:
#     if i == 5:
#         i += 1
#         continue
#     print(i)
#     i += 1
#
# else:  # отрабатывает только если цикл отрабатывает полностью
#     print("Цикл окончен i= ", i)
# while и else цельная конструкция

# else после исключения ничего не выведет
# Вложенный цикл
# i = 1
# while i < 5: # 1
#     print("Внешний цикл i=", i)
#     j = 1
#     while j < 4: # 1, 2, 3
#         print("\tВнутренний цикл j=", j)
#         j += 1
#     i += 1
# при одной итерации внешнего цикла совершаются все итерации внутреннего цикла
# принцип двумерной таблицы

# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i * j, end="\t\t")
#         j += 1
#     print() # по умолчанию в пустом принт \n
#     i += 1

# i = 0
# while i < 3:
#     j = 0
#     while j < 6:
#         print("^", end="")
#         j += 1
#     print()
#     i += 1
# цифры i и j указывают на кол-во итераций
# переменная i- строки, j- яйчейки или столбцы

# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if j % 2 == 0:
#             print("+", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1

# Цикл For
# цикл с заданным кол-вом итераций
# fot element in collection
# print(element)
# for i in "Hello", "World":
#     print(i)
# range(start, stop, step)
# print(range(0,8,2))
# for i in range(0,8,2):
#     print(i, end=" ")
# print()
# i=0
# while i<8:
#     print(i, end=" ")
#     i+=2
# print(range(0,8,)) # по умолчанию step =1, увеличивает счетчик на 1
# for i in range(0,8,2):
#     print(i, end=" ")
# print()
# i=0
# while i<8:
#     print(i, end=" ")
#     i+=1
#
# print(range(8))  # по умолчанию step =1, увеличивает счетчик на 1, start по умолчанию = 0, если отличается - указываем
# for i in range(0, 8, 2):
#     print(i, end=" ")
# print()
# i = 0
# while i < 8:
#     print(i, end=" ")
#     i += 1
# если меняем шаг- должно быть и start указано
# print(range(10, 0, -1))  # вариант разворота
# for i in range(10, 0, -1):
#     print(i, end=" ")
# print()
# i = 0
# while i > 0:
#     print(i, end=" ")
#     i -= 1

# print(range(0, 11, -1))  # вариант разворота
# for i in range(0, 11, -1):
# #     print(i, end=" ")
# #
# # print()
# #
# # i = 0
# # while i <= 10:
# #     print(i, end=" ")
# #     i += 1
# a= 10
# a = 0
# for a in range(0, 10, 1):  # i=0 i<10 i+=1 или i=10 i>0 i-=1 # ЕСЛИ ХОТИМ ПОЛУЧИТЬ a в range указываем (.., a+1,..)
#     print(a, end=" ")
# print()
# a = 0
# while a < 10:
#     print(a, end=" ")
#     a += 1

# a = int(input("Введите целое число:"))
#
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i, end=" ")
#
# for i in range(10, 100):
#     if i % 11 == 0:
#         print(i, end=" ")
#
# for i in range(11, 100,11):
#         print(i, end=" ")
#
# for i in range(10, 100):
#     if i % 10 == i // 10:
#         print(i, end=" ")
#
# for i in range(3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print("Закончен")# отрабатывает так же как и в while
#
# Вложенные циклы for
# for i in range(3):
#     print("+++")
#     for j in range(2):
#         print("----")
# w = 12
# h = 4
# for i in range(h):
#     for j in range(w):
#         print("*", end="")
#     print()

# w = int(input("Введите ширину:"))
# h = int(input("Введите длину:"))
# for i in range(h): # range может работать только с числами
#     for j in range(w):
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# for можно записать в одну строку
# letter = [i*2 for i in "Hello"] # что будет выводится  будет в i*2, выводится список в квадр скобках
# print(letter)
#
# for i in "Hello":
#     print(i*2)
#
# num = [i for i in range(30) if i % 2 == 0] # запись в одну строку, можно скомбинировать с тернарным выражением?
# print(num)

# только for может быть в одну строку
# for i in range(30):
#     if i % 2 == 0:
#         print(i)

# nums = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
# list- список. тип данных в других языках - массив
# внутри могут находиться разные типы данных
# nums = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28] # под одним именем могут хранить больше одной переменной
# print(nums)
# print(type(nums))
# print(nums[10]) # индексация начинается с нуля, длина списка равна- последний индекс+ 1
# print(nums[-1]) # последний индекс
# print(nums[-2]) # предпоследний индекс
# print("кол-во элтов списка:", len(nums))
#
# # длина списка- последний индекс+ 1
# # последний индекс - длина списка -1
# # список- можем обратиться к элементу
# nums[1]= 256
# nums[3]+= 100
# print(nums)

# # список- изменяемый тип данных!
# s = [] # способ создания пустого списка
# print(s)
# print(type(s))
#
# t= list() # способ создания пустого списка через явное преобразование типа # функция явного преобразования типов
# print(t)
# print(type(t))
#
# t= list("Python") # способ создания пустого списка через явное преобразование типа # функция явного преобразования типов
# print(t)
# print(type(t))
#
# print(range(0,8,2))
# print(list(range(1,18,2)))
#
# # строка может преобразоваться к списку
# # range- независимая функция

# a = [1, 3, 5, 7]
# b = [11, 13, 15, 17]
# print(a+b)# сложение списков
# print(a*3) # можем умножить на целое число, но не на отрицательное!

# a = [1, 3, 5, 7]
# for i in a:
#     print(i)

# a = [0 for i in range(5)]
# print(a)  # [0, 0, 0, 0, 0]
#
# a = [i for i in range(5)]
# print(a)  # [0, 1, 2, 3, 4]
#
# a = [0 for _ in range(5)]  # если не хотим писать переменную буквой
# print(a)  # [0, 0, 0, 0, 0]

# n = 15
# a = [i**2 for i in range(2, n)]
# print(a)  # [0, 1, 2, 3, 4]

# список не является числом!
# a= [0] * int(input("Введите число эл-тов списка"))
# print(a)
# for i in range(len(a)):
#     a[i]= int(input("->"))
# print(a)


# создать  наполнение пользователем списка одной строкой
# a = [int(input("->")) for i in range(int(input("n=")))]  # сначала отрабатывает for, затем вводим каждое значение
# print(a)
#
# lst = [9, 6, 3, 5]  # работает со всеми типами задач! # потому что сначала обращаемся к индексу
# for i in range(len(lst)):  # 0 1 2 3
#     print(lst[i], end=" ")
# print()
#
# for key in lst:  # обращается  сразу к значению списка, особенность работы for для пайтон!!__
#     print(key, end=" ") # прохождение по списку как по коллекции

# 5.02.25!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# n = list(range(21, 41))
# print(n)
# count = sum_ = 0
# for i in range(len(n)):
#     if n[i] % 2 == 0:
#         count += 1
#     else:
#         sum_ += n[i]
# print("Четные= ", count)
# print("Сумма нечетных= ", sum_)

# n = list(range(21, 41))
# print(n)
# count = sum_ = 0
# for i in n:
#     if i % 2 == 0:
#         count += 1
#     else:
#         sum_ += i
# print("Четные= ", count)
# print("Сумма нечетных= ", sum_)

# a = [int(input("->")) for i in range(int(input("n=")))]
# print(a)
# for i in range(len(a)):
#     if i % 2 == 0:
#         print(i, end="")
# print()
#
# a = [int(input("->")) for i in range(int(input("n=")))]
# print(a)
# for i in range(0, len(a), 2):
#     print(i, end="")
#

# a = [int(input("->")) for i in range(int(input("n=")))]
# print(a)
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i], end="")

# a = [int(input("->")) for i in range(int(input("n=")))]
# print(a)
# for i in range(len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i], end="")

# Некорректное решение для такой задачи
# a = [int(input("->")) for i in range(int(input("n=")))]
# for i in a:
#     if i > i-1:
#         print(i, end="")
# множественное присваивание при обращении по индексу
# a = [4, 8, 5, 7, 5, 9, 1]
# print(a)
# print(a)
# a[0], a[1] = a[1], a[2]
# Срезы
# список[start:stop:step] - одно или 2 двоеточия
# a = [4, 8, 5, 7, 5, 9,]
# print(a)
# print(a[1:4])
# print(a[:])
# print(a[:5])
# print(a[5:])
# print(a[1:4:2])
# print(a[::2]) # от начала и до конца
# print(a[::-1])#развернуть индекс
# print(a[::-2])
# print(a[5:2:-1])
# print(a[-1:0:-1]) # в этом случае нулевой индекс не включается
# print(a[10:20]) # выход за пределы списка
# находить диапазон через срез
# lst = list(range(1, 8))
# print(lst)
# print(lst[::-1])
# print(lst[::2])
# print(lst[1::2])
# print(lst[:1])
# print(lst[-1:])
# print(lst[3:4])
# print(lst[3:4])
# print(lst[4:])
# print(lst[4:1:-1])
# print(lst[2:5])
# a = [4, 8, 5, 7, 5, 9,]
# print(a)
# # a[1:2] = [0,0,0,0]
# # print(a)
# # a[1:3] = [0,0,0,0]
# # print(a)
# a[1:2] = [20]
# print(a)
# # a[2] = [120] # список поддерживает вложенный список
# # print(a)
# a[10:11] = [100] # выходим за диапазон списка и срез позволяет не получить исключение
# print(a)
# print(len(a))
# # получаем индекс следующий за тем который был послeдним
# # срез к существующему списку добавляет элементы
#
# Методы списков
# print(dir(list))
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
# s = [9, 7, 8, 4, 3, 2, 1]
# print(s)
# s.append(99) # добавляет 1 эл-т в конец списка
# print(s)
# s.extend([11,12,13]) # добавл список эл-тов в конец списка
# print(s)
# # s.append([99,100]) # вложенный список
# print(s)
# s.extend("add")
# print(s)
# s.insert(0, 100) # добавляет эл-т по заданному индексу, не удаляя другие, список сдвигается вправо
# print(s)
# # Сам индекс  в insert идет первым значением, значение второе значение
# s.insert(2, 101)
# print(s)
# s.insert(-1, 99) # ПОСМОТРЕТЬ ЗАНЯТИЕ!
# print(s)

# s = []
# n= int(input("Кол-во элтов списка:"))
# for num in range(n):
#     x= int(input("Ввести число:"))
#     # s.append(x)
#     s.insert(0,x)
# print(s)

# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [2, 1, 4, 3, 7]
# c = []  # получить область пересечения списков [2,1,4,3]
# for i in a:
#     for j in b:
#         if i in c:
#             continue # избавились от повторений в наружном цикле, прервет текущую итерацию и перейдет к другой
#         if i == j:
#             c.append(i)
#             break  # прервет только выполнение вложенного цикла(для оптимизации работы программы), если не надо дублир зн
# print(c)

# вариант только для пайтон
# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [2, 1, 4, 3, 7]
# c = []
# for i in a:
#     if i in b and i not in c:
#         c.append(i)
# print(c)
#
# a = [1, 2, 3,]
# b = [11, 22, 33, 4, 2]
# c = []
# if len(b)>len(a):
#
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):
#         c.append(b[i])
#
#
# else:
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):
#         c.append(b[i])
#
# print(c)
# a = [1, 2, 3, 4, 2]
# b = [11, 22, 33, ]
# c = []
# if len(a) > len(b):
#     a, b = b, a
# for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
# for i in range(len(a), len(b)):
#         c.append(b[i])
# print(c)

# Удаление эл-тов из списка
# s= [9,8,1,4,8,5,6,3]
# print(s)
# #
# # item= 5
# # if item in s:
# #     s.remove(item) # удаляет первое вхождению элемента по значению
# # print(s)
# # last = s.pop() # удаляет последний эл-т из списка
# # print(last)
# # print(s)
# #
# try:
#     second= s.pop(10) # удаляет эл-т по заданному индексу
# except:
#     second= "такого индекса нет"
# print(second)
# print(s)
#
# # если метод может попасть в исключение, нужно знать как его отработать
#
# s.clear() # очищает список, не удаляя его сам, удаляются эл-ты списка
# print(s)

# удаление эл-тов без методов. удаление через срез
# s= [9,8,1,4,8,5,6,3]
# print(s)
#
# s[5:]= []
# print(s)
#
# #встроенная функция
# del s[2:4]
# print(s)
#
# # del s[:] # полная очистка списка
# # print(s)

# # не изменяют список
# s= [9,8,1,4,8,5,6,3]
# print(s)
# # num = s.count(8) # количество вхождений заданного эл-та, указывается только одно значение
# # print(num)
#
# ind = s.index(8,3,7) # индекс с которого ищется восемь до 7-го. Находит первый индекс!!!!!!!
# print(ind)
# # ищет первое вхождение заданного эл-та, возвращает индекс на котором нашелся эл-т, можно задать диапазон поиска

# Занятие 10.02.25!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# a = [1, 2, 3]
# # b= a
# b = a.copy()
# b.append(20)
# a.append(100)
# print("a=", a, id(a))
# print("b=", b, id(b))
# они ссылаются на одну яйчейку памяти, поэтому изменяя один, изменяется другой
# метод .copy() создает копию списка(дубликат) позволяет работать с одним списком не трогая другой, у обоих списков
# разный id

# m = [1,3,5,6,2,4,6,1,2,7]
# m.reverse() # разворачивает список, изменяет порядок расположения в списке на противоположный
# print(m)

# m = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# m.sort(reverse=True) # сортировка по убыванию
# # m.sort(reverse=False) # сортировка по умолчанию по возрастанию
# print(m)

# s = ["Виталий", "Сергей", "Александр", "Анна"]
# s.sort(key=len) #сортировка по длине каждого слова по возрастанию
# s.sort() # сортировка по умолчанию( по коду символов)
# s.sort(key=len, reverse=True) #сортировка по длине каждого слова по убыванию
# print(s)

# m = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# print(m)
# m.sort() # работает только со списком и изменяет его
# print(m)
#
# s = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# lst = sorted(s, reverse= True) # функция, которая работает со списком, не изменяет его, создает новый список не
# изменяя
# # старый
# print("lst:", lst) # можно так же добавлять ключ и reverse если хотим развернуть
# print(s)
# метод sort ничего не возвращает, работает только со списками, sorted работает с разными типами данных
# может вернуть переменную в виде нового списка

# import random  # можем импортировать модуль # импорт обязательно должен быть в начале документа!

# print(random.random()) # генерирует случайное число от 0 до 1 не включая 1
# # все импорты должны быть сверху документа
# print(random.randint(5,10)) # генерирует случайное число целое от 5 до 10 включая  5 и 10. строго 2 параметра
# print(random.randrange(5,10,2)) # генерирует случайное число  в диапазоне, не включая 10,
# # работает как range
# print(random.uniform(10.5,25.5)) # работает как randint только для float
# print(round(random.uniform(10.5,25.5), 2)) # round округлит до 2-х знаков после запятой
# city_list = ["Москва", "Воронеж", "Новосибирск", "Сочи", "Екатеринбург"]
# s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# print(random.choice(city_list)) # генерирует 1 элемент из списка
# print(random.choice(s))
# print(random.choices(city_list, k=3)) # генерирует 3 элемент из списка, т.к k=3
# print(random.choices(s, k=3)) # мы можем сохранить значение в переменную, которая будет списком
# random.shuffle(city_list) # метод случайного перемешивания элементов
# print(city_list)

# import random

# mas = [random.randint(50, 100) for i in range(5)]  # 5 итераций, сохраняется список, при каждой итерации
# # сохр случайное значение от 50 до 100 включительно
# print(mas)
# print(len(mas)) # len применимо не только для списка, возвращает длину
# print(max(mas))  # макс значение эл-та
# print(min(mas)) # мин значение эл-та
# # print(sum(mas)) # встроенная функция подсчета суммы всех эл-тов списка
# import random

# mas = [random.randint(0, 100) for i in range(10)]
# print(mas)
# max_ = max(mas)
# print(max(mas))
# mas.remove(max(mas)) # можно заменить на mas.remove(max_) # сначала удалить
# mas.insert(0, max_) # затем вставить из сохраненной переменной
# print(mas)

# import random
#
# mas = [random.randint(0, 100) for i in range(10)]
# print(mas)
# min_ = min(mas)
# print(min_)
# ind = mas.index(min_)
# print(ind)
#
# del mas[:ind] # удаляем элементы от 0 до индекса с минимальным значением
# print(mas)

# m = [
#     [1, 2, 3, 4, ], #0
#     [5, 6, 7, 8],   #1
#     [9, 10, 11, 12] #2
# ]
# print(m)
# print(len(m))
# print(m[1][2])
# print(m[2][1])

# m = [
#     [1, 2, 3, 4, ], #0
#     [5, 6, 7, 8],   #1
#     [9, 10, 11, 12] #2
# ]
# print(m)
# print("Вариант 1") # работаем с индексами
# for row in range(len(m)):
#     # print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t")
#     print()
#
# print("Вариант 2") # работаем сразу с элементами
# for row in m:
#     # print(row)
#     for x in row:
#         print(x, end="\t")
#     print()

# m = ["Hello", "World", [44, [1, 2, 3], 55, ["Python"]]]  # строка как коллекция # работаем с уровнями вложенности
# print(m)
# print(m[1][2])
# print(m[1][2])
# print(m[2][1][1])
# print(m[2][3][0][3]) # получить h

# import math # отвечает за работу математических функций
# print(math.sqrt(4))
# print(math.ceil(3.2)) # метод сеил округление вверх
# print(math.floor(3.8)) # метод флур округление вниз

# import math as m  # модуль math используется как m, сократить название модуля, задать псевдоним
# print(m.sqrt(4))
# print(m.ceil(3.2)) # метод сеил округление вверх
# print(m.floor(3.8)) # МЕТОД ФЛУР округление вниз

# from math import *  # звездочка означает, что взять все модули из math
#
# print(sqrt(4))
# print(ceil(3.2))  # метод сеил округление вверх
# print(floor(3.8))  # МЕТОД ФЛУР округление вниз


# from math import sqrt, ceil, floor  # из модуля math берется только блок указанных функций(самый предпочтительный
# # вариант для работы) так могут импортироваться любые модули
# print(sqrt(4))
# print(ceil(3.2))  # метод сеил округление вверх
# print(floor(3.8))  # МЕТОД ФЛУР округление вниз

#  import math
# print(dir(math))

# from math import pi
#
# # print(pi)
#
# radius = int(input("Введите радиус окружности:"))
# print("Длина окружности:", round(2 * radius * pi, 2))

# import time
# import locale
#
# # print(time.time())  # возвращает кол-во секунд с 1.01.1970
# # print(time.ctime())  # возвращает местное текущее  время если ничего не указано
# # print(time.ctime(739210097))
# # res = time.localtime()
# # print(res)
# # print(res.tm_year, "-", res.tm_mon, "-", res.tm_mday, sep="")
# print(time.strftime("Today is %B %d, %Y"))
# # print(time.strftime("%m/%d/%Y, %H:%M:%S"))
# # print(time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime(739210097))) # форматируем по заданному кол-ву секунд
# locale.setlocale(locale.LC_ALL, "ru")  # отдельный модуль, по умолчанию стоит локаль операционной системы
# print(time.strftime("Сегодня: %B %d, %Y"))
#
# # a = 1000000
# # print(a) # 1'000'000 1_000_000
# import time
#
# start = time.time()
# print("Запуск программы")
# time.sleep(5)
# res = time.time() - start
# print("Программа выполнилась за", res, "сек.")

# Занятие 8 от 12.02.2025

# Функции

# def hello(name, age): # аргументы которые принимаемые один или несколько
#     print("Меня зовут:", name, "Мой возраст:", age)
#
#
# hello("Irina", 28)  # функция должна отделяться от остального кода двумя пустыми строками сверху и снизу(до функции и после)
# hello("Ivan",25)  # функцию можно вызывать несколько раз
# # hello("Irina") - параметры функции
#
# # параметры идут в той же последовательности, что и аргументы!Программа не понимает, это контролируется разработчиком

# def get_sum(a, b):  # имя функции должно быть в нижнем регистре!
#     print(a + b) # название функции должно быть понятным
# # если в названии функции 2 и более слова они разделяются нижним подчеркиванием
#
#
# get_sum(2, 5)
#
#
# def get_sum(a, b):  # имя функции должно быть в нижнем регистре!
#     print(a + b) # название функции должно быть понятным
# # если в названии функции 2 и более слова они разделяются нижним подчеркиванием
#
#
# x = 2
# y = 5
# get_sum(x, y)
# get_sum("abc", "def") # конкатенация строк

# def symbol(count, a, b):
#     for i in range(count):
#         if i % 2 == 0:
#             print(a, end="")
#         else:
#             print(b, end="")
#     print()
#
#
# symbol(9, "+", "-")
# symbol(7, "X", "0")

# # функция сначала должна быть объявлена, а потом вызвана, содержит в себе какой-то блок кода\
# def get_sum(a, b):
#     print("Сумма:", end="")  # возвращается только 7
#     return a + b  # все что будет после return не работает, т.к он прерывает выполнение функции # аналог break цикла
#
#
# x = 2
# y = 5
# res = get_sum(x, y)
# print(res)
# # функция ничего не возвращает без return!
# # return возвращает значение функции в место где вызывалась функция!

# def maximum(one, two):
#     if one > two:
#         return one
#     else:
#         return two
#
#
# print(maximum(9, 5))
# print(maximum(5, 15))
#
# # return сколько угодно, но отрабатывает 1

# def maximum(one, two):
#     if one > two:
#         return one - two
#     else:
#         return one + two
#
#
# a = int(input("a="))
# b = int(input("b="))
# print(maximum(a,b))

# def cub(a):
#     return a * a * a
#
#
# for i in range(1, 11):
#     print(i, "в кубе =", cub(i))

# def change(lst):
#     end = lst.pop()
#     start_ = lst.pop(0)
#     lst.append(start_)
#     lst.insert(0, end)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(["с", "л", "о", "н"]))

# def change(lst):
#     lst[0], lst[-1] = lst[-1], lst[0]  # более короткий способ, условие: одинаковое кол-во переменных слева и справа
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(["с", "л", "о", "н"]))

# def one_big(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# # print(one_big(10, 5))
# # print(one_big(5, 10))
# a = int(input("Введите первое число:"))
# b = int(input("Введите второе число:"))
# if one_big(a, b):
#     print("Первое число больше второго")
# else:
#     print("Второе число больше второго")

# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         if "a" <= ch <= "z":
#             has_lower = True
#         if "0" <= ch <= "9":
#             has_num = True
#
#     if len(password) >= 8 and has_upper:
#         return True
#     return False
#
#
# p = input("Введите пароль: ")
# if check_password(p):
#     print("Надежный пароль")
# else:
#     print("Неадежный пароль")
# # В функции else не обязательно- строка 1362-1363

# def get_sum(a=5, b=3, c=0, d=1):  # присваиваем значения по умолчанию справа налево, не обязательно всем
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum())

# def get_sum(a=5, b=3, c=0, d=1):  # присваиваем значения по умолчанию справа налево, не обязательно всем
#     return a + b + c + d


# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, d=2, c=5))  # может пайтон
# # присвоить значение d в c   и   с в d
# print(get_sum("C", "л", d= "н", c="о"))
#
# def get_sum(a=5, b=3, c=0, d=1):  # присваиваем значения по умолчанию справа налево, не обязательно всем
#     return a + b + c + d
# def get_sum(a, b, c, d):  # присваиваем значения по умолчанию справа налево, не обязательно всем
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, d=2, c=5))  # может пайтон
# # присвоить значение d в c   и   с в d
# print(get_sum("C", "л", d= "н", c="о"))

# def set_param(count=20, symbol="-"):
#     print(symbol * count)
#
#
# set_param(10, "+")
# set_param(5, "*")
# set_param(15, "#")
# set_param(7)
# set_param()


# def display_info(name, age):
#     print("Name:", name, "\nAge:", age)
#
#
# display_info("Irina", 23)
# display_info(23, "Irina")
# display_info(age=23, name="Irina")
# # display_info("Igor",age=23, name="Irina") # выдаст ошибку, т.к не перезаписывает

# def display_info(name, age): #??????????????????????? см лекцию    # особенность пайтон. # для пояснения СМ ЛЕКЦИЮ!
#     print("Name:", name, "\nAge:", age)
#
#
# display_info("Irina", 23)
#
#
# def display_info(name, age):
#     print("Hello",name)
#
#
# display_info(23, "Irina")
# display_info("Irina", 23)

# lt1 = "Hello"
# lt2 = "Hello"
# print(lt1 == lt2, id(lt1))
# print(lt1 is lt2, id(lt2))  # ссылается ли одна и другая переменная на одну единицу памяти- да
#
# lst1 = [1, 2, 3]
# lst2 = [1, 2, 3]
# print(lst1 == lst2, id(lst1))
# print(lst1 is lst2, id(lst2)) # # ссылается ли одна и другая переменная на одну единицу памяти- нет

# lst1 = [1, 2, 3] # список изменяемый тип данных
# print(lst1, id(lst1))
# lst1.append(4)
# print(lst1, id(lst1))
# lst1.pop(1)
# print(lst1, id(lst1))

# lt1 = "Hello" # строка неизменяемый тип данных, ниже мы перезаписываем переменную в другую яйчейку данных
# print(lt1, id(lt1))
# lt1 = lt1 + "!"
# print(lt1, id(lt1))

# # числа так же неизменяемый тип данных и целые и вещественные
# a = 5
# print(a, id(a))
# a = 7
# print(a, id(a))

# lt1 = "Hello" # строка неизменяемый тип данных, ниже мы перезаписываем переменную в другую яйчейку данных
# print(lt1, id(lt1))
# lt1 = lt1[0:-1]
# print(lt1, id(lt1))
# lt1 = lt1[5:10]
# print(lt1, id(lt1))

# Кортеж(tuple)
# похож на список, но неизменяемый


# обратить внимание на область видимости переменных! Конец лекции

# Занятие №9 от 17.02.2025

# Кортеж(tuple)

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__()) #зарезервированный метод выводит размер
# print(tpl.__sizeof__())
# lst[1]= 100
# print(lst)
# # tpl[1] = 100 # кортеж нельзя изменить, но можно преобразовать в список
# print(tpl)
# # после того как кортеж создан, добавить и изменить элементы нельзя
#
# # размер кортежа всегда меньше

# a = ()
# print(a, type(a))
# b = tuple()
# print(b, type(b))
# пустой кортеж изменить не можем
# a = 1, 2, 3, 4, 5, 6, 7  #это кортеж
# print(a, type(a))
# a = 1
# print(a, type(a)) # число инт
# a = 1,
# print(a, type(a)) # кортеж
# a = (1, 2, 3, 4, 5, 6, 7) # кортеж лучше обозначать в скобках

# a = (1, 2, 3)
# print(a, type(a))
# b = tuple("Hello")
# print(b, type(b))

# b = tuple("Hello")
# print(b)
# print(b[1])
# print(b[1:3])
# # не можем присвоить новое значение и изменить

# s1 = [input("->") for i in range(5)]
# print(s1)

# s2 = tuple(input("->") for i in range(5))
# print(s2) # создание кортежа вводом с клавиатуры
#
# s3 = tuple(i for i in range(5)) # генерируем элементы кортежа
# print(s3) # создание кортежа с помощью обычного for

# from random import randint
# s4 = tuple(randint(50,100) for i in range(5))
# print(s4)
# t1 = tuple("hello")
# t2 = tuple("world")
# print(t1)
# print(t2)
# # элементы кортежа можно складывать в новую переменную!
# t3 = t1 + t2  # элементы кортежа можно складывать
# print(t3)
# print(t3*3) # элементы кортежа можно умножать на целочисленное значение. Только целые

# t1 = tuple("hello")
# t2 = tuple("world")
# t3 = t1 + t2  # элементы кортежа можно складывать
# # print(t3.count("l"))
# # print(t3.count("e"))
# print(t3.count("h"))
# print(t3.count("a"))
# print(dir(tuple)) # методы, которые не изменяют кортеж # в наследство от списка count и index

# print(t3.index("l")) # возвр индекс первого вхождения
# print(t3.index("l",4, -1))
# print(t3.index("l",4, -2)) # можно получить исключение value error
# v= "a"
# if v in t3:
#     print(t3.index(v))
# v = "a"
# if v in t3:
#     print(t3.index(v))
# else:
#     print("Такого символа нет")

# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) == 1:
#             return tpl[tpl.index(el):]
#         else:
#             first = tpl.index(el) # получаем индекс первого вхождения
#             second = tpl.index(el, first + 1) + 1
#             return tpl[first:second]
#     else:
#         return () # или return tuple()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 9, 8, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

#
# t = (10, "Python", True, [1, 2, 3], ["Hello", "world"])
# print(t, id(t))
# t[4][0] = "new"
# print(t, id(t))
# print(len(t))
# # так же можно увеличить список
# t[4].append("hi")
# print(t, id(t))


# # Распаковка кортежа
# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t  # распаковка кортежа как множественное присваивание
# # x, y, z = 1, 2, 3  # распаковка кортежа как множественное присваивание
# print(x, y, z)
# # если больше или меньше значений- будет value error
# # сколько значений, столько должно быть и переменных

# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married  # из функции возвращается кортеж
#
#
# # # user = get_user()
# # # print(user)
# # # first_name, year, married = user
#
# first_name, year, married = get_user() # В функции вернулся кортеж, на этой строке происходит распаковка кортежа
# print(first_name, year, married)

# lst = [1, 2, 3, 4, 5, 6]
# print(lst, type(lst))
# tpl = tuple(lst)
# print(tpl, type(tpl))
# lst_2 = list(tpl)
# print(lst_2, type(lst_2))

# Кортеж с вложенными элементами
#
# countries = (
#     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6)))
# )
# print(countries, end="\n\n")
# for country in countries:
#     country_name, country_population, cities = country
#     print("\nСтрана: ", country_name,", население = ", country_population, sep="")
#     for city in cities:
#         city_name, city_population = city
#         print("\tГород: ", city_name, ", население = ", city_population, sep="")


# tpl = tuple(input("Введите строку: "))
# print(tpl)
# lst = []
# for i in range(len(tpl)):
#     if tpl[i] not in lst:
#         lst.append(tpl[i])
#
# for i in range(len(lst)):
#     print("Количество", lst[i], "=", tpl.count(lst[i]))
#

# Множество(set)
# s = {"red", "yellow", "green", "green", "red"}
# print(s, type(s))
# # нет возможности обратиться к элементу по индексу
# # при каждом запуске, элементы перемешиваются рандомно
# # Неупорядоченный коллекционных типов данных, содержащий только уникальные значения
# print(len(s))

# a = ()
# print(a, type(a))
# b = {} # по пустым фигурным скобкам множество(set) создать нельзя, мы создадим dict
# print(a, type(a))
# # set создается через преобразование типов
# a = set("hello")
# print(a, type(a))

# s = [x for x in range(10)]
# print(s)

# m = {x * x for x in range(10)}
# print(m)

# lst = [1, 2, 2, 2, 2, 3, 3, 4, 4, 4, 5, 6]
# num = set(lst)
# print(lst)
# print(num)
# lst_2 = list(num)
# print(lst_2)

# lst = ["red", "yellow", "green", "green", "red"]
# num = set(lst)
# print(lst)
# print(num)
# lst_2 = list(num) # мы получим уникальные элементы, но не сохраним последовательность эл-тов списка
# print(lst_2)

# t = {"red", "yellow", "green"}
# print('red' in t)
# print('blue' in t)
# for i in t:
#     print(i)
# # Множество изменяемый тип данных

# lst = ['ab_1', 'ac_1', 'bc_1', 'bc_2']
# print([i for i in lst])
# print([i for i in lst if 'a' in i])
# print({i for i in lst if 'a' in i}) # в случайном порядке
# print(['A' + i[1:] if i[0] == 'a' else 'В' + i[1:] for i in lst]) # задействовали тернарное выражение
# # если только if- только справа, если if и else- слева
# print(['A' + i[1:] if i[0] == 'a' else 'В' + i[1:] for i in lst if i[1] == 'c'])
# print({'A' + i[1:] if i[0] == 'a' else 'В' + i[1:] for i in lst if i[1] == 'c'})
# print(tuple('A' + i[1:] if i[0] == 'a' else 'В' + i[1:] for i in lst if i[1] == 'c')) # генерация кортежа
# # только через функцию tuple- генерация кортежа

# Методы множеств
# print(dir(set))
# a = {"red", "yellow", "green"}
# print(a)
# a.add("blue") # В подтверждение изменяемости типа данных
# print(a)
# # a.remove("yellow") # может вызывать искл KeyError
# # print(a)
# # a.remove("black") # KeyError
# # print(a)
# color = "black"
# # if color in a:
# #     a.remove(color)
# # print(a)
# # a.discard("yellow")
# # print(a)
# # a.discard(color) # не выдает исключения
# # print(a)
# #
# # a.pop() #нельзя передать какое-то значение, выберет какой-то первый элемент и удалит его(случайный)
# # print(a)
#
# a.clear() # очищает множество, но само множество не удаляется
# print(a)
# print({i for i in range(1000, 1010)})  # не хранит цифры в определенном порядке
# print({i / 2 for i in range(1000, 1010)})  # когда элемент как-то изменяется получается рандомный порядок

# Занятие №10 от 19.02.25

# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# # c = a.union(b) # метод объединения множеств
# # c = a | b # тот же метод, но с другим синтаксисом
# # print(c)
# # a |= b # перезаписываем переменную a, добавляет в множество а все элементы из b
# # print(a)
# # print(b)
# # c = a & b  # амперсанд, возвращает множество- пересечение множеств
# # print(c)
# # a &= b
# # print(a)
# # c = a - b  # разность множеств
# # print(c)
# # a -= b
# # print(a)
# c = a ^ b # возвращает симметричную разность множеств
# print(c)
# a ^= b
# print(a)

# a = {0, 1, 2, 3, 4}
# b = {3, 2, 1}  # является подмножеством a
# c = a >= b # возвращается True потому что b является подмножеством a
# print(c)

# a = {0, 1, 2, 3, 4}
# b = {3, 2, 1}
# c = {6, 2}
# e = {8, 2}
# # d = b ^ c ^ a ^ e  # операции идут пошагово {0, 4, 6, 8}
# d = a.symmetric_difference(b).symmetric_difference(c).symmetric_difference(e) # {0, 4, 6, 8}
# # только по 2 элемента
# # union позволяет добавлять несколько элементов

# a = {1, 2}
# b = {3}
# c = {4, 5}
# d = {3, 2, 6}
# e = {6}
# f = {7, 8}
# j = {9, 8}
# h_ = a.union(b, c, d, e, f, j)
# print(h_)
# print("Unic elem count:", len(h_))
# print("Min elem:", min(h_))
# print("Max elem:", max(h_))

# s1 = "Hello"
# s2 = "How are you"
# s3 = set(s1) & set(s2)
# print(s3)
# for i in s3:
#     print(i, end=" ")

# s = frozenset([1, 2, 3, 4, 5, 6])  # замороженное множество, неизменяемое
# print(s)  # нужен для защиты set от изменения
# s1 = frozenset(["Hello World"])
# print(s1)
# s2 = frozenset("Hello World")
# print(s2)

# Словарь (dict)
# lst = ["one", "two"]
# d = {"first": "one", "second": "two"} # нет индексов, есть ключи и значения
# print(lst)
# print(d)
# print(lst[1])
# print(d["second"]) # обратились по ключу и получили его значение

# d = {0: "text", "one": 45, (1, 2): "Кортеж", True: [1, 2, 3, 4, 5]}
# # ключом может быть цифра, строка, кортеж(неизменяемые типы данных)
# print(d)
# # ключом не может быть список и множество, значения- ЛЮБОЙ ТИП ДАННЫХ
# # если у ключа есть ДУБЛИКАТ, значит его значение перезапишется
# # ключи должны быть уникальными
# # ключом не использовать БУЛЕВЫЕ ТИПЫ ДАННЫХ

# d = {}
# print(d)
# print(d, type(d))
#
# d1 = dict()
# print(d1)
# print(d1, type(d))

# d = {"first": "one", "second": "two"} # в таком случае можно использовать цифры и другие неизменяемые типы данных
# print(d)
# print(d, type(d))
#
# d1 = dict(first="one", second="two") # через функцию преобразования типов, пишем сначала ключ, потом его значение
# # как именованные параметры функции. Параметр функции может быть только строка!
# print(d1)
# print(d1, type(d))

# lst = [
#     ["one", 1],  # больше двух элементов положить не можем, т.к для словаря требуется 2 элемента
#     ["two", 2],
#     ["three", 3]
# ]
# print(lst)
# d = dict(lst)
# print(d)
# # может быть список в списке и кортеж в кортеже

# d = {i: i ** 2 for i in range(1, 7)}  # в виде ключа должен быть  неизменяемый тип данных, СЛОВАРЬ В ОДНУ СТРОКУ
# print(d)
# for i in d:
#     print("Key=", i, "value=", d[i])

# d = {"x1": 3, "x2": 7, "x3": 5, "x4": -1}
# res = 1
# for key in d:
#     res *= d[key]
# print(res)

# d = {"x1": 3, "x2": 7, "x3": 5, "x4": -1}
# print(d)
# del d["x2"] # удаляем значение, ключ не существует без значения, поэтому тоже удаляется(автоматически)
# print(d)

# d = dict()
# d[1] = input("->")
# d[2] = input("->")
# d[3] = input("->")
# d[3] = input("->")
# print(d)

# d = {i: input("->") for i in range(1, 5)}
# print(d)
# dislike = int(input("Какой элемент удалить:"))
# del d[dislike] # если нет ключа, мы получим ошибку
# print(d)

# goods = {
#     "1": ["Core i-3-4330", 9, 4500],
#     "2": ["Core i-5-4670K", 3, 8500],
#     "3": ["AMD FX-6300", 6, 3700],
#     "4": ["Pentium G3220", 8, 2100],
#     "5": ["Core i-5-4350", 5, 6500]
# }
# for i in goods:
#     print(i, ")", goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], "руб", sep="")
#
# while True:
#     n = input("№:")
#     if n == "0":
#         break
#     else:
#         if n in goods:
#             while True:
#                 try:
#                     count = int(input("Количество"))
#                     goods[n][1] += count
#                     break
#                 except ValueError:
#                     print("Значение некорректно, введите число")
#         else:
#             print("Такого ключа не существует")
# for i in goods:
#     print(i, ")", goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], "руб", sep="")

# Методы словарей
# print(dir(dict))
# начинаем с полезных методов
# d = {1: "one", 2: "two", 3: "three"}
# # print(d.keys()) #  ключ(только для получения ключа)
# # print(d.values()) # значение
# # print(d.items()) # ключ+ значение в виде кортежа
# # for i,j in d.items():
# #     print(i, ":", j)# распаковка кортежа в переменные
# d2 = d.copy() # делает независимую копию словаря_________
# d2[2] = "four"
# print("D=", d)
# print("D2", d2)
#
# d = {1: "one", 2: "two", 3: "three"}
# print(d)
# # d.clear() # очищает словарь не удаляя его
# item = d.pop(2)
# print(d)
# print(item)

# d = {1: "one", 2: "two", 3: "three"}
# print(d)
# # d.clear() # очищает словарь не удаляя его
# item = d.pop(4) # вызывает исключения
# print(d)
# print(item)
# d = {1: "one", 2: "two", 3: "three"}
# print(d)
# # d.clear() # очищает словарь не удаляя его
# item = d.pop(4, "Такого ключа не существует") # если элемент не существует, вернет второй элемент!!!!!!
# print(d)
# print(item)
# # встроенная защита от исключений, если мы указываем второй параметр


# Занятие 11 от 24.02.25
# методы словарей
# d = {1: "one", 2: "two", 3: "three"}
# print(d)
# item = d.popitem() # метод удаляет последний ключ-значение словаря и возвращает этот ключ-значение в виде кортежа
# print(item)

# d = {1: "one", 2: "two", 3: "three"}
# # value = d[2]
# value = d.get(6, "Такого ключа нет") # есть защита- либо возвращает значение ключа, если такого ключа нет - возвращает
# # None по умолчанию
# # или возвращает второй необязательный параметр тут необязательно указывать второй параметр
# print(value)

# d = {1: "one", 2: "two", 3: "three"}
# item = d.setdefault(4, "four") # если ключа нет- создает  такой ключ, если укажем второй параметр- добавляет знач ключа
# print(d)
# print(item)
#
# d = {1: "one", 2: "two", 3: "three"}
# item = d.setdefault(2, "four") # если ключ существует, возвращает его значение
# print(d)
# print(item)

# d = {1: "one", 2: "two", 3: "three"}
# # a = {10: "A", 20: "B", 2: "C"}
# a = [(10, "A"), (20, "B"), (2, "B")] # работает с методом update
# # c = a | d # как оператор для объединения словарей, не работает со списком с вложенными кортежами
# # print(c)
# d.update(a)  # перезаписали словарь d, метод универсальный
# print(d)

# d = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New York"}
# new_d = dict()
# # new_d["name__"] = d.pop("name") # удаляя в старом сразу присваиваем в новый
# # new_d["salary__"] = d.pop("salary")
# new_d["name__"], new_d["salary__"] = d.pop("name"), d.pop("salary") # другой способ
# print(d)
# print(new_d)

# d = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New York"} # переименовать ключ нельзя, можно удалить
# # и создать новый
# d["location"] = d.pop("city") # удаляем ключ- значение и добавляем новый
# print(d)

# master_dict = {
#     "John": {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
#     "Tom": {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
#     "Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
#     "Fiona": {"N": 3904, "S": 3645, "E": 8821, "W": 2451}
# }
# for x, y in master_dict.items():
#     print(x)
#     for i, j in y.items():
#         print("\t", i, ":", j)
# # Удобная работа с вложенными словарями

# Генераторы словарей
# d = {"один": 1, "два": 2, "три": 3, "четыре": 4}
# new_d = {value: key for key, value in d.items()} # старый словарь не меняется, меняем местами ключ-значение при
# # создании нового словаря
# print(d)
# print(new_d)
# d = {"один": 1, "два": 2, "три": 3, "четыре": 4}
# new_d = {key: value for key, value in d.items() if value <= 2} # не универсальный вариант решения
# print(new_d) # словарь не поддерживает СРЕЗЫ

# d = {i: i * 5 for i in [10, 20, 30, 40, 50]} # ключами будут элементы списка
# print(d)
#
# s = "Hello"
# d1 = {key: key*3 for key in s} # ключами будут элементы строки
# print(d1)

# d = {"один": 1, "два": 2, "три": 3, "четыре": 4}
#
# print(list(d.values()))
# print(list(d.keys()))
# print(list(d.items()))

# a = ["one", 1, 2, 3, "two", 10, 20, "three", 15, 36, 60, "four", -20]
# d = dict()
# s = None
# for i in a:
#     if type(i) is str: # лучше использовать оператор is
#         d[i] = []
#         s = i
#     else:
#         d[s].append(i)
# print(d)

# zip
# d = dict(zip([1, 2, 3, 4], ["one", "two", "three", "four"])) # словарь
# d1 = list(zip([1, 2, 3, 4], ["one", "two", "three", "four"])) # список кортежей
# d2 = list(zip([1, 2, 3, 4], ["one", "two", "three", "four"],[33,44,55])) # список кортежей, таким образом словарь
# # не получим, т.к 3 элемента
# print(d)
# print(d1)
# print(d2)
# a = [1, 2, 3, 4]
# b = ["one", "two", "three", "four"]
# d = {k: v for k, v in zip(a, b)}  # zip может ограничивать сам цикл- берет один элемент из первого один из второго
# print(d)
# a = {1, 2, 3, 4}
# b = {"one", "two", "three", "four"} # при работе с множествами порядок меняется
# d = {k: v for k, v in zip(a, b)}  # фигурные скобки указывают, что мы получаем словарь
# print(d)
# # zip работает с любыми типами данных
# a = {1, 2, 3, 4}
# b = {"one", "two", "three"} # при появлении лишних элементоа отбрасываются
# d = {k: v for k, v in zip(a, b)}  # фигурные скобки указывают, что мы получаем словарь
# print(d)

# one = {"name": "Igor", "surname": "Pavlov", "job": "Consultant"} ## не объединяем словари
# two = {"name": "Irina", "surname": "Vetrova", "job": "Manager"}
# for (k1, v1), (k2, v2) in zip(one.items(), two.items()):
#     print(k1, "->", v1)
#     print(k2, "->", v2)

# Распаковка последовательности
# s = [(1, "a"), (2, "b"), (3, "c")]
# a, b = zip(*s) # со звездочкой разделяет на несколько последовательностей
# print(a)
# print(b)
# # zip отбрасывает лишние элементы
#
# print(dir(dict)) # в словаре нет сортировки

# letters = ["b", "d", "a", "c"]
# numbers = [4, 1, 3, 1]
# d = dict(zip(letters, numbers))
# print(d)
#
# data1 = list((zip(letters, numbers))) # получили список
# print(data1)
# data1.sort()
# print(data1)
# d2 = dict(data1) # получили словарь отсортированный по ключам
# print(d2)
# data2 = list((zip(numbers, letters))) # сортировка по значениям
# data1.sort()
# d3 = {v: k for k, v in data2}
# print(d3)

# letters = ["b", "d", "a", "c"]
# numbers = [4, 1, 3, 1]
# data = sorted(zip(letters, numbers))
# print(dict(data))

# one = {"один": 1, "два": 2}
# two = {"три": 3, "четыре": 4}
# # print({**one, **two}) # получаем один словарь путем распаковки словарей # распаковка словаря
# print(one | two)
# # print(one,two)
# for k, v in {**one, **two}.items():
#     print(k, "->", v)

# colors = ["red", "green", "blue"]
# ind = 1
# for color in colors:
#     print(str(ind) + "-й цвет" + color)
#     ind += 1

# print()
# for color in enumerate(colors):
#     print(str(ind + "-й цвет" + color))

# enumerate работает по словарям

# d = {"один": 1, "два": 2, "три": 3, "четыре": 4}
# for i, (k, v) in enumerate(d.items(), 1): # нумерация в данном случае будет с единицы,  по умолчанию с нуля
#     print(i, ")", k, ": ", v, sep="")

# enumerate работает в цикле в помощь для нумерации элементов

# a = [1, 2, 3, ]
# b = [*a, 4, 5, 6] # для распаковки списка одна *, при распаковке словаря **
# print(b)

# def func(*args):
#     return args
#
#
# print(func(5))
# print(func(1, 2, 3, "abc"))
# print(func())
# звездочка дает возможность перечислить любое количество передаваемых аргументов

# def summa(*params):
#     res = 0
#     for n in params:
#         res += n
#     return res
#
#
# print(summa(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(summa(7, 8, 9))


# def to_dict(*args):
#     return {i: i for i in args}
#
#
# print(to_dict(1, 2, 3, 4))
# print(to_dict("grey", (2, 17), 3.11, -4))

# def average(*args):
#     sr = sum(args) / len(args)
#     print(sr)
#     res = []
#     for num in args:
#         if num < sr:
#             res.append(num)
#     return res
#
#
# print(average(1,2,3,4,5,6,7,8,9))
# print(average(3,6,1,9,5))

# Занятие 12 от 26.02.25
# Zip работает только с готовой коллекцией!
# Enumerate работает и при генерации словаря в одну строку!!

# def func(a, b, *args):  # В данном случае нужно передать хотя бы 2 параметрa, т.к есть 1 позиционный аргумент
#     return a, b, args
#
#
# print(func(5, 7))
# print(func(1, 2, 3, 4, 5))
#
# # сначала указывают сначала позиционные аргументы, а потом элементы со *
# # нет ограничения на количество позиционных аргументов
# # элемент со * только один

# def scores(student, *score):
#     print("Student name:", student)
#     for i in score:
#         print(i)
#
#
# scores("Igor", 100, 95, 88, 92, 99)
# scores("Ivan", 77, 32, 88)

# 2 ** будут работать со словарями!!, одна * работает с кортежем
# def func(**kwargs): # keywards arguments
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))
# print(func())
# print(func(name="Irina"))

# def info(**data):
#     for k, v in data.items():
#         print(k, ":", v)
#     print()
#
#
# info(name="Irina", surname="Vetrova", age=22)
# info(name="Igor", phone="984653", email="igor@mail.ru", age=30)

# def db(**kwargs):
#     my_dict.update(kwargs)
#
#
# my_dict = {"one": "first"}  #глобальная переменная, снаружи, видна внутри функции, можно писать до или после определ
# # функции
# db(k1=22, k2=31, k3=11, k4=91)
# db(name="Bob", age=31, weight=61, eyes_color="grey")
# print(my_dict)

# def func(a, *args, b=100, **kwargs):
#     return a, args, b, kwargs # кваргс поменять местами с аргс нельзя
#
#
# print(func(1, 2, 3, 4, 5, 6, c=55, d=66, e=77))
# # в определении функции сначала позиционные аргументы, потом с 1 * потом с двумя **
# # для параметров со значением(именованный параметр) по умолчанию в опрелении функции только после аргс и перед кваргс,
# # в ретерн и вызове функции можно указывать в любом месте
# # сначала позиционные аргументы в определении функции(их сколько угодно), далее один *args, потом сколько угодно
# # именованных параметров, потом 1 kwargs

# def func1(*args):
#     print(args[0])
#
#
# def func2(**kwargs):
#     print(kwargs["one"])
#
#
# func1(1, 2, 3, 4, 5)
# func2(one=123, two=456)

# Области видимости (scope)
# в пайтон их 4
# глобальная
# name = "Tom" # глобальная область видимости


# def hi():
#     name = "Sam" #локальная область видимости
#     surname = "Jonson" #локальная область видимости
#     print("Hello", name, surname)
#
#
# def bye():
#     print("GoodBye", name)
#
#
# hi()
# bye()
# # print(surname) - переменная, объявленная в функции является локальной и не видна за пределами функции, т.к
# # после вызова функции она больше не существует
# print(name)
# # В пределах функции приоритет локальной переменной выше

# name = "Tom" # глобальная область видимости
#
#
# def hi():
#     global name # делает переменную name из локальной глобальную, указывают сверху, вначале функции
#     name = "Sam"  # локальная область видимости
#     surname = "Jonson"  # локальная область видимости
#     print("Hello", name, surname)
#
#
# def bye():
#     print("GoodBye", name)
#
#
# print(name)
# hi()
# bye()
# print(name)
#
# # name перезаписывается только если указать global при вызове первой функции
# # если используем глобал- мы перезаписываем локальную переменную в значение глобальной ,
# # которая уже есть за пределами функции
# # в глобал можно помещать несколько переменных

# i = 5
#
#
# def func(arg=i):  # в функцию попадает 5, т.к объявлено до определения функции
#     print(arg)
#
#
# i = 6
# func()
# print(i)

# приоритет идет снутри  от локальной к builtin(4 области видимости)

# import builtins
#
# names = dir(builtins)
# for t in names:
#     print(t)

# # max = 5 ## область видимости builtin, max является зарезервированным словом
#
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(max(lst))

# def add_two(a):
#     x = 2 # 2  - переменная в области вложенной функции enclosed
#
#     def add_some():
#         x = 3  # - локальная переменная
#         print("x во внутренней функции =", x) #  4 отрабатывает эта строка
#         return a + x # 5
#
#
#     return add_some() # 3,сначала отработает вызов функции add_some,  # 6 return отрабатывает после 5-го пункта
#
#
# print(add_two(3)) #  1, отрабатывает первым, вызывает функцию add_two, 7# выводит что в пункте 6

# Вложенные функции
# снаружи во внутрь элементы видны
# def outer(who):
#     def inner():
#         print("Hello,", who)
#
#     inner()
#
#
# outer("World")

# def outer(): # объемлющая область видимости
#     a = 6
#
#     def inner(b):
#         a = 4
#         print("Сумма", a + b)
#
#     print("a=",a)
#     inner(5)
#
#
# outer()

# x = 25
#
#
# def fn():
#     global t
#     a = 30 # 35 # сделали a=35 из enclosed глобальную
#
#     def inner():
#         nonlocal a # сделали a=35 из локальной в enclosed
#         a = 35
#         print("a=", a)
#
#     inner()
#     t = a
#
#
# fn()
# c = x + t
# print(c)

# def fn1():
#     x = 25
#
#     def fn2():
#         x = 33
#
#         def fn3():
#             nonlocal x # выйти до глобальной области видимости не может, обязательно должна быть переменная
#             # в области видимости объемлющей функции, максимум может дойти до enclosed и перезаписать ее
#             x = 55
#
#         fn3()
#         print("fn2.x =", x)
#
#     fn2()
#     print("fn1.x =", x)
#
#
# fn1()

# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2  # локальные переменные после вызова функции перестали существовать, поэтому используем nonlocal
#         b = b1 + b2  # локальные переменные после вызова функции перестали существовать, поэтому используем nonlocal
#         print(a, ",", b)
#
#     inner()
#     return [a, b]
#
#
# print(outer(2, 3, -1, 4))

# # РЕШИТЬ ЗАДАЧУ ТРЕМЯ СПОСОБАМИ!!
#
# def rect_parall(a, b, c):
#     def inner(i, j):
#         return i * j
#
#     s = 2 * (inner(a, b) + inner(a, c) + inner(b, c)) # локальная переменная  для наружной функции
#     return s
#
#
# print(rect_parall(2, 4, 6))
# print(rect_parall(5, 8, 2))
# print(rect_parall(1, 6, 8))
#
# #1 нужно s сделать как глобальную переменную
# #2 переменную s использовать как нелокальную переменную

# Замыкание- когда одна функция возвращает другую функцию
# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner # возвращает вложенную функцию, но не вызывает ее
#
#
# a = outer(5)  # в этой переменной хранится функция
# print(a)
# print(a(10)) # доступ к вложенной функции
# b = outer(6) # вызываем функцию через переменные
# print(b(10))
# print(outer(5)(10)) # аналогичный способ через использование анонимных функций

# def func1():
#     a = 1
#     b = "line"
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b # неизменяемый тип данных без nonlocal не изменим!
#         c.append(4)
#         a = a + 1
#         b = b + "!"
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())

# def func(city):
#     s = 0
#
#     def inner():
#         nonlocal s
#         s += 1
#         print(city, s)
#
#     return inner
#
#
# res1 = func("Москва")
# res1()
# res1()
# res1()
# res2 = func("Сочи")
# res2()
# res2()

# Занятие 13 от 03.03.25
# Анонимные функции(без имени)
# через ключевое слово lambda записывается через одну строку

# def func(x, y):
#     res = x + y
#     return res
#
#
# print(func(1, 2))
#
# print((lambda x, y: x + y)(1, 5)) # функция в одну строку
# func1 = lambda x, y: x + y # сохранили функцию в переменную
# print(func(5, 7)) # можно вызвать функцию через переменную
# print((lambda x, y: x + y)("a", "b"))
# # лямбда выражение- функция в одну строку без больших вычислений, компактная запись

# print((lambda a, b, c: a + b + c)(10, 20, 30))
# print((lambda a, b, c=3: a + b + c)(10, 20)) # в с- значение по умолчанию
# print((lambda a, b=2, c=3: a + b + c)(10)) # в с и b - значения по умолчанию
# print((lambda a=1, b=2, c=3: a + b + c)())# все значения по умолчанию
#
# print((lambda *args: args)(1, 2, 3, 4, 5, 6, 7))
# print((lambda *args: args)(6, 7))
# print((lambda *args: sum(args))(1, 2, 3, 4, 5, 6, 7))
# print((lambda *args: sum(args))(6, 7))
# print((lambda **kwargs: kwargs.items())(name=1, age=20))
# print((lambda **kwargs: sum(kwargs.values()))(name=1, age=20))

# c = (
#     lambda x: x * 2,
#     lambda x: x * 3,
#     lambda x: x * 4,
# )
#
# for t in c:
#     print(t("abc__"))

# def outer(n):
#     def inner(x):
#         return x + n
#     return inner
#
#
# f = outer(42)
# print(f(3))
#
#
# def outer1(m):
#     return lambda x: x + m
#
#
# fm = outer1(40)
# print(fm(10))
#
#
# outer1 = lambda m: lambda x: x + m
# print(outer1(55)(5))
# a = (lambda m: lambda x: x + m)(33)
# print(a(66))
# print((lambda m: lambda x: x + m)(33)(100))
# res = (lambda m: lambda x: x + m)(33)(120)
# print(res)
# res = (lambda m: lambda x: "x>m" if x > m else "m>x")(33)(120) # какой-то один результат можно указать в return,
# # его же можно поместить в lambda
# print(res)
# res = (lambda n: lambda x: lambda y: n + x + y)(2)(4)(6)
# print(res)

# d = {"b": 10, "a": 15, "c": 4}
# print(d)
# lst= list(d.items())
# print(lst)
# # lst.sort() # сортировка по ключам
# # print(lst)
# # lst.sort(reverse=True) # сортировка по ключам в обратном порядке
# # print(lst)
# lst.sort(key=lambda i: i[1]) # сравнение происходит по первому индексу в кортеже!, lambda так же не вызываем
# print(lst)
# d2= dict(lst)
# print(d2)

# def func(i):
#     return i[1]
#
#
# d = {"b": 10, "a": 15, "c": 4}
# print(d)
# lst= list(d.items())
# print(lst)
# # lst.sort() # сортировка по ключам
# # print(lst)
# # lst.sort(reverse=True) # сортировка по ключам в обратном порядке
# # print(lst)
# lst.sort(key=func) # способ через функцию, но мы ее не вызываем!
# print(lst)
# d2= dict(lst)
# print(d2)

# players = [
#     {'name': "Антон", 'last name': 'Бирюков', 'rating': 9},
#     {'name': "Алексей", 'last name': 'Бодня', 'rating': 10},
#     {'name': "Федор", 'last name': 'Сидоров', 'rating': 4},
#     {'name': "Михаил", 'last name': 'Семенов', 'rating': 6},
# ]
# res1 = sorted(players, key=lambda item: item["last name"])
# print(res1)
# res2 = sorted(players, key=lambda item: item["rating"], reverse=True)
# print(res2)
# res3 = sorted(players, key=lambda item: item["rating"])
# print(res3)
#
# # словари нельзя отсортировать пока не укажем как это сделать

# lst = [
#     (lambda x, y: x + y),
#     (lambda x, y: x - y),
#     (lambda x, y: x * y),
#     (lambda x, y: x / y)
# ]

# lst = [
#     (lambda x, y: x + y),
#     (lambda x, y: x - y),
#     (lambda x, y: x * y),
#     (lambda x, y: x / y)
# ]
# lst = [
#     lambda x, y: x + y,
#     lambda x, y: x - y,
#     lambda x, y: x * y,
#     lambda x, y: x / y
# ]

# lst = [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y, lambda x, y: x / y]
# print(lst[0](5, 7))
# print(lst[1](5, 7))
# print(lst[2](5, 7))
# print(lst[3](5, 7))

# d = {
#     1: lambda: print("Январь"),
#     2: lambda: print("Февраль"),
#     3: lambda: print("Март"),
#     4: lambda: print("Апрель"),
#     5: lambda: print("Май"),
#     6: lambda: print("Июнь"),
#     7: lambda: print("Июль"),
#     8: lambda: print("Август"),
#     9: lambda: print("Сентябрь"),
#     10: lambda: print("Октябрь"),
#     11: lambda: print("Ноябрь"),
#     12: lambda: print("Декабрь")
# }
# d[3]()
# d[12]()

# map() # работает с разными типами данных, поэтому нужно указать тип данных на выходе

# def mult(t):
#     return t * 2
#
#
# lst = [2, 8, 12, -5, -10]
# print(list(map(mult, lst)))  # к каждому элементу списка вызывается функция mult
# # map возвращает итерируемую последовательность
# # первым параметром map принимает функцию, он ее возвращает
# print(list(map(lambda t: t * 2, lst)))
# print(list(map(lambda t: t * 2, [2, 8, 12, -5, -10])))
# # map это цикл который требует тип, какой хотим получить на выходе, первым параметром
# # принимает функцию, вторым итерируемый объект
# lst1 = [2, 8, 12, -5, -10]
# lst2 = [12, 18, 112, -15, -100]
# print(list(map(lambda x, y: (x, y), lst1, lst2)))
# print(dict(map(lambda x, y: (x, y), lst1, lst2))) #(x, y) - возвращает 1 элемент кортеж
# print(dict(map(lambda x, y: [x, y], lst1, lst2))) #[x, y] - возвращает 1 элемент список

# t = (2.88, -1.78, 100.55)
# print(tuple(map(lambda x: int(x), t)))
# # map работает с любой функцией в т.ч с готовой встроенной
# print(tuple(map(int, t))) # функция int применяется к каждому элементу кортежа

# areas = [3.5464564554, 5.435345435439543, 4.34232312332103, 9.98728127, 32.0821312380123]
# print(list(map(round, areas)))
# print(list(map(round, areas, range(1,7)))) # при первой итерации добавляем 1 цифру после точки и так далее
# print(list(map(round, areas, range(1,3)))) # ограничивает итерации
# print(list(map(round, areas, range(1,10)))) # может быть больше значений
# # map позволяет добавить 3-й параметр, потому что round может иметь второй параметр

# l1 = [1, 2, 3, 7] # если есть лишний элемент, он отбрасывается, не получим исключения, но потеряем данные
# l2 = [4, 5, 6]
# print(list(map(lambda x, y: x + y, l1, l2)))

# # filter()- не изменяет элементы, но возвращает по условию
# t = ("abcd", "qwe", "zxcvc", "def", "hjk")
# print(tuple(filter(lambda s: len(s) == 3, t))) # отфильтровал из исходного кортежа только элементы с длиной- 3
# # выводит в t только True, а далее добавляет элемент в новый кортеж
# # filter используется для сравнения, в результате функции получаем объект содержащий элементы-True по условию
# # в filter должен быть оператор сравнения

# lst = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# print(list(filter(lambda s: s > 75, lst))) # Условие задается без if
#
# от 1 до 40
# from random import randint
# lst = [randint(0, 40) for i in range(10)]
# print(lst)
# print(list(filter(lambda s: s in range(10, 21), lst)))

# lst = [45, 55, 60, 37, 100, 105, 220]
# print(list(filter(lambda x: x % 15 == 0, lst)))
# # print(list(filter(lambda x: not x % 15, lst)))
# print(list(filter(lambda x: x % 2, range(10))))
# print(list(map(lambda x: x**2, filter(lambda x: x % 2, range(10))))) # более сложный вариант вариант для понимания
# print([x**2 for x in range(10) if x % 2]) # более простой и понятный вариант

# Декораторы основаны на замыкании

# def hello():
#     return "Hello, i am func 'hello'"
# def super_func(func):
#     print("Hello, i am func 'super_func'")
#     print(func())
#
# super_func(hello) # в функцию передаем другую функцию в виде аргумента
# # в пайтон близко имя переменной и имя функции
# # функции согут передаваться в другие в качестве аргумента
#
# def hello():
#     return "Hello, i am func 'hello'"
# def super_func(func):
#     print("Hello, i am func 'super_func'")
#     print(func())
#
#
# text = hello
# print(text())

# def my_decor(func):
#     def inner():
#         print("До кода")
#         func()
#         print("После кода")
#
#     return inner
#
#
# def func_test():
#     print("Hi i am 'func_test'")
#
#
# test = my_decor(func_test)
# test()

# def my_decor(func):
#     def inner():
#         print("До кода")
#         func()
#         print("После кода")
#
#     return inner
#
#
# @my_decor # декоратор- дополнительный функционал
# def func_test():
#     print("Hi i am 'func_test'")
#
#
# func_test()

# def my_decor(func): # декорирующая функция
#     def inner():
#         print("-"*30)
#         func()
#         print("*"*30)
#
#     return inner
#
# @my_decor #декоратор
# def func_test(): #декорируемая функция
#     print("Hi i am 'func_test'")
#
# @my_decor #декоратор
# def test(): #декорируемая функция
#     print("I am 'test'")
#
#
# func_test()
# test()
# # test = my_decor(func_test)
# # test()

# def my_decor(a):
#     def inner():
#         print("До кода")
#         a()
#         print("После кода")
#
#     return inner
#
#
# def func_test():
#     print("Hi i am 'func_test'")
#
#
# test = my_decor(func_test)
# test()
# Занятие 14 от 05.03.25
#
# def circle(fn):
#     def wrap():
#         return '(' + fn() + ')'
#
#     return wrap
#
#
# def angle(fn):
#     def wrap():
#         return '<' + fn() + '>'
#
#     return wrap
#
#
# @angle
# @circle
# def expression():
#     return '5 + 2'
#
#
# print(expression())
# # можно применять несколько декораторов, очередность имеет разницу, чем ближе декоратор к функции, значит
# # ближе тобразится ближе к функции(окружать функцию)
# def cnt(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count += 1
#         fn()
#         print('Вызов функции:', count)
#
#     return wrap
#
#
# @cnt
# def hello():
#     print('hello')
#
#
# hello()

# def outer(fn):
#     def inner(arg1, arg2): # вложенная функция- место принятия параметров декорируемой функции
#         print('Данные', arg1, arg2)
#         fn(arg1, arg2) # вызываем тем же кол-вом параметров
#
#     return inner
#
#
# @outer
# def pr_f_name(f, l):
#     print('Меня зовут', f, l)
#
#
# pr_f_name('Irina', 'Vetrova')
#  # во вложенную функцию приходят аргументы по количеству параметров декорируемой функции

# def outer(fn):
#     def inner(*args, **kwargs):  # вложенная функция- место принятия параметров декорируемой функции
#         print('args:', args)
#         print('kwargs:', kwargs)
#         fn(*args, **kwargs)  # вызываем тем же кол-вом параметров
#
#     return inner
#
#
# @outer
# def pr_data(a, b, c, study='Python'):
#     print(a, b, c, 'learn', study, end='\n\n')
#
#
# pr_data('Боря', 'Лиза', 'Света', study='Java')
# pr_data('Вова', 'Лиза', 'Женя')
# # во вложенную функцию приходят аргументы по количеству параметров декорируемой функции
# # аргументы вложенной функции декорирующей функции   берутся из вызова  декорируемой функции
# # один и тот же декоратор можно применять к разным функциям
# # как правило исп *args, **kwargs вместе
# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, '=', end=' ')
#             fn(x, y)
#
#         return wrap
#
#     return args_dec
#
#
# @decor("Сумма", '+')
# def summa(a, b):
#     print(a + b)
#
#
# summa(5, 2)
#
#
# @decor("Разность", "-")
# def sub(a, b):
#     print(a - b)
#
#
# sub(5, 2)
#
# # максимальный синтаксис декоратора из трех функций фложенных друг в друга, для декоратора обязательно надо передать
# #параметры
# def decor(arg):
#     def sub_decor(fn):
#         def inner(*args, **kwargs):
#             return arg * fn(*args, **kwargs)
#
#         return inner
#     return sub_decor
#
#
# @decor(3)
# def return_num(num):
#     return num
#
#
# print(return_num(5))

# функция должна возвращать результат!

# def decor(arg):
#     def sub_decor(fn):
#         def inner(*args, **kwargs):
#             print(args) # звездочку указываем только когда принимаем аргументы  и когда вызываем функц, в остальном виде без звездочек
#             return arg * fn(*args, **kwargs)
#
#         return inner
#
#     return sub_decor
#
#
# @decor(3)
# def return_num(num):
#     return num
#
#
# print(return_num(5,2,3))
# def typed(*args, **kwargs):
#     def wrapper(fn):
#         def wrap(*f_args, **f_kwargs):
#             for i in range(len(args)):
#                 if type(f_args[i]) is not args[i]:
#                     # return "Неверный тип данных"
#                     raise TypeError('Неверный тип данных')# генерирует исключение # явное пояснение почему прога прекратилась
#             for k in kwargs:
#                 if type(kwargs[k]) is not kwargs[k]:
#                     raise TypeError('Неверный тип данных')
#             return fn(*f_args, **f_kwargs)
#
#         return wrap
#
#     return wrapper
#
#
# @typed(int, int, int, )
# def typed_fn(x, y, z):
#     return x * y * z
#
#
# @typed(str, str, str)
# def typed_fn2(x, y, z):
#     return x + y + z
#
#
# @typed(str, str, z=int)
# def typed_fn3(x, y, z):
#     return (x + y) * z
#
#
# print(typed_fn(3, 4, 5))
# # print(typed_fn(3, 4, "Hi"))
# print(typed_fn(3, 4, 8))
# print(typed_fn2('Hi', 'world', '!'))
# print(typed_fn(3, 4, 8))
# print(typed_fn3('Hello', 'world', z=5))
# print(typed_fn3('Hello', 'world', z='!'))
# # звездочки указать там где указываем параметры или при вызове функции

# Строки
# print(2)
# print(bin(18)) # привели  число 18 к двоичной системе счисления
# # 0b- префикс двоичной системы счисления
# print(oct(18)) # привели  число 18 к восьмеричной  системе счисления
# # 0о- префикс восьмеричной  системы счисления
# print(hex(18)) # привели  число 18 к шестнадцатеричной системе счисления
# # 0x- префикс шестнадцатеричной  системы счисления
# print(0b10010)
# print(0o22)
# print(0x12)
# print(0b10010 + 0o22 + 0x12 + 6) # можем работать с числами в любой системе счислений, на выходе десятичная по умолчанию
# #буквы префикса лучше использовать нижнего регистра
# q = 'Pyt'
# w = 'hon'
# e = q + w
# print(e)
# # print(e * 3)
# # print(e * -3)
# # print('a'in e)
# # print('t'in e)
# # print(e[1])
# # строка неизменяемый тип данных
# print(e[1:3])
# print(e[::-1]) # развернули строку
# def change_str(s, old, new):
#     s2 = ""
#     i = 0
#     while i < len(s):
#         if s[i] == old:
#             s2 += new
#         else:
#             s2 += s[i]
#         i += 1
#     return s2
#
#
# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования"
# str2 = change_str(str1, "N", "P")
# print(str1)
# print(str2)

# префиксы у строк
# print(u"Привет")
# print("Привет")
# print("C:\\file.txt")
# print(r"C:\file.txt") # префикс r- сырые строки- подавляет экранирование, любые спецсимволы используются как обычные
# упал стакан с водой

# print("\U0001206C")

# Занятие 15 от 10.03.25

# print(b"1ab2c3") # - для отображения байтовых строк, префикс b
# префикс f

# name = "Дмитрий"
# age = 25
# print(f"Меня зовут {name}. Мне {age} лет.")
# # В f строку переменные с любыми типами данных

# x = 10
# y = 5
# print(f"{x=},{y=}")  # отформатированный вид
# print(f"{x =},{y:}")  # только оператор равенства отображает имя переменной, пробельный символ не рекомендуется
# print("x=", x, ", y=", y, sep="")
# # вычисления в f-строке
# print(f"{round(10/7, 2)}")
# print(f"{10/7:.3f}") # работает по типу round
# # все что можно сделать с переменной работает внутри фигурных скобок
# num = 74
# print(f"{num}")
# print(f"{{num}}")
# print(f"{{{num}}}")
# print(f"{{{{{num}}}}}")

# fr- чаще при работе с путями
# dir_name = "folder"
# file_name = "file.txt"
# print(fr"home\{dir_name}\{file_name}") #
# print("home\\" + dir_name + "\\" + file_name)
#
# #br - сырые строки байтовые
# s = """Многострочный
# текст """
# print(s)
# st = ("Многострочный "
#       "текст")
# print(st)
# s1 = '''Многострочный
# текст'''
# print(s1)
# тройные кавычки- не комментарий

# def square(n):
#     """"Принимает число n, возвращает квадрат числа n"""  # документирование строки именно первой строкой!
#     return n ** 2
#
#
# print(square(5))
# # print(square.__doc__) #- вызов документации функции
# # print(sum.__doc__)
# # print(min.__doc__)
# print(len.__doc__)

# написать развернутую документацию для функции, лучше использовать тройные двойные кавычки!
# from math import pi
#
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания.
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     return 2 * pi * r * (r + h)
#
#
# print(cylinder(2, 4))
# print(cylinder.__doc__)

# print(ord("a")) ##- смотрим символы в значении юникода
# print(ord("а"))
# print(ord("б"))

# while True:
#     n = input("->")
#     if n != "-1":
#         print(ord(n))
#     else:
#         break
#
# # Ё- до букв русского алфавита в верхнем регистре и ё-после букв русского алфавита в нижнем регистре

# st = "Test string for me "
# arr = [ord(x) for x in st]
# arr1 = [int(sum(arr)/len(arr))] + arr
# print("ASCI коды", arr)
# print("Среднее арифметическое", arr1)
# arr1 += [ord(x) for x in input("->")[:3] if ord(x) not in arr1]
# print(arr1)
# print(st.count(st[-1])-1)
# arr1.sort(reverse=True)
# print(arr1)

# print(chr(97))
# print(chr(35))
# print(chr(8364))

# a = 122
# b = 97
# if a > b:
#     for i in range(b, a+1):
#         print(chr(i), end=" ")
# else:
#     for i in range(a, b + 1):
#         print(chr(i), end=" ")

# print("apple" == "Apple")
# print("apple" > "Apple")
# print(ord("a"))
# print(ord("A"))

# from random import randint
#
# short = 8
# long = 16
# min_ascii = 33
# max_ascii = 126
#
#
# def random_password():
#     rand_len = randint(short,long)
#     result = ""
#     for i in range(rand_len):
#         result += chr(randint(min_ascii, max_ascii))
#     return result
#
#
# print("Случайный пароль:", random_password())

# print(dir(str))
# s = "hello, WORLD! I am learning Python."
# # print(s.capitalize()) # первая буква в верхнем, остальные в нижнем регистре
# # print(s.lower())  # например перевести все символы логина в нижний регистр, исп чаще всего
# # print(s.upper())  # переводит все символы в верхний регистр
# #
# # print(s.swapcase()) # инвертирование регистра символов
# # print(s.title()) #- переводит первую букву каждого слова в верхний регистр
# # print(s.count("h"))
# # print(s.count("i"))
# # print(s.lower().count("i")) # операции идут слева направо, в этом случае методы вып по цепочке
# # print(s.count("h", 1, -4)) # подсчитывает кол-во вхождений подстроки в строку(символов)
# print(s.find("Python")) # возвращает первый индекс вхождения подстроки в строку
# print(s.find("h",1)) # можно указать start и stop
# print(s.find("h",1,4)) # если вхождение не найдено- возвращает -1!
# print(s.index("Python")) # возвращает первый индекс вхождения подстроки в строку
# # # print(s.index("h",1,4)) # если вхождение подстроки не найдено- вернет ValueError!

# st = "один два"
# one = st[:st.find(" ")]
# two = st[st.find(" ")+1:]
# print(one)
# print(two)
# print(two + " " + one)

# s = "hello, WORLD! I am learning Python."
# print(s.find("h")) # так же возвращает -1 если элемент не найден,
# print(s.rfind("h")) # поиск с правой стороны так же возвращает -1 если элемент не найден,
# print(s.rindex("h")) # возвращает последний индекс подстроки, его элемента нет- ValueError

# st = "I am learning Python. hello, WORLD!"
# print(st[:st.find("h")] + st[st.rfind("h")+1:])

# s = "hello, WORLD! I am learning Python."
# print(s.startswith("he")) # возвращает True, если строка началась с заданой подстроки
# print(s.startswith("he",14))
# print(s.find("I am"))
# print(s.endswith("Python")) # возвр True если строка заканчивается подстрокой
# # можно определить чем началась и закончилась строка

# print("abc123".isalnum()) # определяет состоит ли строка из букв и цифр, возвр булево значение
# print("abc%123".isalnum()) # если попал спецсимвол- false
# print("".isalnum()) #  false
# print("a".isalnum()) #  true
# print("3".isalnum()) #  true
# print("AvbRq".isalpha()) # проверяет на наличие букв, регистр не важен
# print("12343".isdigit()) # проверяет на наличие цифр, если только цифры- true

# print("abc".islower()) # определяет состоит ли строка из букв в нижнем регистре, остальные символы игнорируются
# print("Abc".islower())
# print("abc122133".islower())
# print("#@#$abc122133".islower())
# print("#@#$122133".islower())
#
# print("ADC".isupper()) # определяет состоит ли строка из букв в верхнем регистре, ост символы игнорируются
# print("py".center(10)) # метод выравнивания строки по центру
# print("py".center(10,"-"))
# print("py".center(1))

# print("    py".lstrip()) # удалит пробелы слева
# print("    py     ".rstrip()) # Удалит пробелы справа
# print("    py     ".strip()) # удалит пробелы и слева и справа
#
# print("https://www.python.org".lstrip("https:/"))
# print("https://www.python.org".rstrip("org."))
# print("https://www.python.org".strip("https:/org."))
# print("https://www.python.org".lstrip("https:/").rstrip("org."))

# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования"
# print(str1.replace("N", "P")) # ищем старое значение и меняем на новое
# print(str1.replace("Nython", "Python")) # поиск и замена
# print(str1.replace("Nython", "Python",2)) # указали количество замен

# # join - собирает коллекцию в строку
# st = "-"  # символ объединитель
# seq = ("a", "b", "c")
# print(st.join(seq))
#
# print("..".join(["1","99"]))
# # # print("..".join([1,99])) работает только со строками
# print(":".join("abc"))
# print(":".join("a"))

# метод разделения строки по разделителю
# print("Строка разделенная пробелами".split()) # преобразует строку в список по символу разделителю
# print("www.python.org.ru".split(".")) # символ разделитель не попадает в список, переводит именно в список!
# print("www.python.org.ru".split(".",2))
# print("www.python.org.ru".rsplit("."))
# print("www.python.org.ru".rsplit(".",2))

# # st ="Никонов Валерий Анатольевич"
# st = input("Введите ФИО: ").split()
# # st = st.split()
# print(f"{st[0]} {st[1][0]} {st[2][0]}")
# num = input("Введите числа через пробел: ").split()
# print(num)
# num = list(map(int, num))
# print(num)
# print(sum(num))

# Занятие 16 от 12.03.25

# Регулярные выражения regular expression

# import re

# s = "Я ищу совпадения в 2025 году. И я их найду в 2 счёта."
# reg = r"\." # r-строка часто используется в шаблонах

# print(re.findall(reg, s))  # возвратит список содержащий все совпадения
# print(re.search(reg, s))  # показал местоположение первого совпадения объекта
# print(re.search(reg, s).span())
# print(re.search(reg, s).start())
# print(re.search(reg, s).end())
# print(re.search(reg, s).group())
# print(re.match(reg, s)) # поиск совпадения только сначала строки
# print(re.split(reg, s)) # возвращает список в котором строка разбита по заданному шаблону
# # шаблон в разделителе может содержать несколько символов
# print(re.sub(reg, "!", s)) # поиск и замена
# print(dir(re))

# s = "Я ищу совпадения в 2025 году. И я их найду в 2 счёта. 6789. [Hel-lo]_World"
# # reg = r"[0-9]" # диапазон от 0 до 9, так используется чаще всего
# # reg = r"[12][0-9][0-9][0-9]" # одни квадратные скобки- один символ
# # reg = r"[А-Яа-яЁё]"
# # reg = r"[А-яЁё]" # работает только с русскими буквами
# # reg = r"[A-Za-z\[\]]" # в квадратных скобках отменяются спецсимволы
# reg = r"[^0-9]" # поиск всего кроме цифр
# print(re.findall(reg, s))
# # дефис ставится в квадратных скобках либо в самом начале, но чаще в конце квадратных скобок, в квадратных скобках
# # ищется один символ

# st = "Час в 24-ти часовом формате от 00 до 23. 2021-06-15T21:45. Минуты в диапазоне от 00 до 59. 2021-06-15T01:09."
# reg = "[0-2][0-9]:[0-5][0-9]"
# print(re.findall(reg, st))
# точка- один абсолютно любой символ
# s = "Я ищу совпадения в 2025 году. И я их найду в 2 счёта. 6789. [Hel-lo]_World 200000"
# reg = r"[0-9]..."
# reg = r"\d"  # одна любая цифра в диапазоне от 0 до 9
# reg = r"\D"  # отрицание- все кроме цифр
# reg = r"\s"  # поиск пробельного символа
# reg = r"\S"  # все кроме пробельного символа
# reg = r"\w" # ищутся буквы, цифры, символ _
# reg = r"\W" # Все кроме верхн строка
# reg = r"\AЯ ищу" # ищет символы в начале строки
# reg = r"\ZWorld" # # ищет символы в конце строки
# reg = r"сов\B"
# reg = r"\bсов"
# reg = r"\w+"
# reg = r"\d+"
# reg = r"20*" # в данном случае звездочка относится к нулю # двойка должна быть, ноль может быть, может не быть
# print(re.findall(reg, s))

# Количество повторений
# + от 1 до бесконечности
# * от 1 до бесконечности
# ? от 0 до 1 повторения

# d = "05-03-1987 # Дата рождения"
#
# print("Дата рождения:", re.sub(r"\s\s#.+", "", d))  # в шаблонах пробелов быть не должно
# print("Дата рождения:", re.sub(r"-", ".", d))  # в шаблонах пробелов быть не должно
# print("Дата рождения:", re.sub(r"\s\s#.+", "", re.sub(r"-", ".", d)))
# # отрабатывает сначала вложенный, потом внешний метод

# st = "autor=Пушкин А.С.; title  = Евгений Онегин; price =200; year= 1831"
# # reg = r"\w+\s*=\s*\w+\s*\w+\.?\w?\.?" # звездочка преимущественно работает с пробелами
# # reg = r"\w+\s*=[\w\s.]*"
# reg = r"\w+\s*=[^;]+"
# print(re.findall(reg, st))
# reg1 = r";\s"
# print(re.split(reg1,st))

# st = "12 сентября 2025 года"
# # reg = r"\d{4}"
# # reg = r"\d{2,4}" # диапазон в шаблон просто так пробел не ставим
# # reg = r"\d{,4}" # ищется от 0 до 4 включительно
# # reg = r"\d{1,4}" # ищется от 1 до 4 включительно
# reg = r"\d{4,}" # ищется от 4 до бесконечности
# print(re.findall(reg, st))

# st = "+7 499 456 45 78, +74994564578, +7(499) 456 45 78, 74994564578"
# reg = r"\+?7\d{10}"
# print(re.findall(reg,st))
# s = "Я ищу совпадения в 2025 году. И я их найду в 2 счёта. 6789. [Hel-lo]_World 200000"
# # reg = r"^\w+\s\w+" # ищется совпадение только от начала строки
# reg = r"\w+\s\w+$" # ищется совпадение только в конце строки
# print(re.findall(reg, s))


# def validate_login(login):
#     return re.findall(r"^[A-Za-z0-9_-]{3,16}$", login)
#
#
# print(validate_login("Python_master"))
# print(validate_login("Dangeon_master"))
# print(validate_login("!!!!Pyt???"))
# print(validate_login("Pyth0345345943on"))

# text = "<body>Пример жадного соответствия регулярных выражений</body>"
# print(re.findall("<.*?>", text))
# # *? +? ??
# #{m,n}? {,n}? {m,}?

# st= "Петр, Ольга, Наталья и Виталий отлично учатся "
# reg= r"Петр|Ольга|Наталья|Виталий"
# print(re.findall(reg,st))
# import re
# st = "int = 4, float = 4.0f, double = 8.0"
# # reg = r"\w+\s*=\s*\d[.\w+]*"
# # reg = r"int\s*=\s*\d[.\w+]*|float\s*=\s*\d[.\w+]*"
# # reg = r"(?:int|float)\s*=\s*\d[.\w+]*" # ?:- сделать скобки () не сохраняющими
# reg = r"((int|float)\s*=\s*(\d[.\w+]*))" # выводит только элемент в круглых скобках
# print(re.findall(reg, st))

# d = "Word2016, PS6,AI5"
# reg = r"[A-Za-z]+(\d+)" # что есть в круглых скобках то и выводится
# print(re.findall(reg, d)) # для метода findall
# print(re.search(reg, d))

# st = "5 + 7*2 - 4"
# reg = r"\s*[+*-]\s*"
# print(re.split(reg, st))


#  Занятие 17 от 17.03.25
import re

# d = "Word2016, PS6,AI5"
# reg = r"([A-Za-z]+)\d+"
# print(re.findall(reg, d))
# print(re.search(reg, d))

# st = "5 + 7*2 - 4"
# reg = r"\s*([+*-])\s*"
# print(re.split(reg, st))

# s = "Я ищу совпадения в 2025 году. И я их найду в 2 счёта."
# reg = r"(\d+)\s(\D+)"
# print(re.search(reg, s).group()) # group по умолчанию находит все совпадение
# m = re.search(reg, s)
# print(m[0])  # обозначает все совпадение
# print(m[1])  # обозначает  совпадение в первых скобках
# print(m[2])  # обозначает  совпадение во вторых скобках
# print(re.search(reg, s).group(1))
# print(re.search(reg, s).group(2))
# group(0) - находит все совпадение по умолчанию
# group(1) - находит  совпадение внутри первых круглых скобок
# group(2) - находит совпадение внутри вторых круглых скобок
# если круглых скобок нет, а внутри group()- число- будет ошибка

# #  дописать первое с материала урока!______________________________________________
# s = "Самолет прилетает 10/23/2025. Будем рады вас видеть после 10/24/2025."
# reg = r"(\d{2})/(\d{2})/(\d{2})"
# print(re.sub(reg, r"\2.\1.\3", s))
# # #  дописать! 2-е с материала урока +


# s = "yandex.com and yandex.ru"
# reg = r"(([a-z0-9-]{2,}\.)+[a-z]{2,4})"
# print(re.sub(reg, r"http://\1", s))
# print(re.sub(reg, r"http://\2", s))


# print(re.findall(r"\w+", "12 + й"))
# print(re.findall(r"\w+", "12 + й", flags=re.ASCII))
# text = "hello world"
# print(re.findall(r"\w\+", text))
# print(re.findall(r"\w\+", text, re.DEBUG))

# text = "helLo worLd"
# reg = r"l"
# print(re.findall(reg, text))
# print(re.findall(reg, text, re.IGNORECASE))

# text = """"
# one
# two
# """
#
# print(re.findall(r"one.\w+", text))
# print(re.findall(r"one.\w+", text, re.DOTALL))  # работает с многострочным текстом
# #

# text = """"
# one
# two
# """
# print(re.findall(r"one$", text))
# print(re.findall(r"one$", text, re.MULTILINE))
# print(re.findall(r"one$", text, re.MULTILINE))
#
# print(re.findall("""
# [a-z.-]+ # part1
# @ # @
# [a-z.]+ # part2
#  """, "test@mail.ru", re.VERBOSE))

# text = """Python,
# python,
# PYTHON"""
# reg = "(?im)^python"
# print(re.findall(reg, text))

# Рекурсия- функция вызывает сама себя
# def elevator(n):  # 5
#     if n == 0:  # базовый случай
#         print("Вы в подвале")
#         return
#     print("=>", n)
#     elevator(n - 1) # 5 4 3 2 1
#     print(n, end="")
#
#
# n1 = int(input("На каком этаже находитесь"))
# elevator(n1)
#
# # рекурсия- аналог итераций

# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res += i
#     return res
# def sum_list(lst):
#     if len(lst) == 1:
#         print(lst, "=> lst[0]:", lst[0])
#         return lst[0]
#     else:
#         print(lst, "=> lst[0]:", lst[0])
#         return lst[0] + sum_list(lst[1:])
#
#
# print(sum_list([1, 3, 5, 7, 9]))

# законы рекурсии:
# должен быть базовый случай
# алгоритм должен двигаться к базовому случаю
# алгоритм должен вызывать сам себя

# def to_str(n, base):  # 254, 10; 25,10; 2,10
#     convert = "0123456789ABCDF"
#     if n < base:
#         return convert[n] # "2"
#     else:
#         return to_str(n // base, base) + convert[n % base]  # to_str(254 // 10, 10) + "4" +"5"
#
#
# print(to_str(254, 10))

# def to_str(n, base):  # 254, 16; 15,16
#     convert = "0123456789ABCDEF"
#     if n < base:
#         return convert[n] # "F"
#     else:
#         return to_str(n // base, base) + convert[n % base]  # to_str(254 // 10, 10) + convert[14]("E")
#
#
# print(to_str(254, 16))

# names = ["Adam", ["Bob", ["Chet", "Cat"], "Barb", "Berb"], "Alex", ["Bea", "Bill"], "Ann"]
# print(len(names))
# print(names[0])
# print(isinstance(names[0],list)) # возвращает булево значение является ли объект каким-то типом данных
# print(names[1])
# print(isinstance(names[1],list))
# print(names[1][1])
# print(isinstance(names[1][1],list))
# print(names[1][1][0])
# print(isinstance(names[1][1][0],list))

# names = ["Adam", ["Bob", ["Chet", "Cat"], "Barb", "Berb"], "Alex", ["Bea", "Bill"], "Ann"]
#
#
# def count_items(item_list): #["Adam", ["Bob", ["Chet", "Cat"], "Barb", "Berb"], "Alex", ["Bea", "Bill"], "Ann"]
#     count = 0 # 1+5
#     for item in item_list:  #["Bob", ["Chet", "Cat"], "Barb", "Berb"], "Alex", ["Bea", "Bill"], "Ann"]
#         if isinstance(item, list):
#             count += count_items(item)
#         else:
#             count += 1
#     return count
#
#
# print(count_items(names))

# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res += i
#     return res
#
#
# print(sum_list([1, 3, 5, 7, 9]))

# Работа с файлами
# .txt
# f = open("Text.txt", 'r')
# f = open("Text.txt", 'r')
# print(f)
# print(*f)
# print(f.closed)
# f.close()
# print(f.closed)
# print(f.mode)
# print(f.name)
# print(f.encoding)

# f = open("Text.txt", 'r')
# print(f.read(3)) # позволяет указать число символов
# print(f.read()) # позволяет указать число символов
# f.close()

# f = open("Text.txt", 'r') # режим чтения выдает ошибку если файл не найден, по умолчанию параметр- режим чтения
# f.close()

# f = open("xyz.txt", 'w')
# f.write("This is line1.\nThis is line2.\nThis is line2.")
# f.close(
# f = open("xyz.txt")
# print(f.read())
# print(f.readline())
# print(f.readline(8))
# print(f.readline())
# print(f.readline())
# print(f.readlines())
# print(f.readlines(26))
# f.close()

# f = open("xyz.txt")
# for line in f:
#     print(line)
# f.close()

# count = 0
# f = open("xyz.txt")
# for line in f:
#     count += 1
# print(count)
# f.close()

# f = open("xyz.txt")
# print(len(f.readlines()))
# f.close()

# f = open("test.txt",'w')
# f.write("Hello\nWorld\n")
# f.close()
#
# f = open("test.txt",'a')
# f.write("Dangeon master")
# f.close()

# lines = ["This is line1","\nThis is line2","This is line3"]
# f = open("test1.txt",'a')
# f.writelines(lines)
# f.close()

#  Занятие 18 от 19.03.25

# file = "text2.txt"
# f = open(file, "w")
# f.write("Замена строки в текстовом файле;\nИзменить строку в списке;\nЗаписать список в файл;\n")
# f.close()
# f = open(file, "r")
# data = f.readlines()  # список строкровых значений
# print(data)
# data[1] = "Hello World;\n"
# print(data)
# f.close()
# f = open(file, "w")
# f.writelines(data)
# f.close()

# файлы могут хранить строки
# f = open("text3.txt", "w")
# lst = [i for i in range(1, 100, 5)]
# print(lst)
# for index in lst:
#     f.write(str(index)+"\t")
# f.close()
#
# # либо
# f = open("text3.txt", "w")
# lst = [str(i) for i in range(1, 100, 5)]
# print(lst)
# for index in lst:
#     f.write(index)
# f.close()
# # В файлы записываем строковые значения

# f = open("Text.txt","r")
# print(f.read(3))
# print(f.tell()) # возвращает позицию условного курсора в файле
# print(f.seek(1)) # перемещает условный курсор в заданную позицию и возвращает эту позицию
# print(f.read())
# print(f.tell())
# f.close()

# f = open("text.txt","a")
# print(f.write("I am learning Python"))
# print(f.seek(3))
# print(f.write("-new string-"))
# print(f.tell())
# f.close()

# f = open("text.txt","r+") # режим r не позволяет работать с несозданными файлом, читает и записывает в созданном файле
# print(f.write("I am learning Python"))
# print(f.seek(3))
# print(f.write("-new string-"))
# print(f.tell())
# f.close()

# f = open("text.txt","w+") # создался пустой файл
# print(f.read()) # ничего не вывелось, т.к файл пустой, но не вызвалось ошибки
# f.close()

# f = open("text.txt","a+") # создался пустой файл
# print(f.read()) # ничего не вывелось, т.к файл пустой, но не вызвалось ошибки
# f.close()

# Контекстный менеджер
# with open("text.txt", "w") as f:
#     print(f.write("0123456789"))
#     print(f.closed) # файл открыт в пределах табуляции, как только выходим за пределы контекстного менеджера-
#     # файл закрыт
# print(f.closed)

# with open("text.txt", "r") as f:
#     print(f.read())

# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 5.47]
#
#
# def get_line(lt):
#     lt = list(map(str, lt))
#     return "".join(lt)
#
#
# with open("res.txt", "w") as f:
#     f.write(get_line(lst))
# print("Файл записан")

# with open("res.txt", "r") as f:
#     nums = f.read()
# print(nums)
#
# lst = list(map(float, nums.split()))
# print(lst)
# print(sum(lst))

# file_name = "long.txt"
# with open(file_name, "w") as f:
#     f.write("Файл — именованная область данных на носителе информации, используемая как базовый"
#             " объект с данными  в операционных системах.") # взаимодействия


# def longest_word(file):
#     with open(file, "r") as text:
#         lst = text.read().split()
#         print(lst)
#         max_lenght = (len(max(lst, key=len)))
#         print(max_lenght)
#         res = [word for word in lst if len(word) == max_lenght]
#         return res[0] if len(res) == 1 else res
#
#
# print(longest_word(file_name))

# text = ("Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №4\nСтрока №5"
#         "\nСтрока №6\nСтрока №7\nСтрока №8\nСтрока №9\nСтрока №10\n")
# with open("one.txt", "w") as f:
#     f.write(text)
#
# # в файловом менеджере можно открыть несколько файлов, но с разными псевдонимами
# with open("one.txt","r") as fr, open("two.txt","w") as fw:
#     for line in fr:
#         line = line.replace("Строка","Линия-")
#         fw.write(line)

# Модули
# OS и OS.PATH

# import os

# print(os.getcwd()) # путь к текущей директории(папка где находится этот проект)
# print(os.listdir()) # перечислены все файлы и все папки(директории) в папке проекта(по умолчанию список текущего каталога)
# print(os.listdir("..")) #выйти на уровень выше
# print(os.listdir(".venv"))
#
# # os.mkdir("folder") # программно создали папку повторно создать нельзя
# # os.rmdir("folder") # программно удалили папку
# # os.makedirs("nested1/nested2/nested3") # создается папка с промежуточными директориями- повторно создать нельзя
#
# # os.remove("xyz.txt") # удалить файл
# # os.rename("long.txt","ololong.txt") # переименовал файл, может добавить расширение
# # os.rename("ololong.txt","nested1/ololon1g.txt") # переименовал файл, переместил в папку(в существующую директорию)
# os.rename("two.txt.txt","test/two.txt.txt") # ошибка при перемещении в несуществующую директорию
# os.renames("two.txt.txt","test/two.txt.txt") # переименовывает файл, может создавать директории при перемещении
# #если директории не существует

# for root, dirs, files in os.walk("nested1", topdown=True):
#     print("Roots", root)
#     print("\tDirs", dirs)
#     print("\t\tFiles", files)

# for root, dirs, files in os.walk("nested1", topdown=False):
#     print("Roots", root)
#     print("\tDirs", dirs)
#     print("\t\tFiles", files)

# os.rmdir("nested1") # нельзя удалить папку, если она не пуста

#
# def remove_empty_dirs(root_tree):
#     for root, dirs, files in os.walk("nested1", topdown=False):
#         if not os.listdir(root):
#             os.rmdir(root)
#             print(f"Директория {root} удалена")
#
#
# remove_empty_dirs("nested1")

# import os.path
# print(os.path.split(r"H:\_STUDY 2025\Doc_pycharm\nested1\nested2\nested3\res.txt"))
# # разбивает путь на 2 элемента кортежа(head and tail)
# print(os.path.split(r"H:\_STUDY 2025\Doc_pycharm\nested1\nested2\nested3")) # разбиение по последнему \
# #возвращает кортеж и мы можем обратиться к нему по индексу!
# print(os.path.join(r"H:\_STUDY 2025","Doc_pycharm","nested1","nested2","nested3","res.txt")) # собирает путь
# print(os.path.exists(r"H:\_STUDY 2025\Doc_pycharm\nested1\nested2\nested3")) # возвращеет будево значение существует ли путь или папка
# print(os.path.exists(r"H:\_STUDY 2025\Doc_pycharm\nested1\nested3"))
# print(os.path.isfile(r"H:\_STUDY 2025\Doc_pycharm\nested1\nested2\nested3\res.txt")) # является ли элемент файлом
# print(os.path.isdir(r"H:\_STUDY 2025\Doc_pycharm\nested1\nested2\nested3\res.txt")) # является элемент папкой(директорией)

#  Занятие 19 от 24.03.25
# with open("text.txt", "w+") as f:
#     f.write("Hello")
#     f.seek(0)
#     data = f.read()
#     data += "!"
#     f.seek(0)
#     f.write(data)

# git add -A - добавляеn все папки и файлы .git в
# аналог git add --all
# аналог git add main.py только один файл
# аналог git add . - аналог (# git add -A - добавляеn все папки и файлы .git в)
# git rm - убрать из отслеживания

# print("Данные на локальном репозитории")
print("Код созданный на новом устройстве")
