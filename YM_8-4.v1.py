"""
В задаче со складом мы реализуем меню, для взаимодействия. По сути - это прототип программы учета товара,
проверки наличия и перемещения. Пример меню: сколько на складе, сколько в подразделениях, добавить оргтехнику,
переместить в подразделение, выйти.

Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер,
ксерокс). В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
уникальные для каждого типа оргтехники.
"""

class Warehouse:
    data_of_equipment = {}

class Equipment:
    unit_equipment = 'шт'
    dividing_line = '___________________________'
    color_print_scan = 'цветной/черно-белый'

    def __init__(self, name_type, factory, model, year, articul, pce, color):
        self.name_type = name_type
        self.factory = factory
        self.model = model
        self.year = year
        self.articul = articul
        self.pce = pce
        self.color = color

    def __str__(self):
        return (f'КАРТОЧКА ТОВАРА\nНаименование: {self.name_type}\nПроизводитель: {self.factory}\n'
                f'Модель: {self.model}\nРежим работы: {Equipment.color_print_scan}\n'
                f'Цвет устройства: {self.color}\nГод выпуска: {self.year}\nАртикул: {self.articul}\n'
                f'Остаток на складе: {self.pce} {Equipment.unit_equipment}\n')

    def __add__(self, other):

    def def remuve


class Printer(Equipment):
    def __init__(self, name_type, factory, model, year, articul, pce, color, sposob_pechati, max_paper):
        super(Printer, self).__init__(name_type, factory, model, year, articul, pce, color)
        self.sposob_pechati = sposob_pechati
        self.max_paper = max_paper

    def __str__(self):
        return super(Printer, self).__str__() + f'Способ печати: {self.sposob_pechati}\n' \
                                                f'Формат бумаги: {self.max_paper}\n{Equipment.dividing_line}'


class Scaner(Equipment):
    def __init__(self, name_type, factory, model, year, articul, pce, color):
        super(Scaner, self).__init__(name_type, factory, model, year, articul, pce, color)

    def __str__(self):
        return super(Scaner, self).__str__() + f'{Equipment.dividing_line}'


class Xerox(Equipment):
    def __init__(self, name_type, factory, model, year, articul, pce, color, sposob_pechati, max_paper):
        super(Xerox, self).__init__(name_type, factory, model, year, articul, pce, color)
        self.sposob_pechati = sposob_pechati
        self.max_paper = max_paper

    def __str__(self):
        return super(Xerox, self).__str__() + f'Способ печати: {self.sposob_pechati}\n' \
                                              f'Формат бумаги: {self.max_paper}\n{Equipment.dividing_line}'


p = Printer('Принтер', 'HP', 'CW86', '2021', '45-89', '99', 'Black', 'LASER', 'A3')
print(p)

s = Scaner('Сканер', 'EPSON', 'YM897-18', '2020', '50-73', '5', 'White')
print(s)

x = Xerox('Ксерокс', 'Canon', 'CaXe91-02', '2021', '46-15a', '7', 'Black', 'Струйный', 'A4')
print(x)
