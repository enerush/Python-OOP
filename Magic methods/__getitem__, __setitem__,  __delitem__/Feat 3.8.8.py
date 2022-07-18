"""
Подвиг 8.
Вам нужно реализовать в программе игровое поле для игры "Крестики-нолики". Для этого требуется объявить
класс TicTacToe (крестики-нолики), объекты которого создаются командой:
    game = TicTacToe()

Каждый объект game должен иметь публичный атрибут:
    pole - игровое поле: кортеж размером 3х3 с объектами класса Cell.

Каждая клетка игрового поля представляется объектом класса Cell и создается командой:
    cell = Cell()

Объекты класса Cell должны иметь следующие публичные локальные атрибуты:
    is_free - True, если клетка свободна; False в противном случае;
    value - значение поля: 1 - крестик; 2 - нолик (по умолчанию 0).
Также с каждым объектом класса Cell должна работать функция:
    bool(cell)
- которая возвращает True, если клетка свободна (cell.is_free=True) и False в противном случае.

Класс TicTacToe должен иметь следующий метод:
    clear() - очистка игрового поля (все клетки заполняются нулями и переводятся в закрытое состояние);

А объекты этого класса должны иметь следующую функциональность (обращение по индексам):
    game[0, 0] = 1 # установка нового значения, если поле закрыто
    res = game[1, 1] # получение значения центральной ячейки поля (возвращается число)

Если указываются некорректные индексы, то должно генерироваться исключение командой:
    raise IndexError('неверный индекс клетки')
Если идет попытка присвоить новое значение в открытую клетку поля, то генерировать исключение:
    raise ValueError('клетка уже занята')

Также должны быть реализованы следующие срезы при обращении к клеткам игрового поля:
    slice_1 = game[:, indx] # выбираются все элементы (кортеж) столбца с индексом indx
    slice_2 = game[indx, :] # выбираются все элементы (кортеж) строки с индексом indx


P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.

P.P.S. При передаче среза в магических методах __setitem__() и __getitem__() параметр индекса становится объектом класса
 slice. Его можно указывать непосредственно в квадратных скобках упорядоченных коллекций (списков, кортежей и т.п.).
 """


class Cell:
    def __init__(self):
        self.is_free = True
        self.value = 0

    def __bool__(self):
        return bool(self.is_free)


class TicTacToe:
    def __init__(self):
        self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(3))

    def clear(self):
        for i in range(3):
            for j in range(3):
                self.pole[i][j].is_true = True
                self.pole[i][j].value = 0

    def __getitem__(self, item):
        i, j = item
        if type(i) is int and type(j) is int:
            return self.pole[i][j].value
        else:
            if type(i) is int:
                return self.pole[i][0].value, self.pole[i][1].value, self.pole[i][2].value
            if type(j) is int:
                return self.pole[0][j].value, self.pole[1][j].value, self.pole[2][j].value

    def __setitem__(self, key, value):
        i, j = key
        if i not in range(0, 4) or j not in range(0, 4):
            raise IndexError('неверный индекс клетки')
        if not self.pole[i][j]:
            raise ValueError('клетка уже занята')
        self.pole[i][j].value = value


game = TicTacToe()
game.clear()
game[0, 0] = 1
game[1, 0] = 2
# формируется поле:
# 1 0 0
# 2 0 0
# 0 0 0

#game[3, 2] = 2 # генерируется исключение IndexError
if game[0, 0] == 0:
    game[0, 0] = 2
v1 = game[0, :]  # 1, 0, 0
v2 = game[:, 0]  # 1, 2, 0
print(game[0, :])  # 1, 0, 0
print(game[:, 0])  # 1, 2, 0

for i in range(3):
    for j in range(3):
        print(game.pole[i][j].value, end=' ')
    print()