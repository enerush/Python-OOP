"""
Подвиг 7.
Используя информацию о модуле abc из предыдущего подвига 6, объявите базовый класс с именем StackInterface со
следующими абстрактными методами:
    def push_back(self, obj) - добавление объекта в конец стека;
    def pop_back(self) - удаление последнего объекта из стека.

На основе этого класса объявите дочерний класс с именем Stack. Объекты этого класса должны создаваться командой:
    st = Stack()
и в каждом объекте этого класса должен формироваться локальный атрибут:
    _top - ссылка на первый объект стека (для пустого стека _top = None).

В самом классе Stack переопределить абстрактные методы базового класса:
    def push_back(self, obj) - добавление объекта в конец стека;
    def pop_back(self) - удаление последнего объекта из стека.

Сами объекты стека должны определяться классом StackObj и создаваться командой:
    obj = StackObj(data)
где data - информация, хранящаяся в объекте (строка). В каждом объекте класса StackObj должны автоматически формироваться атрибуты:
    _data - информация, хранящаяся в объекте (строка);
    _next - ссылка на следующий объект стека (если следующий отсутствует, то _next = None).

P.S. В программе требуется объявить только классы. На экран выводить ничего не нужно.
"""


from abc import ABC, abstractmethod


class StackInterface(ABC):

    @abstractmethod
    def push_back(self, obj):
        pass

    @abstractmethod
    def pop_back(self):
        pass


class Stack(StackInterface):

    def __init__(self):
        self._top = None
        self._last = None

    def push_back(self, obj):
        if self._top is None:
            self._top = obj
            print(f"add - {obj._data}")
            self._last = obj
        else:
            self._last._next = obj
            obj._prev = self._last
            print(f"add - {obj._data}")
            self._last = obj

    def pop_back(self):
        if self._top is None:
            return None

        if self._last == self._top:
            res = self._top
            print(f'remove = {res._data}')
            self._top = None
            return res._data

        self._last._prev._next = None
        res = self._last
        self._last = self._last._prev
        print(f'remove = {res._data}')
        return res._data


class StackObj:
    def __init__(self, data):
        self._data = data
        self._next = None
        self.prev = None


st = Stack()
st.push_back(StackObj("obj 1"))
st.push_back(StackObj("obj 2"))
st.push_back(StackObj("obj 3"))
st.pop_back()
st.pop_back()
st.pop_back()


