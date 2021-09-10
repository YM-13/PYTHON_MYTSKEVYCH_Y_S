"""
Реализовать базовый класс Worker (работник).
● определить атрибуты: name, surname, position (должность), income (доход);
● последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
● создать класс Position (должность) на базе класса Worker;
● в классе Position реализовать методы получения полного имени сотрудника
(get_full_name) и дохода с учётом премии (get_total_income);
● проверить работу примера на реальных данных: создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров.
"""


class Worker:

    def __init__(self, n, s, p, d):
        self.name = n
        self.surname = s
        self.position = p
        self._income = d.values()


class Position(Worker):

    def get_full_name(self):
        print(f'Full Name of worker: {self.name} {self.surname}, his position in company: {self.position}')

    def get_total_income(self):
        print(f'His wage including bonus is {sum(self._income)}')


person_1 = Position("Igor", "Polakov", "Manager", {"wage": 1500, "bonus": 500})
person_1.get_full_name()
person_1.get_total_income()
