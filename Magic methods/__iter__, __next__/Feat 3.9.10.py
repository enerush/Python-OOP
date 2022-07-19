"""
Подвиг 10 (на повторение).
Объявите класс Matrix (матрица) для операций с матрицами. Объекты этого класса должны создаваться командой:
m1 = Matrix(rows, cols, fill_value)
где rows, cols - число строк и столбцов матрицы; fill_value - заполняемое начальное значение элементов матрицы
(должно быть число: целое или вещественное). Если в качестве аргументов передаются не числа, то генерировать исключение:
raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')

Также объекты можно создавать командой:
m2 = Matrix(list2D)
где list2D - двумерный список (прямоугольный), состоящий из чисел (целых или вещественных). Если список list2D не
прямоугольный, или хотя бы один из его элементов не число, то генерировать исключение командой:
raise TypeError('список должен быть прямоугольным, состоящим из чисел')

Для объектов класса Matrix должны выполняться следующие команды:
matrix = Matrix(4, 5, 0)
res = matrix[0, 0] # возвращается первый элемент матрицы
matrix[indx1, indx2] = value # элементу матрицы с индексами (indx1, indx2) присваивается новое значение

Если в результате присвоения тип данных не соответствует числу, то генерировать исключение командой:
raise TypeError('значения матрицы должны быть числами')

Если указываются недопустимые индексы матрицы (должны быть целыми числами от 0 и до размеров матрицы), то генерировать
исключение:
raise IndexError('недопустимые значения индексов')

Также с объектами класса Matrix должны выполняться операторы:
matrix = m1 + m2 # сложение соответствующих значений элементов матриц m1 и m2
matrix = m1 + 10 # прибавление числа ко всем элементам матрицы m1
matrix = m1 - m2 # вычитание соответствующих значений элементов матриц m1 и m2
matrix = m1 - 10 # вычитание числа из всех элементов матрицы m1

Во всех этих операция должна формироваться новая матрица с соответствующими значениями. Если размеры матриц не совпадают
(разные хотя бы по одной оси), то генерировать исключение командой:
raise ValueError('операции возможны только с матрицами равных размеров')
"""


class Matrix:
    def __init__(self, *args):
        if len(args) == 1:
            self.mtrx = args[0]

        else:
            self.rows, self.cols, self.fill_value = args
            self.mtrx = [[self.fill_value] * self.cols for _ in range(self.rows)]

    @staticmethod
    def _check_square(mtrx):
        x = len(mtrx[0])
        flag1 = all([len(row) == x for row in mtrx])
        return flag1

    def _check_el(self, mtrx):
        return all([all([x in (int, float) for x in row]) for row in mtrx])

    def __setattr__(self, key, value):
        if key in ('rows', 'cols') and type(value) is not int:
            raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')
        elif key == 'fill_value' and type(value) not in (int, float):
            raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')
        elif key == 'mtrx' and not self._check_square(value):
            raise TypeError('список должен быть прямоугольным, состоящим из чисел')
        elif key == 'mtrx' and self._check_el(value):
            raise TypeError('значения матрицы должны быть числами')
        else:
            return object.__setattr__(self, key, value)

    def __getitem__(self, item):
        r, c = item
        if not (0 <= c < len(self.mtrx[0])) or not (0 <= r < len(self.mtrx)):
            raise IndexError('недопустимые значения индексов')
        return self.mtrx[r][c]

    def __setitem__(self, key, value):
        r, c = key
        if not 0 <= c < len(self.mtrx[0]) or not 0 <= r < len(self.mtrx):
            raise IndexError('недопустимые значения индексов')
        if not type(value) in (int, float):
            raise TypeError('значения матрицы должны быть числами')
        self.mtrx[r][c] = value

    @staticmethod
    def _check_mtrx(mtrx1, mtrx2):
        r, c = len(mtrx1.mtrx), len(mtrx1.mtrx[0])
        r1, c1 = len(mtrx2.mtrx), len(mtrx2.mtrx[0])
        if r != r1 or c != c1:
            raise ValueError('операции возможны только с матрицами равных размеров')

    def __add__(self, other):
        r, c = len(self.mtrx), len(self.mtrx[0])
        if type(other) in (int, float):
            return Matrix([[self[i, j] + other for j in range(c)] for i in range(r)])
        else:
            self._check_mtrx(self, other)
            return Matrix([[self[i, j] + other[i, j] for j in range(c)] for i in range(r)])

    def __sub__(self, other):
        r, c = len(self.mtrx), len(self.mtrx[0])
        if type(other) in (int, float):
            return Matrix([[self[i, j] - other for j in range(c)] for i in range(r)])
        else:
            self._check_mtrx(self, other)
            return Matrix([[self[i, j] - other[i, j] for j in range(c)] for i in range(r)])


mt1 = Matrix(3, 5, 3)
mt2 = Matrix(3, 5, 5)
print(mt1.mtrx)
print(mt1 + 5.5)
