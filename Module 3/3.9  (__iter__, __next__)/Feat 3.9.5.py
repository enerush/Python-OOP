"""
Подвиг 5.
Объявите в программе класс Person, объекты которого создаются командой:
    p = Person(fio, job, old, salary, year_job)
- где fio - ФИО сотрудника (строка); job - наименование должности (строка); old - возраст (целое число);
salary - зарплата (число: целое или вещественное); year_job - непрерывный стаж на указанном месте работы (целое число).
В каждом объекте класса Person автоматически должны создаваться локальные атрибуты с такими же именами: fio, job, old,
salary, year_job и соответствующими значениями.
Также с объектами класса Person должны поддерживаться следующие команды:
    data = p[indx] # получение данных по порядковому номеру (indx) атрибута (порядок: fio, job, old, salary, year_job
                     и начинается с нуля)
    p[indx] = value # запись в поле с указанным индексом (indx) нового значения value
    for v in p: # перебор всех атрибутов объекта в порядке: fio, job, old, salary, year_job
        print(v)

При работе с индексами, проверить корректность значения indx. Оно должно быть целым числом в диапазоне [0; 4].
Иначе, генерировать исключение командой:
    raise IndexError('неверный индекс')
"""


class Person:
    def __init__(self, fio: str, job: str, old: int, salary: (int, float), year_job: int):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job
        self.lst = [fio, job, old, salary, year_job]
        self.len_lst = len(self.lst)
        self.iter_indx = -1

    def _check_idx(self, indx):
        if type(indx) is not int or not (-self.len_lst <= indx < self.len_lst):
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self._check_idx(item)
        return self.lst[item]

    def __setitem__(self, key, value):
        self._check_idx(key)
        self.lst[key] = value

    def __iter__(self):
        self.iter_indx = -1
        return self

    def __next__(self):
        if self.iter_indx < len(self.lst) - 1:
            self.iter_indx += 1
            return self.lst[self.iter_indx]
        else:
            raise StopIteration


pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
pers[0] = 'Балакирев С.М.'
for v in pers:
    print(v)
pers[5] = 123  # IndexError