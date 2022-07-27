"""
Подвиг 7.
Объявите класс RadiusVector2D, объекты которого должны создаваться командами:
v1 = RadiusVector2D()        # радиус-вектор с координатами (0; 0)
v2 = RadiusVector2D(1)       # радиус-вектор с координатами (1; 0)
v3 = RadiusVector2D(1, 2)    # радиус-вектор с координатами (1; 2)

В каждом объекте класса RadiusVector2D должны формироваться локальные приватные атрибуты:
__x, __y - координаты конца вектора (изначально значения равны 0, если не передано какое-либо другое).

В классе RadiusVector2D необходимо объявить два объекта-свойства:
x - для изменения и считывания локального атрибута __x;
y - для изменения и считывания локального атрибута __y.

При инициализации и изменении локальных атрибутов, необходимо проверять корректность передаваемых значений:
- значение должно быть числом (целым или вещественным) в диапазоне [MIN_COORD; MAX_COORD].

Если проверка не проходит, то координаты не меняются (напомню, что при инициализации они изначально равны 0).
Величины MIN_COORD = -100, MAX_COORD = 1024 задаются как публичные атрибуты класса RadiusVector2D.

Также в классе RadiusVector2D необходимо объявить статический метод:
norm2(vector) - для вычисления квадратической нормы vector - переданного объекта класса RadiusVector2D
(квадратическая норма вектора: x*x + y*y).

P.S. В программе требуется объявить только класс. На экран ничего выводить не нужно.
"""


class RadiusVector2D:  # объекты которого должны создаваться командами
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x=0, y=0):
        if self._check_coord(x):
            self.__x = x
        else:
            self.__x = 0

        if self._check_coord(y):
            self.__y = y
        else:
            self.__y = 0

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if self._check_coord(x):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if self._check_coord(y):
            self.__y = y

    @classmethod
    def _check_coord(cls, num):
        if type(num) in (int, float) and cls.MIN_COORD < num < cls.MAX_COORD:
            return True
        return False

    @staticmethod
    def norm2(vector):
        return vector.x**2 + vector.y**2