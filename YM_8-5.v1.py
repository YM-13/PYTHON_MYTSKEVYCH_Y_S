"""
Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём
оргтехники на склад и передачу в определённое подразделение компании. Для хранения
данных о наименовании и количестве единиц оргтехники, а также других данных, можно
использовать любую подходящую структуру (например, словарь).
"""

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

    def __init__(self, name_type, factory, model, year, articul, pce, color, type_of_print=(), max_paper_size=()):
        self.name_type = name_type
        self.factory = factory
        self.model = model
        self.year = year
        self.articul = articul
        self.pce = pce
        self.color = color
        self.type_of_print = type_of_print
        self.max_paper_size = max_paper_size

    def add(self):
        d = dict.fromkeys(['Наименование', 'Производитель', 'Модель', 'Режим работы', 'Цвет устройства',
                           'Год выпуска', 'Артикул', 'Остаток на складе'],
                          [self.name_type, self.factory, self.model, Equipment.color_print_scan,
                           self.color, self.year,self.articul,self.pce])

        # Warehouse.data_of_equipment = {'Наименование': self.name_type,
        #                                'Производитель': self.factory,
        #                                'Модель': self.model,
        #                                'Режим работы': Equipment.color_print_scan,
        #                                'Цвет устройства': self.color,
        #                                'Год выпуска': self.year,
        #                                'Артикул': self.articul,
        #                                'Остаток на складе': self.pce
        #                                }
        return d

    def remove(self):
        pass

    def __str__(self):
        my_list = []
        for x, y in Warehouse.data_of_equipment:
            my_list.append(zip[x, y])
        my_str = (" ".join(my_list))
        return my_str#(f'КАРТОЧКА ТОВАРА\nНаименование: {self.name_type}\nПроизводитель: {self.factory}\n'
                # f'Модель: {self.model}\nРежим работы: {Equipment.color_print_scan}\n'
                # f'Цвет устройства: {self.color}\nГод выпуска: {self.year}\nАртикул: {self.articul}\n'
                # f'Остаток на складе: {self.pce} {Equipment.unit_equipment}\n')


class Printer(Equipment):

    def __init__(self, name_type, factory, model, year, articul, pce, color, type_of_print, max_paper_size):
        super(Printer, self).__init__(name_type, factory, model, year, articul, pce, color)
        self.type_of_print = type_of_print
        self.max_paper_size = max_paper_size

    # def __str__(self):
    #     return super(Printer, self).__str__() + f'Способ печати: {self.type_of_print}\n' \
    #                                             f'Формат бумаги: {self.max_paper_size}\n{Equipment.dividing_line}'


#class Scaner(Equipment):
    # def __init__(self, name_type, factory, model, year, articul, pce, color):
    #     super(Scaner, self).__init__(name_type, factory, model, year, articul, pce, color)
    #
    # def __str__(self):
    #     return super(Scaner, self).__str__() + f'{Equipment.dividing_line}'


# class Xerox(Equipment):
#     def __init__(self, name_type, factory, model, year, articul, pce, color, type_of_print, max_paper_size):
#         super(Xerox, self).__init__(name_type, factory, model, year, articul, pce, color)
#         self.type_of_print = type_of_print
#         self.max_paper_size = max_paper_size
#
#     def __str__(self):
#         return super(Xerox, self).__str__() + f'Способ печати: {self.type_of_print}\n' \
#                                               f'Формат бумаги: {self.max_paper_size}\n{Equipment.dividing_line}'


p = Printer('Принтер', 'HP', 'CW86', '2021', '45-89', '99', 'Black', 'LASER', 'A3')
p.add()
print(p)
print(p.add())

# s = Scaner('Сканер', 'EPSON', 'YM897-18', '2020', '50-73', '5', 'White')
# print(s)
#
# x = Xerox('Ксерокс', 'Canon', 'CaXe91-02', '2021', '46-15a', '7', 'Black', 'Струйный', 'A4')
# print(x)



