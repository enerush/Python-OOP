"""
Подвиг 9 (на повторение).
Объявите класс StringDigit, который наследуется от стандартного класса str. Объекты класса StringDigit должны
создаваться командой:
    sd = StringDigit(string)
где string - строка из цифр (например, "12455752345950"). Если в строке string окажется хотя бы один не цифровой символ,
то генерировать исключение командой:
    raise ValueError("в строке должны быть только цифры")

Также в классе StringDigit нужно переопределить оператор + (конкатенации строк) так, чтобы операции:
    sd = sd + "123"
    sd = "123" + sd
создавали новые объекты класса StringDigit (а не класса str). Если же при соединении строк появляется не цифровой символ,
то генерировать исключение:
    raise ValueError("в строке должны быть только цифры")
"""


class StringDigit(str):
    def __init__(self, string):
        self._check_data(string)
        self.string = string

    @staticmethod
    def _check_data(string):
        for i in string:
            if i not in '1234567890':
                raise ValueError("в строке должны быть только цифры")

    def __add__(self, string):
        self._check_data(string)
        return StringDigit(super().__add__(string))

    def __radd__(self, other):
        self._check_data(other)
        return StringDigit(other + self.string)


sd = StringDigit("123")
print(sd)           # 123
print(sd + "456")   # StringDigit: 123456
print(type("789" + sd))   # StringDigit: 789123456
#print(sd + "12f")   # ValueError