"""
Подвиг 3.
Создается проект, в котором предполагается использовать списки из целых чисел. Для этого вам ставится задача создать
класс с именем ListInteger с базовым классом list и переопределить три метода:
    __init__()
    __setitem__()
    append()
так, чтобы список ListInteger содержал только целые числа. При попытке присвоить любой другой тип данных, генерировать
исключение командой:
    raise TypeError('можно передавать только целочисленные значения')
"""


class ListInteger(list):
    def __init__(self, iterable):
        super().__init__(map(self._check_value, iterable))

    @staticmethod
    def _check_value(value):
        if type(value) is not int:
            raise TypeError('можно передавать только целочисленные значения')
        return value

    def __setitem__(self, key, value):
        super().__setitem__(key, self._check_value(value))

    def append(self, value):
        super().append(self._check_value(value))


s = ListInteger((1, 2, 3))
print(s)
s[1] = 10
s.append(11)
print(s)
# s[0] = 10.5  # TypeError