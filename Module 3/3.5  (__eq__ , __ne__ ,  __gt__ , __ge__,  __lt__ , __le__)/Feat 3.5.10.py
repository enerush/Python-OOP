"""Подвиг 10. Объявите в программе класс с именем Box (ящик), объекты которого должны создаваться командой:
    box = Box()
А сам класс иметь следующие методы:
    add_thing(self, obj) - добавление предмета obj (объект другого класса Thing) в ящик;
    get_things(self) - получение списка объектов ящика.
Для описания предметов необходимо объявить еще один класс Thing. Объекты этого класса должны создаваться командой:
    obj = Thing(name, mass)
где name - название предмета (строка); mass - масса предмета (число: целое или вещественное).
Объекты класса Thing должны поддерживать операторы сравнения:
    obj1 == obj2
    obj1 != obj2
Предметы считаются равными, если у них одинаковые названия name (без учета регистра) и массы mass.
Также объекты класса Box должны поддерживать аналогичные операторы сравнения:
    box1 == box2
    box1 != box2
Ящики считаются равными, если одинаковы их содержимое (для каждого объекта класса Thing одного ящика и можно найти
ровно один равный объект из второго ящика).
"""


class Box:
    def __init__(self):
        self.box = []

    def add_thing(self, obj):  # добавление предмета obj (объект другого класса Thing) в ящик
        self.box.append(obj)

    def get_things(self):  # получение списка объектов ящика
        return self.box

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        lst = self.box.copy()
        for el1 in other.box:
            for el2 in lst:
                if el1.name == el2.name and el1.mass == el2.mass:
                    lst.remove(el2)
        return True if len(lst) == 0 else False

    def __len__(self):
        return len(self.box)


class Thing:
    def __init__(self, name: str, mass: (int, float)):
        self.name = name
        self.mass = mass

    def __eq__(self, other):
        return self.mass == other.mass and self.name.lower() == other.name.lower()


b1 = Box()
b2 = Box()

b1.add_thing(Thing('мел', 100))
b1.add_thing(Thing('тряпка', 200))
b1.add_thing(Thing('доска', 2000))

b2.add_thing(Thing('тряпка', 200))
b2.add_thing(Thing('мел', 100))
b2.add_thing(Thing('доска', 2000))

res = b1 == b2 # True
