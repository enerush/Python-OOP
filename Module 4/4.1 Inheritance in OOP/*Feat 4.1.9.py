"""
Большой подвиг 9.
Используя механизм наследования, вам поручено разработать функционал по построению моделей нейронных сетей.
Базовый класс Layer имеет локальный атрибут next_layer, который ссылается на следующий объект слоя нейронной сети
(объект класса Layer или любого объекта дочерних классов). У последнего слоя значение next_layer = None.
Создавать последовательность слоев предполагается командами:
    first_layer = Layer()
    next_layer = first_layer(Layer())
    next_layer = next_layer(Layer())
    ...

То есть, сначала создается объект first_layer класса Layer, а затем он вызывается как функция для образования связки со
следующим слоем. При этом возвращается ссылка на следующий слой и переменная next_layer ссылается уже на этот следующий
слой нейронной сети. И так можно создавать столько слоев, сколько необходимо.
В каждом объекте класса Layer также должен формироваться локальный атрибут:
    name = 'Layer'
Но сам по себе класс Layer образует только связи между слоями. Никакой другой функциональности он не несет. Чтобы это
исправить, в программе нужно объявить еще два дочерних класса:
    Input - формирование входного слоя нейронной сети;
    Dense - формирование полносвязного слоя нейронной сети.

Конечно, создавать нейронную сеть мы не будем. Поэтому, в классе Input нужно лишь прописать инициализатор так, чтобы его
объекты создавались следующим образом:
    inp = Input(inputs)
где inputs - общее число входов (целое число). Также в объектах класса Input должен автоматически формироваться атрибут:
    name = 'Input'  (Не забывайте при этом, вызывать инициализатор базового класса Layer).

Объекты второго дочернего класса Dense предполагается создавать командой:
    dense = Dense(inputs, outputs, activation)
где inputs - число входов в слой; outputs - число выходов слоя (целые числа); activation - функция активации (строка,
например: 'linear', 'relu', 'sigmoid'). И в каждом объекте класса Dense также должен автоматически формироваться атрибут:
    name = 'Dense'
"""


class Layer:
    def __init__(self, name='Layer'):
        self.name = name
        self.next_layer = None  # ссылка на следующий объект слоя нейронной сети

    def __call__(self, obj):
        self.next_layer = obj
        return obj


class Input(Layer):
    """Формирование входного слоя нейронной сети"""

    def __init__(self, inputs):
        super().__init__('Input')
        self.inputs = inputs


class Dense(Layer):
    """Формирование полносвязного слоя нейронной сети"""

    def __init__(self, inputs: int, outputs: int, activation: str):
        super().__init__('Dense')
        self.inputs = inputs
        self.outputs = outputs
        self.activation = activation


class NetworkIterator:
    def __init__(self, network):
        self.network = network

    def __iter__(self):
        obj = self.network
        while obj:
            yield obj
            obj = obj.next_layer


network = Input(128)
layer = network(Dense(network.inputs, 1024, 'linear'))
layer = layer(Dense(layer.inputs, 10, 'softmax'))

for x in NetworkIterator(network):
    print(x.name)
