"""
Подвиг 8.
Вы несколько раз уже делали стек-подобную структуру, когда объекты последовательно связаны между собой:
Доведем ее функционал до конца. Для этого, по прежнему, нужно объявить классы:
Stack - для представления стека в целом;
StackObj - для представления отдельных объектов стека.
В классе Stack должны быть методы:
push_back(obj) - для добавления нового объекта obj в конец стека;
push_front(obj) - для добавления нового объекта obj в начало стека.
В каждом объекте класса Stack должен быть публичный атрибут:
top - ссылка на первый объект стека (при пустом стеке top = None).

Объекты класса StackObj создаются командой:
obj = StackObj(data) - где data - данные, хранящиеся в объекте стека (строка).
Также в каждом объекте класса StackObj должны быть публичные атрибуты:
data - ссылка на данные объекта;
next - ссылка на следующий объект стека (если его нет, то next = None).

Наконец, с объектами класса Stack должны выполняться следующие команды:
st = Stack()
st[indx] = value # замена прежних данных на новые по порядковому индексу (indx); отсчет начинается с нуля
data = st[indx]  # получение данных из объекта стека по индексу
n = len(st) # получение общего числа объектов стека
for obj in st: # перебор объектов стека (с начала и до конца)
    print(obj.data)  # отображение данных в консоль

При работе с индексами (indx), нужно проверять их корректность. Должно быть целое число от 0 до N-1,
где N - число объектов в стеке. Иначе, генерировать исключение командой:
raise IndexError('неверный индекс')
"""


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

    def __len__(self):
        return self.len

    def push_back(self, obj):
        if self.top is None:
            self.top = obj
            self.len += 1
        else:
            self.last.next = obj
            self.len += 1
        self.last = obj

    def push_front(self, obj):
        if self.top is None:
            self.top = obj
            self.len += 1
        else:
            obj.next = self.top
            self.top = obj
            self.len += 1

    def __getitem__(self, item):
        if type(item) is not int or not 0 <= item < self.len:
            raise IndexError('неверный индекс')
        el = self.top
        if item == 0:
            return self.top.data

        for _ in range(item):
            el = el.next
        return el.data

    def __setitem__(self, key, value):
        if type(key) is not int or not 0 <= key < self.len:
            raise IndexError('неверный индекс')
        el = self.top
        if key == 0:
            self.top.data = value
        else:
            for _ in range(key):
                el = el.next
            el.data = value

    def __iter__(self):
        self.curr_el = self.top
        return self

    def __next__(self):
        if self.curr_el is None:
            raise StopIteration
        res = self.curr_el
        self.curr_el = self.curr_el.next
        return res


st = Stack()
st.push_back(StackObj("obj0"))
st.push_back(StackObj("obj1"))
st.push_front(StackObj("obj2"))

st[2] = 'new data'        # замена прежних данных на новые по порядковому индексу (indx); отсчет начинается с нуля
data = st[0]              # получение данных из объекта стека по индексу
print(len(st))            # получение общего числа объектов стека
for obj in st:            # перебор объектов стека (с начала и до конца)
    print(obj.data)       # отображение данных в консоль