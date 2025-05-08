class Account:
    __slots__ = ["__surname", "__number", "__percent", "__balance"]
    __usd_course = 0.012
    __eur_course = 0.011
    __rub = "RUB"
    __usd = "USD"
    __eur = "EUR"

    def __init__(self, surname, number, percent, balance):
        self.__surname = surname
        self.__number = number
        self.__percent = percent
        self.__balance = balance
        print(f"Счёт #{self.__number} принадлежащий {self.__surname} был открыт.\n{"*" * 50}\n")

    def __del__(self):
        print(f"Счёт #{self.__number} принадлежащий {self.__surname} закрыт.\n{"*" * 50}")

    @classmethod  # изменение курса доллара
    def change_usd(cls, new_usd):
        cls.__usd_course = new_usd

    @classmethod  # изменение курса евро
    def change_eur(cls, new_eur):
        cls.__eur_course = new_eur

    @staticmethod  # статический конвертер
    def converter(balance, exchange_rate):
        return balance * exchange_rate

    @property  # getter для фамилии владельца счёта(не используется, но должен быть)
    def surname(self):
        return self.__surname

    @surname.setter  # setter для изменения фамилии владельца счёта
    def surname(self, new_surname):
        self.__surname = new_surname

    @property  # getter для снятия со счёта(не используется, но должен быть)
    def withdrawal(self):
        return self.__balance

    @withdrawal.setter  # setter для снятия со счёта
    def withdrawal(self, money):
        if money > self.__balance:
            print(f"К сожалению у вас нет {money} {Account.__rub} на счёте.\n"
                  f"Текущий баланс {self.__balance} {Account.__rub}\n")
        else:
            self.__balance -= money
            print(f"Было успешно снято {money} {Account.__rub}\nТекущий баланс {self.__balance} {Account.__rub}\n")

    @property  # getter для пополнения счёта(не используется, но должен быть)
    def add_money(self):
        return self.__balance

    @add_money.setter  # setter для пополнения счёта
    def add_money(self, money):
        self.__balance += money
        print(f"{money} {Account.__rub} было успешно добавлено!\nТекущий баланс {self.__balance} {Account.__rub}\n")

    @property  # getter для начисления процентов
    def add_percent(self):
        self.__balance += self.__balance * self.__percent
        return f"Проценты были успешно начислены!\nТекущий баланс {self.__balance} {Account.__rub}\n"

    @property
    def to_usd(self):  # конвертация в доллары
        balance_usd = Account.converter(self.__balance, Account.__usd_course)
        return f"Состояние счёта: {balance_usd} {Account.__usd} "

    @property
    def to_eur(self):  # конвертация в евро
        balance_eur = Account.converter(self.__balance, Account.__eur_course)
        return f"Состояние счета: {balance_eur} {Account.__eur}"

    @property  # getter для получения информации о счёте
    def account_info(self):
        info = (f"Информация о счете:\n{"-" * 20}\n#{self.__number}\nВладелец: {self.__surname}\n"
                f"Текущий баланс {self.__balance} {Account.__rub}\nПроценты: {self.__percent:.0%}\n")
        return info


person1 = Account("Долгих", "12345", 0.03, 1000)
print(person1.account_info)
print(person1.to_usd)
print(person1.to_eur)
Account.change_usd(2)
Account.change_eur(3)
print()
print(person1.to_usd)
print(person1.to_eur)
person1.surname = "Дюма"
print(person1.account_info)
print(person1.add_percent)
person1.withdrawal = 100
person1.withdrawal = 3000
person1.add_money = 5000
person1.withdrawal = 3000


