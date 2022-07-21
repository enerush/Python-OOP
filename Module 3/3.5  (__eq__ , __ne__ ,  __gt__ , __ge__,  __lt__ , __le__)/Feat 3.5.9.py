"""
Подвиг 9 (релакс).
Необходимо объявить класс Body (тело), объекты которого создаются командой:
    body = Body(name, ro, volume) - где name - название тела (строка); ro - плотность тела (число: вещественное или
целочисленное); volume - объем тела  (число: вещественное или целочисленное).
Для объектов класса Body должны быть реализованы операторы сравнения:
    body1 > body2  # True, если масса тела body1 больше массы тела body2
    body1 == body2 # True, если масса тела body1 равна массе тела body2
    body1 < 10     # True, если масса тела body1 меньше 10
    body2 == 5     # True, если масса тела body2 равна 5
Масса тела вычисляется по формуле:
    m = ro * volume
"""


class Body:
    def __init__(self, name: str, ro: (int, float), volume: (int, float)):
        self.name = name
        self.ro = ro
        self.volume = volume
        self.m = self.ro * self.volume

    def __eq__(self, other):
        other = other.m if type(other) is Body else other
        return self.m == other

    def __gt__(self, other):
        other = other.m if type(other) is Body else other
        return self.m > other

    def __lt__(self, other):
        other = other.m if type(other) is Body else other
        return self.m < other


body1 = Body('John', 1, 70)
body2 = Body('Emmy', 1, 50)

print(body1 > body2)   # True, если масса тела body1 больше массы тела body2
print(body1 == body2)  # True, если масса тела body1 равна массе тела body2
print(body1 < 10)      # True, если масса тела body1 меньше 10
print(body2 == 5)      # True, если масса тела body2 равна 5