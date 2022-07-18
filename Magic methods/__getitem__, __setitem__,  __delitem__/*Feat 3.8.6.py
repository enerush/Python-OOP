"""
Подвиг 6.
Ранее вы уже создавали стек-подобную структуру, когда один объект ссылается на следующий и так по цепочке до последнего.
Для этого в программе объявлялись два класса:
    StackObj - для описания объектов стека;
    Stack - для управления стек-подобной структурой.

И, далее, объекты класса StackObj следовало создавать командой:
    obj = StackObj(data)
где data - это строка с некоторым содержимым объекта (данными). При этом каждый объект класса StackObj должен иметь
следующие локальные атрибуты:
    data - ссылка на строку с данными, указанными при создании объекта;
    next - ссылка на следующий объект класса StackObj (при создании объекта принимает значение None).

Класс Stack предполагается использовать следующим образом:
    st = Stack() # создание объекта стек-подобной структуры
В каждом объекте класса Stack должен быть локальный публичный атрибут:
    top - ссылка на первый объект стека (если стек пуст, то top = None).
А в самом классе Stack следующие методы:
    push(self, obj) - добавление объекта класса StackObj в конец стека;
    pop(self) - извлечение последнего объекта с его удалением из стека;
Дополнительно в классе Stack нужно объявить магические методы для обращения к объекту стека по его индексу, например:
    obj_top = st[0] # получение первого объекта
    obj = st[4] # получение 5-го объекта стека
    st[2] = StackObj("obj3") # замена прежнего (3-го) объекта стека на новый
Если индекс не целое число или число меньше нуля или больше числа объектов в стеке, то должно генерироваться исключение
командой:
    raise IndexError('неверный индекс')"""


class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def next(self):
        if self is None:
            return
        return self.__next

    @next.setter
    def next(self, nxt):
        if self.__check_next(nxt):
            self.__next = nxt

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @classmethod
    def __check_next(cls, nxt):
        if type(nxt) == StackObj or nxt is None:
            return True
        return False


class Stack:
    def __init__(self):
        self.top = None
        self.last = None
        self.len = 0

    def push(self, obj):
        if self.top is None:
            self.top = obj
            self.len += 1
        else:
            self.last.next = obj
            self.len += 1
        self.last = obj

    def pop(self):
        obj = self.top

        if obj.next is None:
            self.top = None
            return self.top

        prev = None
        while obj != self.last:
            prev = obj
            obj = obj.next

        prev.next = None
        res = self.last
        self.last = prev
        return res

    def __getitem__(self, item):
        if type(item) is not int or not 0 <= item < self.len:
            raise IndexError('неверный индекс')
        el = self.top
        if item == 0:
            return self.top

        for _ in range(item):
            el = el.next
        return el

    def __setitem__(self, key, value):
        if type(key) is not int or not 0 <= key < self.len:
            raise IndexError('неверный индекс')
        el = self.top
        if key == 0:
            self.top.data = value
        else:
            for _ in range(key):
                el = el.next
            el.data = value.data


st = Stack()
st.push(StackObj("obj0"))
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st[1] = StackObj("new obj1")
print(st[1].data)  # new obj1
res = st[3]  # исключение IndexError
