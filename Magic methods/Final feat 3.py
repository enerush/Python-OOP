from random import choice


class Cell:
    def __init__(self):
        self.is_free = True
        self.value = 0

    def __bool__(self):
        return bool(self.is_free)


class TicTacToe:
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)

    def __init__(self):
        self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(3))

    def show(self):
        for i in range(3):
            for j in range(3):
                print(self.pole[i][j], end=' ')
            print()

    def init(self):
        for i in range(3):
            for j in range(3):
                self.pole[i][j].is_true = True
                self.pole[i][j].value = 0

    @staticmethod
    def _check_coord(i, j):
        if 0 <= i < 3 and 0 <= i < 3:
            return True
        return False

    def _get_free_cells(self):
        res = []
        for i in range(3):
            for j in range(3):
                if self.pole[i][j].value == self.FREE_CELL:
                    res.append(self.pole[i][j])
        return res

    def human_go(self):
        x = None
        while True:
            i, j = input('Sent coords, what do you prefer to mark')
            if self._check_coord(i, j) and self.pole[i][j].value == self.FREE_CELL:
                self.pole[i][j].value = self.HUMAN_X
                break

    def computer_go(self):
        res = self._get_free_cells()
        choice(res).value = self.COMPUTER_O

    def __getitem__(self, item):
        i, j = item
        if type(i) != int or type(j) != int or not 0 <= i < 3 or not 0 <= i < 3:
            raise IndexError('некорректно указанные индексы')
        return self.pole[i][j]

    def __setitem__(self, key, value):
        i, j = key
        if type(i) != int or type(j) != int or not 0 <= i < 3 or not 0 <= i < 3:
            raise IndexError('некорректно указанные индексы')
        self.pole[i][j] = value

    def __bool__(self):
        if self._get_free_cells():
            return True
        return False


game = TicTacToe()
game.init()
step_game = 0
while game:
    game.show()

    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()

    step_game += 1


game.show()

if game.is_human_win:
    print("Поздравляем! Вы победили!")
elif game.is_computer_win:
    print("Все получится, со временем")
else:
    print("Ничья.")