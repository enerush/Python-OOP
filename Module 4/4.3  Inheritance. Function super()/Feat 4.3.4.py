"""
Подвиг 4.
Создается программа по учету склада. Каждый предмет на складе должен описываться базовым классом Thing.
Объекты этого класса создаются командой:
    th1 = Thing(name, weight)
где name - наименование предмета (строка); weight - вес предмета (вещественное число).

Для описания каждого конкретного вида предметов, создаются дочерние классы (на основе базового Thing):
    ArtObject - для представления арт-объектов;
    Computer - для системных блоков компьютеров;
    Auto - для автомобилей.

Объекты этих классов создаются командами:
    obj = ArtObject(name, weight, author, date)  # author - автор (строка); date - дата создания (строка)
    obj = Computer(name, weight, memory, cpu)    # memory - размер памяти (целое число); cpu - тип процессора (строка)
    obj = Auto(name, weight, dims)               # dims - габариты, кортеж (width, length, height) - вещественные или целые числа

На основе класса Auto создаются дочерние классы Mercedes и Toyota, объекты которых определяются командами:
    auto1 = Mercedes(name, weight, dims, model, old) # model - модель (строка); old - время использования, в годах (целое число)
    auto2 = Toyota(name, weight, dims, model, wheel) # model - модель (строка); wheel - тип руля: True - леворульный, False - праворульный
Во всех объектах классов должны создаваться соответствующие локальные атрибуты: name, weight и т.д.

Инициализация атрибутов должна выполняться в соответствующих классах (не должно быть дублирования кода).
"""


class Thing:
    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight


class ArtObject(Thing):
    def __init__(self, name: str, weight: float, author: str, date: str):
        super().__init__(name, weight)
        self.author = author
        self.date = date


class Computer(Thing):
    def __init__(self, name: str, weight: float, memory: int, cpu: str):
        super().__init__(name, weight)
        self.memory = memory
        self.cpu = cpu


class Auto(Thing):
    def __init__(self, name: str, weight: float, dims: tuple):
        super().__init__(name, weight)
        self.dims = dims


class Mercedes(Auto):
    def __init__(self, name: str, weight: float, dims: tuple, model, old: int):
        super().__init__(name, weight, dims)
        self.model = model
        self.old = old


class Toyota(Auto):
    def __init__(self, name: str, weight: float, dims: tuple, model: str, wheel: bool):
        super().__init__(name, weight, dims)
        self.model = model
        self.wheel = wheel
