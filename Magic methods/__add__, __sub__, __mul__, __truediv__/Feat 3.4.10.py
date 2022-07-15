"""
    Подвиг 10 (на повторение).
В нейронных сетях использую операцию под названием Max Pooling. Суть ее состоит в сканировании прямоугольной
таблицы чисел (матрицы) окном определенного размера (обычно, 2x2 элемента) и выбора наибольшего значения в пределах
этого окна, если окна выходят за пределы матрицы, то они пропускаются (игнорируются).
Мы повторим эту процедуру. Для этого в программе нужно объявить класс с именем MaxPooling, объекты которого создаются
командой:
    mp = MaxPooling(step=(2, 2), size=(2,2))
    - где step - шаг смещения окна по горизонтали и вертикали; size - размер окна по горизонтали и вертикали.
Параметры step и size по умолчанию должны принимать кортеж со значениями (2, 2).
Для выполнения операции Max Pooling используется команда:
    res = mp(matrix)
    - где matrix - прямоугольная таблица чисел; res - ссылка на результат обработки таблицы matrix
           (должна создаваться новая таблица чисел.

Прямоугольную таблицу чисел следует описывать вложенными списками. Если при сканировании таблицы часть окна выходит за
ее пределы, то эти данные отбрасывать (не учитывать все окно).
Если matrix не является прямоугольной таблицей или содержит хотя бы одно не числовое значение, то должно генерироваться
исключение командой:
    raise ValueError("Неверный формат для первого параметра matrix.")
"""


class MaxPooling:
    def __init__(self, step=(2, 2), size=(2, 2)):
        self.step = step
        self.size = size

    def __call__(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0

        if rows == 0:
            return [[]]

        if not all(map(lambda x: len(x) == cols, matrix)) or\
                not all(map(lambda row: all(map(lambda x: type(x) in (int, float), row)), matrix)):
            raise ValueError('Wrong format for matrix`s first element')

        h, w = self.size[0], self.size[1]
        sh, sw = self.step[0], self.step[1]

        rows_range = (rows - h) // sh + 1
        cols_range = (cols - w) // sw + 1

        res = [[0] * cols_range for _ in range(rows_range)]
        for i in range(rows_range):
            for j in range(cols_range):
                s = (x for r in matrix[i * sh: i * sh + h] for x in r[j * sw: j * sw + w])
                res[i][j] = max(s)
        return res


mp = MaxPooling()
res = mp([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]])    # [[6, 8], [9, 7]]
print(res)
