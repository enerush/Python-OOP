"""
Подвиг 2.
Объявите класс Record (запись), который описывает одну произвольную запись из БД.
Объекты этого класса создаются командой:
    r = Record(field_name1=value1,... , field_nameN=valueN)
где field_nameX - наименование поля БД; valueX - значение поля из БД.
В каждом объекте класса Record должны автоматически создаваться локальные публичные атрибуты по именам полей
(field_name1,... , field_nameN) с соответствующими значениями. Например:
    r = Record(pk=1, title='Python ООП', author='Балакирев')
В объекте r появляются атрибуты:
    r.pk # 1
    r.title # Python ООП
    r.author # Балакирев

Также необходимо обеспечить доступ к этим полям (чтение/запись) через индексы следующим образом:
    r[0] = 2 # доступ к полю pk
    r[1] = 'Супер курс по ООП' # доступ к полю title
    r[2] = 'Балакирев С.М.' # доступ к полю author
    print(r[1]) # Супер курс по ООП
    r[3] # генерируется исключение IndexError
Если указывается неверный индекс (не целое число или некорректное целое число), то должно генерироваться исключение командой:
    raise IndexError('неверный индекс поля')

"""


class Record:
    def __init__(self, *args, **kwargs):
        self.__dict__ = kwargs
        self.lst_key = [i for i in self.__dict__.keys()]

    def __setitem__(self, key, value):
        if type(key) is not int or key >= len(self.__dict__) or key < 0:
            raise IndexError('неверный индекс поля')

        indx = self.lst_key[key]
        self.__dict__[indx] = value

    def __getitem__(self, item):
        if type(item) is not int or item >= len(self.__dict__) or item < 0:
            raise IndexError('неверный индекс поля')

        key = self.lst_key[item]
        return self.__dict__[key]


r = Record(pk=1, title='Python ООП', author='Балакирев')
r[0] = 2  # доступ к полю pk
r[1] = 'Супер курс по ООП'  # доступ к полю title
r[2] = 'Балакирев С.М.'  # доступ к полю author
print(r.__dict__)
print(r[1])  # Супер курс по ООП
r[3]  # генерируется исключение IndexError