# class Account:
# #     __slots__ = ["__surname", "__number", "__percent", "__balance"]
# #     __usd_course = 0.012
# #     __eur_course = 0.011
# #     __rub = "RUB"
# #     __usd = "USD"
# #     __eur = "EUR"
# #
# #     # Инициализатор
# #     def __init__(self, surname, number, percent, balance):
# #         self.__surname = surname
# #         self.__number = number
# #         self.__percent = percent
# #         self.__balance = balance
# #         print(f"Счёт #{self.__number} принадлежащий {self.__surname} был открыт.\n{"*" * 50}\n")
# #
# #     # Деструктор для экземпляров класса.
# #     def __del__(self):
# #         print(f"Счёт #{self.__number} принадлежащий {self.__surname} закрыт.\n{"*" * 50}")
# #
# #     # Метод изменения курса доллара внутри класса.
# #     @classmethod
# #     def change_usd(cls, new_usd):
# #         cls.__usd_course = new_usd
# #
# #     # Метод изменения курса евро внутри класса.
# #     @classmethod
# #     def change_eur(cls, new_eur):
# #         cls.__eur_course = new_eur
# #
# #     # Статический конвертер.
# #     @staticmethod
# #     def converter(balance, exchange_rate):
# #         return balance * exchange_rate
# #
# #     # Getter для фамилии владельца счёта(не используется, но должен быть).
# #     @property
# #     def surname(self):
# #         return self.__surname
# #
# #     # Setter для изменения фамилии владельца счёта.
# #     @surname.setter
# #     def surname(self, new_surname):
# #         self.__surname = new_surname
# #
# #     # @property  # getter для снятия со счёта(не используется, но должен быть)
# #     # def withdrawal(self):
# #     #     return self.__balance
# #
# #     # Метод для снятия средств со счёта с проверкой баланса, выводит баланс в рублях.
# #     def withdrawal(self, money):
# #         if money > self.__balance:
# #             print(f"К сожалению у вас нет {money} {Account.__rub} на счёте.\n{self.print_balance()}\n")
# #         else:
# #             self.__balance -= money
# #             print(f"Было успешно снято {money} {Account.__rub}\n{self.print_balance()}\n")
# #
# #     # @property  # getter для пополнения счёта(не используется, но должен быть)
# #     # def add_money(self):
# #     #     return self.__balance
# #
# #     # Метод пополнения счета в рублях, выводит баланс в рублях.
# #     def add_money(self, money):
# #         self.__balance += money
# #         print(f"{money} {Account.__rub} было успешно добавлено!\n{self.print_balance()}\n")
# #
# #     # Метод начисления процентов по счёту, выводит баланс в рублях.
# #     def add_percent(self):
# #         self.__balance += self.__balance * self.__percent
# #         print(f"Проценты были успешно начислены!\n{self.print_balance()}\n")
# #
# #     # Метод вывода результата конвертации рубли в доллар.
# #     def to_usd(self):
# #         balance_usd = Account.converter(self.__balance, Account.__usd_course)
# #         print(f"Состояние счёта: {balance_usd} {Account.__usd}")
# #
# #     # Метод вывода результата конвертации рубли в евро.
# #     def to_eur(self):
# #         balance_eur = Account.converter(self.__balance, Account.__eur_course)
# #         print(f"Состояние счета: {balance_eur} {Account.__eur}")
# #
# #     # Метод вывода баланса в рублях(вспомогательный).
# #     def print_balance(self):
# #         return f"Текущий баланс {self.__balance} {Account.__rub}"
# #
# #     # Метод выводящий сведения о состоянии открытого счёта.
# #     def account_info(self):
# #         info = (f"Информация о счете:\n{"-" * 20}\n#{self.__number}\nВладелец: {self.__surname}\n"
# #                 f"{self.print_balance()}\nПроценты: {self.__percent:.0%}\n")
# #         print(info)
# #
# #
# # person1 = Account("Долгих", "12345", 0.03, 1000)
# # person1.account_info()
# # person1.to_usd()
# # person1.to_eur()
# # Account.change_usd(2)
# # Account.change_eur(3)
# # print()
# # person1.to_usd()
# # person1.to_eur()
# # person1.surname = "Дюма"
# # person1.account_info()
# # person1.add_percent()
# # person1.withdrawal(100)
# # person1.withdrawal(3000)
# # person1.add_money(5000)
# # person1.withdrawal(3000)