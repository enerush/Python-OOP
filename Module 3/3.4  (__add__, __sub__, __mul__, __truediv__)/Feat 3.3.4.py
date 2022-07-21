class ObjList:
    def __init__(self, data):
        self.__data = data  # reference to a string of data
        self.__prev = None  # link to previous linked list object
        self.__next = None  #

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, prev):
        self.__prev = prev

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        self.__next = next


class LinkedList:
    head = None
    tail = None

    def add_obj(self, obj):
        """The method to add a new obj object of class ObjList to the end of a linked list"""
        if self.head is None:
            self.head = obj
            self.tail = obj
        else:
            self.tail.next = obj
            obj.prev = self.tail
            self.tail = obj

    def remove_obj(self, indx):
        """The method to remove object of class ObjList from linked list by index"""
        next = self.head
        count = 0
        prev = None

        while next is not None:
            if count == indx:
                if next == self.head:
                    self.head = next.next
                    next.next.prev = self.head

                elif next == self.tail:
                    next.prev.next = None
                    self.tail = next.prev

                else:
                    prev.next = next.next
                    next.prev = prev
            count += 1
            prev = next
            next = next.next

    def __len__(self):
        """The method returns the number of objects in the linked list"""
        lst = []
        next = self.head
        while next is not None:
            lst.append(next)
            next = next.next
        return len(lst)

    def __call__(self, indx, *args, **kwargs):
        """The method returns a string stored in an object of class ObjList located under the given index"""
        next = self.head
        count = 0

        while next is not None:
            if count == indx:
                return next.data

            count += 1
            next = next.next



linked_lst = LinkedList()
linked_lst.add_obj(ObjList("Sergey"))
linked_lst.add_obj(ObjList("Balakirev"))
linked_lst.add_obj(ObjList("Python"))
linked_lst.remove_obj(2)
linked_lst.add_obj(ObjList("Python ООП"))
n = len(linked_lst)  # n = 3
d = linked_lst(1)  # s = Balakirev