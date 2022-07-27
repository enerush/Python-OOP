"""
Подвиг 10 (на повторение).
Объявите класс EmailValidator для проверки корректности email-адреса. Необходимо запретить создание объектов этого класса:
при создании экземпляров должно возвращаться значение None, например:
em = EmailValidator() # None
В самом классе реализовать следующие методы класса (@classmethod):
check_email(cls, email) - возвращает True, если email записан верно и False - в противном случае;
get_random_email(cls) - для генерации случайного email-адреса по формату: xxxxxxx...xxx@gmail.com, где x - любой
допустимый символ в email (латинский буквы, цифры, символ подчеркивания и точка).

Корректность строки email определяется по следующим критериям:
- допустимые символы: латинский алфавит, цифры, символы подчеркивания, точки и собачка @ (одна);
- длина email до символа @ не должна превышать 100 (сто включительно);
- длина email после символа @ не должна быть больше 50 (включительно);
- после символа @ обязательно должна идти хотя бы одна точка;
- не должно быть двух точек подряд.

Также в классе нужно реализовать приватный статический метод класса:
is_email_str(email) - для проверки типа переменной email, если строка, то возвращается значение True, иначе - False.

Метод is_email_str() следует использовать в методе check_email() перед проверкой корректности email.
Если параметр email не является строкой, то check_email() возвращает False.

P.S. В программе требуется объявить только класс. На экран ничего выводить не нужно.
"""

from string import ascii_letters
from random import randint, choices


class EmailValidator:

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def check_email(cls, email):
        if cls.__is_email_str(email):
            if len(email.split('@')) != 2:
                return False
            el1, args = email.split('@')

            if len(args.split('.')) != 2:
                return False
            el2, el3 = args.split('.')
            lst = ''.join([el1, el2, el3])
            prev = ''

            for i in range(len(lst)):
                if lst[i] not in ascii_letters + '1234567890_.':
                    return False
                if lst[i] == '.' and prev == '.':
                    return False
                prev = lst[i]

            if len(el1) > 100 and len(el2 + el3) > 50:
                return False
            return True

        return False

    @staticmethod
    def get_random_email():
        symbols = ascii_letters + '_.'
        ln = randint(1, 15)
        res = ''.join(choices(symbols, k=ln)) + '@gmail.com'
        return res

    @staticmethod
    def __is_email_str(email):
        if type(email) is str:
            return True

        return False


res1 = EmailValidator.check_email("sc_lib@list.ru")  # True
res2 = EmailValidator.check_email("sc_lib@list_ru")  # False