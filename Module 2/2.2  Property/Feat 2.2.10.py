"""
Подвиг 10 (на закрепление).
Вы создаете телефонную записную книжку. Она определяется классом PhoneBook. Объекты этого класса создаются командой:
p = PhoneBook()

А сам класс должен иметь следующий набор методов:
add_phone(phone) - добавление нового номера телефона (в список);
remove_phone(indx) - удаление номера телефона по индексу списка;
get_phone_list() - получение списка из объектов всех телефонных номеров.

Каждый номер телефона должен быть представлен классом PhoneNumber. Объекты этого класса должны создаваться командой:
note = PhoneNumber(number, fio)
где number - номер телефона (число) в формате XXXXXXXXXXX (одиннадцати цифр, X - цифра); fio - Ф.И.О. владельца номера
(строка).

В каждом объекте класса PhoneNumber должны формироваться локальные атрибуты:
number - номер телефона (число);
fio - ФИО владельца номера телефона.

Необходимо объявить два класса PhoneBook и PhoneNumber в соответствии с заданием.
P.S. В программе требуется объявить только классы. На экран ничего выводить не нужно.
"""


class PhoneBook:  # Объекты этого класса создаются командой:
    def __init__(self):
        self.lst = []

    def add_phone(self, phone):  # добавление нового номера телефона (в список)
        self.lst.append(phone)

    def remove_phone(self, indx):  # удаление номера телефона по индексу списка
        del self.lst[indx]

    def get_phone_list(self):  # получение списка из объектов всех телефонных номеров
        return self.lst


class PhoneNumber:  # Объекты этого класса должны создаваться командой:

    def __init__(self, number, fio):
        self.number = self._check_num(number)
        self.fio = self._check_fio(fio)

    @staticmethod
    def _check_num(num):
        if type(num) is int and len(str(num)) == 11:
            return num

    @staticmethod
    def _check_fio(fio):
        if type(fio) is str:
            return fio


p = PhoneBook()
p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
p.add_phone(PhoneNumber(21345678901, "Панда"))
phones = p.get_phone_list()