# class Orgtehnika:
#
#     ci_orgteh = 'шт'
#     n_podcherc = '___________________________'
#     work_color = 'цветной/черно-белый'
#
#     def __init__(self, name_type, factory, model, year, articul, pce, color):
#         self.name_type = name_type
#         self.factory = factory
#         self.model = model
#         self.year = year
#         self.articul = articul
#         self.pce = pce
#         #        self.max_format = max_format
#         self.color = color
#
#     @classmethod
#     def derezer(cls, ):
#         gad_info = input('Накладная поставщика: \nНаименование: \nПроизводитель: \n')
#         raspred_dict = dict.fromkeys(['a', 'b', 'c'], gad_info)
#         a = raspred_dict['a']
#         if a == 1:
#             Printer.printer_dict[a1] = a
#
#
#
#     def carta_tovara(self):
#         print(f'КАРТОЧКА ТОВАРА\nНаименование: {self.name_type}\nПроизводитель: {self.factory}\n'
#               f'Модель: {self.model}\nРежим работы: {Orgtehnika.work_color}\n'
#               f'Цвет устройства: {self.color}\nГод выпуска: {self.year}\nАртикул: {self.articul}\n'
#               f'Остаток на складе: {self.pce} {Orgtehnika.ci_orgteh}\n{Orgtehnika.n_podcherc}')
#
#
# class Printer(Orgtehnika):
#     def __init__(self, name_type, factory, model, year, articul, pce, color):
#         Orgtehnika.__init__(self, name_type, factory, model, year, articul, pce, color)
#
#     printer_dict = {'a1', 'b', 'c'}
#
#     def carta_tovara(self, sposob_pechati, max_paper):  # sposob_pechati
#         self.sposob_pechati = sposob_pechati
#         self.max_paper = max_paper
#         return (f'КАРТОЧКА ТОВАРА\nНаименование: {self.name_type}\nПроизводитель: {self.factory}\n'
#                 f'Способ печати: {self.sposob_pechati}\nМодель: {self.model}\nРежим работы: {Orgtehnika.work_color}\n'
#                 f'Формат бумаги: {self.max_paper}\nЦвет устройства: {self.color}\nГод выпуска: {self.year}\nАртикул: {self.articul}\n'
#                 f'Остаток на складе: {self.pce} {Orgtehnika.ci_orgteh}\n{Orgtehnika.n_podcherc}')
#
#
# class Scaner(Orgtehnika):
#     def __init__(self, name_type, factory, model, year, articul, pce, color):
#         Orgtehnika.__init__(self, name_type, factory, model, year, articul, pce, color)
#
#     scaner_dict = {}
#
#     def carta_tovara(self, tip_scanera, max_doc_format):
#         self.tip_scanera = tip_scanera
#         self.max_doc_format = max_doc_format
#         return (f'КАРТОЧКА ТОВАРА\nНаименование: {self.name_type}\nПроизводитель: {self.factory}\n'
#                 f'Тип сканера: {self.tip_scanera}\nМодель: {self.model}\nРежим работы: {Orgtehnika.work_color}\n'
#                 f'Формат документа: {self.max_doc_format}\nЦвет устройства: {self.color}\nГод выпуска: {self.year}\nАртикул: {self.articul}\n'
#                 f'Остаток на складе: {self.pce} {Orgtehnika.ci_orgteh}\n{Orgtehnika.n_podcherc}')
#
#
# class Xerox(Orgtehnika):
#     def __init__(self, name_type, factory, model, year, articul, pce, color):
#         Orgtehnika.__init__(self, name_type, factory, model, year, articul, pce, color)
#
#     xero_dict = {}
#
#     def carta_tovara(self, sposob_pechati, max_paper):  # sposob_pechati
#         self.sposob_pechati = sposob_pechati
#         self.max_paper = max_paper
#         return (f'КАРТОЧКА ТОВАРА\nНаименование: {self.name_type}\nПроизводитель: {self.factory}\n'
#                 f'Способ печати: {self.sposob_pechati}\nМодель: {self.model}\nРежим работы: {Orgtehnika.work_color}\n'
#                 f'Формат документа: {self.max_paper}\nЦвет устройства: {self.color}\nГод выпуска: {self.year}\nАртикул: {self.articul}\n'
#                 f'Остаток на складе: {self.pce} {Orgtehnika.ci_orgteh}\n{Orgtehnika.n_podcherc}')
#
# Orgtehnika.derezer()
# prin_1 = Printer('Принтер', 'HP', 'CW86', '2021', '45-89', '99', 'Black')
# print(prin_1.carta_tovara('LASER', 'A3'))
#
# scan_1 = Scaner('Сканер', 'EPSON', 'YM897-18', '2020', '50-73', '5', 'White')
# print(scan_1.carta_tovara('Планшетный', 'A2'))
#
# xero_1 = Printer('Ксерокс', 'Canon', 'CaXe91-02', '2021', '46-15a', '7', 'Black')
# print(xero_1.carta_tovara('Струйный', 'A4'))