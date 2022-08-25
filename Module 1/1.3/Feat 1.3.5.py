"""
Подвиг 5.
Объявите пустой класс с именем Car. С помощью функции setattr() добавьте в этот класс атрибуты:

model: "Тойота"
color: "Розовый"
number: "П111УУ77"
Выведите на экран значение атрибута color, используя словарь __dict__ класса Car.
"""


class Car:
    pass


d = {
    'model': "Тойота",
    'color': "Розовый",
    'number': "О111АА77"
}
[setattr(Car, k, v) for k, v in d.items()]

print(Car.__dict__['color'])