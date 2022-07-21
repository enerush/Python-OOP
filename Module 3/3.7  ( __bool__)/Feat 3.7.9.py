"""
Подвиг 9 (на повторение).
Объявите в программе класс Vector, объекты которого создаются командой:
    v = Vector(x1, x2, x3,..., xN)
где x1, x2, x3,..., xN - координаты вектора (числа: целые или вещественные).

С каждым объектом класса Vector должны выполняться операторы:
    v1 + v2 # суммирование соответствующих координат векторов
    v1 - v2 # вычитание соответствующих координат векторов
    v1 * v2 # умножение соответствующих координат векторов
    v1 += 10 # прибавление ко всем координатам вектора числа 10
    v1 -= 10 # вычитание из всех координат вектора числа 10
    v1 += v2
    v2 -= v1
    v1 == v2 # True, если соответствующие координаты векторов равны
    v1 != v2 # True, если хотя бы одна пара координат векторов не совпадает

При реализации бинарных операторов +, -, * следует создавать новые объекты класса Vector с новыми (вычисленными) координатами.
При реализации операторов +=, -= координаты меняются в текущем объекте, не создавая новый.
Если число координат (размерность) векторов v1 и v2 не совпадает, то при операторах +, -, * должно генерироваться исключение командой:
    raise ArithmeticError('размерности векторов не совпадают')
"""


class Vector:
    def __init__(self, *args):
        self.lst = list(args)

    def coords(self):
        return self.lst

    def __len__(self):
        return len(self.lst)

    def __eq__(self, other):
        if len(self) != len(other):
            raise ArithmeticError('размерности векторов не совпадают')
        return all([i == j for i, j in zip(self.lst, other.lst)])

    def __add__(self, other):
        if type(other) is Vector:
            if len(self) != len(other):
                raise ArithmeticError('размерности векторов не совпадают')
            return Vector(*[i + j for i, j in zip(self.lst, other.lst)])
        return Vector(*[i + other for i in self.lst])

    def __iadd__(self, other):
        self.lst = (self + other).lst
        return self

    def __sub__(self, other):
        if type(other) is Vector:
            if len(self) != len(other):
                raise ArithmeticError('размерности векторов не совпадают')
            return Vector(*[i - j for i, j in zip(self.lst, other.lst)])
        return Vector(*[i - other for i in self.lst])

    def __isub__(self, other):
        self.lst = (self - other).lst
        return self

    def __mul__(self, other):
        if len(self) != len(other):
            raise ArithmeticError('размерности векторов не совпадают')
        other = other.lst if type(other) is Vector else other
        return Vector(*[i * j for i, j in zip(self.lst, other)])


v1 = Vector(1, 2, 3)
v1.coords()
v2 = Vector(4, 5, 6)
print(v1 == v2)  # False
print(v1 != v2)  # True
print((v1 + v2).coords())  # [5, 7, 9]
print((v1 - v2).coords())  # [-3, -3, -3]
print((v1 * v2).coords())  # [4, 10, 18]
v1 += 10
print(v1.coords())  # [11, 12, 13]
v1 -= 10
print(v1.coords())  # [1, 2, 3]
v1 += v2
print(v1.coords())  # [5, 7, 9]
v2 -= v1
print(v2.coords())  # [-1, -2, -3]
