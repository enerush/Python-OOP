"""
Подвиг 3.
Объявите класс с именем Clock и определите в нем следующие переменные и методы:
- приватная локальная переменная time для хранения текущего времени, целое число (своя для каждого объекта класса Clock
с начальным значением 0);
- публичный метод set_time(tm) для установки текущего времени (присваивает значение tm приватному локальному свойству
time, если метод check_time(tm) возвратил True);
- публичный метод get_time() для получения текущего времени из приватной локальной переменной time;
- приватный метод класса check_time(tm) для проверки корректности времени в переменной tm (возвращает True, если
значение корректно и False - в противном случае).

Проверка корректности выполняется по критерию: tm должна быть целым числом, больше или равна нулю и меньше 100 000.
Объекты класса Clock предполагается использовать командой:
clock = Clock(время)
Создайте объект clock класса Clock и установите время, равным 4530.
P.S. На экран ничего выводить не нужно.
"""


class Clock:
    def __init__(self, time=0):
        self.__time = time

    def set_time(self, tm):
        if self.__check_time(tm):
            self.__time = tm

    def get_time(self):
        return self.__time

    @classmethod
    def __check_time(cls, tm):
        return type(tm) is int and 0 <= tm < 100000


clock = Clock()
clock.set_time(4530)