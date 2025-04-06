# class Person:
#     # __slots__ = ["__name", "__age"]
#
#     @staticmethod
#     def check_name(n):
#         if isinstance(n, str):
#             return True
#         return False
#
#     @staticmethod
#     def check_age(a):
#         if isinstance(a, int) and a > 0:
#             return True
#         return False
#
#     def __init__(self, name="Default", age=1):
#         if Person.check_name(name):
#             self.__name = name
#         else:
#             print("Некорректное имя")
#         if Person.check_age(age):
#             self.__age = age
#         else:
#             print("Некорректный возраст")
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         if Person.check_name(name):
#             self.__name = name
#         else:
#             print("Некорректное имя")
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, age):
#         if Person.check_age(age):
#             self.__age = age
#         else:
#             print("Некорректный возраст")
#
#     @age.deleter
#     def age(self):
#         del self.__age
#
#
# p1 = Person("Irina", 26)
# print(p1.__dict__)
# print(p1.name, p1.age, sep="\n")
# p1.name, p1.age = "Igor", 31
# print(p1.name, p1.age, sep="\n")
# del p1.name
# print(p1.__dict__)
#

