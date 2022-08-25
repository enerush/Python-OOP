"""
Подвиг 6.
Объявите дескриптор данных FloatValue, который бы устанавливал и возвращал вещественные значения. При записи
вещественного числа должна выполняться проверка на вещественный тип данных. Если проверка не проходит, то генерировать
исключение командой:
raise TypeError("Присваивать можно только вещественный тип данных.")

Объявите класс Cell, в котором создается объект value дескриптора FloatValue. А объекты класса Cell должны создаваться
командой:
cell = Cell(начальное значение ячейки)

Объявите класс TableSheet, с помощью которого создается таблица из N строк и M столбцов следующим образом:
table = TableSheet(N, M)
Каждая ячейка этой таблицы должна быть представлена объектом класса Cell, работать с вещественными числами через объект
value (начальное значение должно быть 0.0).

В каждом объекте класса TableSheet должен формироваться локальный атрибут:
cells - список (вложенный) размером N x M, содержащий ячейки таблицы (объекты класса Cell).

Создайте объект table класса TableSheet с размером таблицы N = 5, M = 3. Запишите в эту таблицу числа от 1.0 до 15.0
(по порядку).

P.S. На экран в программе выводить ничего не нужно.
"""


class FloatValue:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self._check_num(value)
        instance.__dict__[self.name] = value
    @staticmethod
    def _check_num(num):
        if type(num) is not float:
            raise TypeError("Присваивать можно только вещественный тип данных.")


class Cell:
    value = FloatValue()

    def __init__(self, value=0.0):
        self.value = value


class TableSheet:  # с помощью которого создается таблица из N строк и M столбцов следующим образом:
    def __init__(self, N, M):
        self.cells = [[Cell() for _ in range(M)] for _ in range(N)]
        self.N = N
        self.M = M

    def show(self):
        for i in range(self.N):
            for j in range(self.M):
                print(self.cells[i][j].value, end='  ')
            print()

    def set(self):
        count = 1.0
        for i in range(self.N):
            for j in range(self.M):
                self.cells[i][j].value = count
                count += 1


table = TableSheet(5, 3)
table.set()