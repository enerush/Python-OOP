"""
Подвиг 10 (на повторение).
Объявите в программе класс Vector, объекты которого создаются командой:
v = Vector(x1, x2, ..., xN)
где x1, x2, ..., xN - координаты радиус-вектора (числа: целые или вещественные).
С объектами этого класса должны выполняться команды:
v1 = Vector(1, 2, 3)
v2 = Vector(3, 4, 5)
v = v1 + v2 # формируется новый вектор (объект класса Vector) с соответствующими координатами
v = v1 - v2 # формируется новый вектор (объект класса Vector) с соответствующими координатами
Если размерности векторов v1 и v2 не совпадают, то генерировать исключение:
    raise TypeError('размерности векторов не совпадают')
В самом классе Vector объявите метод с именем get_coords, который возвращает кортеж из текущих координат вектора.
На основе класса Vector объявите дочерний класс VectorInt для работы с целочисленными координатами:
v = VectorInt(1, 2, 3, 4)
v = VectorInt(1, 0.2, 3, 4) # ошибка: генерируется исключение raise ValueError('координаты должны быть целыми числами')

При операциях сложения и вычитания с объектом класса VectorInt:
v = v1 + v2  # v1 - объект класса VectorInt
v = v1 - v2  # v1 - объект класса VectorInt

должен формироваться объект v как объект класса Vector, если хотя бы одна координата является вещественной. Иначе,
v должен быть объектом класса VectorInt.
"""


class Vector:
    def __init__(self, *args):
        if self.__class__ is VectorInt:
            self.check_int_coord(args)
        self.coords = list(args)

    def __add__(self, other):
        self.check_lens(other)
        res = [i + j for i, j in zip(self.coords, other.coords)]
        if self.__class__ is VectorInt and other.__class__ is VectorInt:
            return VectorInt(*res)

        if all([i is int for i in res]):
            return VectorInt(*res)
        return Vector(*res)

    def __sub__(self, other):
        self.check_lens(other)
        res = [i - j for i, j in zip(self.coords, other.coords)]
        if all([i is int for i in res]):
            return VectorInt(*res)
        return Vector(*res)

    def check_lens(self, obj2):
        if len(self.coords) != len(obj2.coords):
            TypeError('размерности векторов не совпадают')

    @staticmethod
    def check_int_coord(coords):
        if not all([type(num) is int for num in coords]):
            raise ValueError('координаты должны быть целыми числами')

    def get_coords(self):
        return tuple(self.coords)


class VectorInt(Vector):
    pass


v1 = VectorInt(1, 2, 3)
v2 = VectorInt(3, 4, 5)
print(type(v1 + v2))