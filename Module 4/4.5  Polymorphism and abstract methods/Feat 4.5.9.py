"""
Подвиг 9 (на повторение).
Вам поручают разработать класс для представления маршрутов в навигаторе. Для этого требуется объявить класс с именем Track,
объекты которого могут создаваться командами:
    tr = Track(start_x, start_y)
    tr = Track(pt1, pt2, ..., ptN)
где start_x, start_y - начальная координата маршрута; pt1, pt2, ..., ptN - набор из произвольного числа точек (координат) маршрута.

В каждом объекте класса Track должен формироваться локальный приватный атрибут:
    __points - список из точек (координат) маршрута.

Каждая точка (координата) должна определяться классом PointTrack, объекты которого создаются командой:
    pt = PointTrack(x, y)
где x, y - числа (целые или вещественные). Если передается другой тип данных, то должно генерироваться исключение командой:
    raise TypeError('координаты должны быть числами')

В классе PointTrack переопределите магический метод __str__, чтобы информация об объекте класса возвращалась в виде строки:
    "PointTrack: <x>, <y>"

Например:
pt = PointTrack(1, 2)
print(pt) # PointTrack: 1, 2

В самом классе Track должно быть свойство (property) с именем:
    points - для получения кортежа из точек маршрута.

Также в классе Track должны быть методы:
    def add_back(self, pt) - добавление новой точки в конец маршрута (pt - объект класса PointTrack);
    def add_front(self, pt) - добавление новой точки в начало маршрута (pt - объект класса PointTrack);
    def pop_back(self) - удаление последней точки из маршрута;
    def pop_front(self) - удаление первой точки из маршрута.

P.S. В программе требуется объявить только классы. На экран выводить ничего не нужно.
"""
from collections import deque


class PointTrack:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __setattr__(self, key, value):
        if type(value) not in (int, float):
            raise TypeError('координаты должны быть числами')
        return super().__setattr__(key, value)

    def __str__(self):
        return f"PointTrack: {self.x}, {self.y}"


class Track:

    def __init__(self, *args):
        self.__points = deque(args)

    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, value):
        self.__points = tuple(value)

    def add_back(self, pt):
        self.__points.append(pt)

    def add_front(self, pt):
        self.__points.appendleft(pt)

    def pop_back(self):
        del self.__points[-1]

    def pop_front(self):
        del self.__points[0]


tr = Track(PointTrack(0, 0), PointTrack(1.2, -0.5), PointTrack(2.4, -1.5))
tr.add_back(PointTrack(1.4, 0))
tr.pop_front()
for pt in tr.points:
    print(pt)


