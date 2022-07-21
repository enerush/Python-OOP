"""
Подвиг 6.
Вам дают задание разработать итератор для последовательного перебора элементов вложенных (двумерных)
списков следующей структуры:
    lst = [[x00],
           [x10, x11],
        [x20, x21, x22],
        [x30, x31, x32, x33],
        ...
        ]

Для этого необходимо в программе объявить класс с именем TriangleListIterator, объекты которого создаются командой:
    it = TriangleListIterator(lst) - где lst - ссылка на перебираемый список.
Затем, с объектами класса TriangleListIterator должны быть доступны следующие операции:
    for x in it:  # последовательный перебор всех элементов списка: x00, x10, x11, x20, ...
        print(x)
    it_iter = iter(it)
    x = next(it_iter)

Итератор должен перебирать элементы списка по указанной треугольной форме. Даже если итератору на вход будет передан
прямоугольная таблица (вложенный список), то ее перебор все равно должен осуществляться по треугольнику. Если же это
невозможно (из-за структуры списка), то естественным образом должна возникать ошибка IndexError: index out of range
(выход индекса за допустимый диапазон)."""

from functools import reduce


class TriangleListIterator:
    def __init__(self, lst):
        self.lst = lst
        self.deque = self._make_deque(lst)
        self.curr_el = None

    @staticmethod
    def _make_deque(lst):
        res = []
        count = 1
        try:
            for i in range(len(lst)):
                lst_1 = []
                for j in range(count):
                    lst_1.append(lst[i][j])
                count += 1
                res.append(lst_1)
            return reduce(lambda x, y: x + y, res, [])
        except:
            raise IndexError('выход индекса за допустимый диапазон')

    def __iter__(self):
        self.curr_el = -1
        return self

    def __next__(self):
        if self.curr_el < len(self.deque) - 1:
            self.curr_el += 1
            return self.deque[self.curr_el]
        else:
            raise StopIteration


lst = [['x00', 'x01', 'x02'],
       ['x10', 'x11'],
       ['x20', 'x21', 'x22', 'x23', 'x24'],
       ['x30', 'x31', 'x32', 'x33']]

it = TriangleListIterator(lst)
for x in it:  # последовательный перебор всех элементов списка: x00, x10, x11, x20, ...
    print(x)

it_iter = iter(it)
x = next(it_iter)