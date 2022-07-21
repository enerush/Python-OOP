"""
Подвиг 5.
Объявите в программе следующие классы без содержимого (используйте оператор pass):
    Protists, Plants, Animals, Mosses, Flowering, Worms, Mammals, Human, Monkeys
и постройте схему наследования в соответствии со следующей иерархией древа жизни:

Затем, объявите в программе классы:
    Monkey - наследуется от Monkeys и служит для описания обезьян;
    Person - наследуется от Human и служит для описания человека;
    Flower - наследуется от Flowering и служит для описания цветка;
    Worm - наследуется от Worms и служит для описания червей.

Объекты этих классов должны создаваться командами:
    obj = Monkey(name, weight, old)
    obj = Person(name, weight, old)
    obj = Flower(name, weight, old)
    obj = Worm(name, weight, old)
где name - наименование (или имя) объекта (строка); weight - вес (вещественное число); old - возраст (целое число).
В каждом объекте любого из этих классов должны создаваться соответствующие атрибуты: name, weight, old.
Затем, используя функции isinstance() и генератор списков (List comprehensions), сформируйте следующие списки из
указанных объектов:
lst_animals - все объекты, относящиеся к животным (Animals);
lst_plants - все объекты, относящиеся к растениям (Plants);
lst_mammals - все объекты, относящиеся к млекопитающим (Mammals)."""


class Protists:
    def __init__(self, name, weight, old):
        self.name = name
        self.weight = weight
        self.old = old


class Plants(Protists):
    pass


class Animals(Protists):
    pass


class Mosses(Plants):
    pass


class Flowering(Plants):
    pass


class Worms(Animals):
    pass


class Mammals(Animals):
    pass


class Human(Animals):
    pass


class Monkeys(Animals):
    pass


class Monkey(Monkeys):
    def __init__(self, *args):
        super().__init__(*args)


class Person(Human):
    def __init__(self, *args):
        super().__init__(*args)


class Flower(Flowering):
    def __init__(self, *args):
        super().__init__(*args)


class Worm(Worms):
    def __init__(self, *args):
        super().__init__(*args)


m1 = Monkey("мартышка", 30.4, 7)
m2 = Monkey("шимпанзе", 24.6, 8)
p1 = Person("Балакирев", 88, 34)
p2 = Person("Верховный жрец", 67.5, 45)
f1 = Flower("Тюльпан", 0.2, 1)
f2 = Flower("Роза", 0.1, 2)
w1 = Worm("червь", 0.01, 1)
w2 = Worm("червь 2", 0.02, 1)
lst_objs = [m1, m2, p1, p2, f1, f2, w1, w2]

lst_animals = [item for item in lst_objs if isinstance(item, Animals)]
lst_plants = [item for item in lst_objs if isinstance(item, Plants)]
lst_mammals = [item for item in lst_objs if isinstance(item, Mammals)]

