"""
Подвиг 6.
Объявите класс с именем ShopItem (товар), объекты которого создаются командой:
    item = ShopItem(name, weight, price)  - где name - название товара (строка); weight - вес товара
(число: целое или вещественное); price - цена товара (число: целое или вещественное).
Определите в этом классе магические методы:
    __hash__() - чтобы товары с одинаковым названием (без учета регистра), весом и ценой имели бы равные хэши;
    __eq__() - чтобы объекты с одинаковыми хэшами были равны.
Затем, из входного потока прочитайте строки командой:
    lst_in = list(map(str.strip, sys.stdin.readlines()))
Строки имеют следующий формат:
    название товара 1: вес_1 цена_1
    ...
    название товара N: вес_N цена_N

Например:
Системный блок: 1500 75890.56
Монитор Samsung: 2000 34000
Клавиатура: 200.44 545
Монитор Samsung: 2000 34000

Как видите, товары в этом списке могут совпадать.
Необходимо для всех этих строчек сформировать соответствующие объекты класса ShopItem и добавить в словарь с
именем shop_items. Ключами словаря должны выступать сами объекты, а значениями - список в формате:
    [item, total] - где item - объект класса ShopItem; total - общее количество одинаковых объектов (с одинаковыми
хэшами). Подумайте, как эффективно программно наполнять такой словарь, проходя по списку lst_in один раз.
"""


class ShopItem:
    def __init__(self, name: str, weight: (int, float), price: (int, float)):
        self.name = name
        self.weight = weight
        self.price = price

    def __hash__(self):
        return hash((self.name.lower(), self.weight, self.price))

    def __eq__(self, other):
        return self.name.lower() == other.name.lower(), self.weight == other.weight, self.price == other.price


lst_in = ['Системный блок: 1500 75890.56',
     'Монитор Samsung: 2000 34000',
     'Клавиатура: 200.44 545',
     'Монитор Samsung: 2000 34000']


shop_items = {}

for el in lst_in:
    name, values = el.split(':')
    weight, price = values.split()
    k = ShopItem(name, weight, price)
    if shop_items.get(k):
        shop_items[k][1] += 1
    shop_items[k] = shop_items.setdefault(k, [k, 1])

print(shop_items)

