"""
Подвиг 10 (на повторение).
Объявите класс с именем Triangle, объекты которого создаются командой:
    tr = Triangle(a, b, c) - где a, b, c - длины сторон треугольника (числа: целые или вещественные).
В классе Triangle объявите следующие дескрипторы данных:
    a, b, c - для записи и считывания длин сторон треугольника.

При записи нового значения нужно проверять, что присваивается положительное число (целое или вещественное).
Иначе, генерируется исключение командой:
    raise ValueError("длины сторон треугольника должны быть положительными числами")

Также нужно проверять, что все три стороны a, b, c могут образовывать стороны треугольника.
То есть, должны выполняться условия:
    a < b+c; b < a+c; c < a+b
Иначе генерируется исключение командой:
    raise ValueError("с указанными длинами нельзя образовать треугольник")

Наконец, с объектами класса Triangle должны выполняться функции:
    len(tr) - возвращает периметр треугольника;
    tr() - возвращает площадь треугольника (можно вычислить по формуле Герона: s = sqrt(p * (p-a) * (p-b) * (p-c)),
где p - полупериметр треугольника).
"""


class Triangle:
    def __init__(self, a: (int, float), b: (int, float), c: (int, float)):
        self.a = a
        self.b = b
        self.c = c

    def __setattr__(self, key, value):
        self._check_num(value)
        object.__setattr__(self, key, value)
        if len(self.__dict__) == 3:
            if self.a >= self.b + self.c or self.b >= self.a + self.c or self.c >= self.a + self.b:
                raise ValueError("с указанными длинами нельзя образовать треугольник")

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self._check_num(value):
            setattr(instance, self.name, value)

    @staticmethod
    def _check_num(num):
        if num <= 0:
            raise ValueError("длины сторон треугольника должны быть положительными числами")

    def __len__(self):
        return self.a + self.b + self.c

    def __call__(self):
        a, b, c = self.a, self.b, self.c
        p = len(self) / 2
        return (p * (p-a) * (p-b) * (p-c))**0.5


tr = Triangle(3, 6, 8)
print(tr.__dict__)
print(tr())