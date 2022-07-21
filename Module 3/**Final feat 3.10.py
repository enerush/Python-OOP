"""
Техническое задание.
Необходимо объявить класс с именем TicTacToe (крестики-нолики) для управления игровым процессом. Объекты этого класса
будут создаваться командой:
game = TicTacToe()
В каждом объекте этого класса должен быть публичный атрибут:
pole - двумерный кортеж, размером 3x3.

Каждый элемент кортежа pole является объектом класса Cell:
    cell = Cell()
В объектах этого класса должно автоматически формироваться локальное свойство:
    value - текущее значение в ячейке: 0 - клетка свободна; 1 - стоит крестик; 2 - стоит нолик.
Также с объектами класса Cell должна выполняться функция:
    bool(cell) - возвращает True, если клетка свободна (value = 0) и False - в противном случае.
К каждой клетке игрового поля должен быть доступ через операторы:
    res = game[i, j] # получение значения из клетки с индексами i, j
    game[i, j] = value # запись нового значения в клетку с индексами i, j
Если индексы указаны неверно (не целые числа или числа, выходящие за диапазон [0; 2]), то следует генерировать
исключение командой:
    raise IndexError('некорректно указанные индексы')
Чтобы в программе не оперировать величинами: 0 - свободная клетка; 1 - крестики и 2 - нолики, в классе TicTacToe должны
быть три публичных атрибута (атрибуты класса):
    FREE_CELL = 0      # свободная клетка
    HUMAN_X = 1        # крестик (игрок - человек)
    COMPUTER_O = 2     # нолик (игрок - компьютер)
В самом классе TicTacToe должны быть объявлены следующие методы (как минимум):
    init() - инициализация игры (очистка игрового поля, возможно, еще какие-либо действия);
    show() - отображение текущего состояния игрового поля (как именно - на свое усмотрение);
    human_go() - реализация хода игрока (запрашивает координаты свободной клетки и ставит туда крестик);
    computer_go() - реализация хода компьютера (ставит случайным образом нолик в свободную клетку).
Также в классе TicTacToe должны быть следующие объекты-свойства (property):
    is_human_win - возвращает True, если победил человек, иначе - False;
    is_computer_win - возвращает True, если победил компьютер, иначе - False;
    is_draw - возвращает True, если ничья, иначе - False.

Наконец, с объектами класса TicTacToe должна выполняться функция:
    bool(game) - возвращает True, если игра не окончена (никто не победил и есть свободные клетки)
и False - в противном случае.
"""

from random import choice
from time import sleep


class Cell:
    def __init__(self):
        self.value = 0

    def __bool__(self):
        return self.value == 0


class TicTacToe:
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)

    def __init__(self):
        self.pole = [[Cell() for _ in range(3)] for _ in range(3)]
        self.winner = 0

    def __getitem__(self, item):
        """Геттер значения клетки по координатам"""
        i, j = item
        if type(i) != int or type(j) != int or not 0 <= i < 3 or not 0 <= i < 3:
            raise IndexError('Incorrect indices!')
        return self.pole[i][j].value

    def __setitem__(self, key, value):
        """Сеттер значения клетки по координатам"""
        i, j = key
        if type(i) != int or type(j) != int or not 0 <= i < 3 or not 0 <= i < 3:
            raise IndexError('Incorrect indices!')
        self.pole[i][j].value = value

    def __bool__(self):
        """Проверка окончена игра или нет"""
        return self.winner == 0

    def init(self):
        """Инициализация поля"""
        self.pole = [[Cell() for _ in range(3)] for _ in range(3)]
        self.winner = 0

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
        """Ход человека"""
        while True:
            try:
                i, j = map(int, input('Enter the coordinate (example: "1 2"): ').split())
            except:
                print('Incorrect indices! Try again...')
                continue

            if self[i, j] == 0:
                self[i, j] = self.HUMAN_X
                self._update_winner()
                break

    def computer_go(self):
        """Ход компьютера"""
        res = self._get_free_cells()
        choice(res).value = self.COMPUTER_O
        self._update_winner()

    def _check_pole_for_win(self, player):
        """Проверка поля на наличие победителя"""
        rows = any([all([x.value == player for x in row]) for row in self.pole])
        cols = any([all([self[i, j] == player for i in range(3)]) for j in range(3)])
        d1 = all([self[i, i] == player for i in range(3)])
        d2 = all([self[i, 2 - i] == player for i in range(3)])
        return any([rows, cols, d1, d2])

    def _update_winner(self):
        """Обновление атрибута winner"""
        human = self._check_pole_for_win(self.HUMAN_X)
        computer = self._check_pole_for_win(self.COMPUTER_O)

        if human and not computer:
            self.winner = 1
        elif computer and not human:
            self.winner = 2
        elif not human and not computer and bool(self._get_free_cells()):
            self.winner = 0
        else:
            self.winner = 3

    @property
    def is_human_win(self):
        return self.winner == 1

    @property
    def is_computer_win(self):
        return self.winner == 2

    @property
    def is_draw(self):
        return self.winner == 3

    def show(self):
        """Отрисовка поля в консоль"""
        for i in range(3):
            for j in range(3):
                if self[i, j] == 0:
                    print('-', end=' ')
                elif self[i, j] == 1:
                    print('X', end=' ')
                else:
                    print('O', end=' ')
            print()


game = TicTacToe()
game.init()
step_game = 0
while game:
    game.show()
    print()

    if step_game % 2 == 0:
        game.human_go()
        print('Your move:')
    else:
        print('Computer move:')
        sleep(1)
        game.computer_go()

    step_game += 1

game.show()

if game.is_human_win:
    print("Congratulations! You have won!")
elif game.is_computer_win:
    print("It will succeed, eventually!")
else:
    print("Nobody's.")