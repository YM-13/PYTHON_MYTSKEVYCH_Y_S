"""
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А
также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определите
параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
уникальные для каждого типа оргтехники.
"""


class Orgtehnika:
    ci_orgteh = 'шт'
    n_podcherc = '___________________________'
    work_color = 'цветной/черно-белый'

    def __init__(self, name_type, factory, model, year, articul, pce, color):
        self.name_type = name_type
        self.factory = factory
        self.model = model
        self.year = year
        self.articul = articul
        self.pce = pce
        #        self.max_format = max_format
        self.color = color

    def carta_tovara(self):
        print(f'КАРТОЧКА ТОВАРА\nНаименование: {self.name_type}\nПроизводитель: {self.factory}\n'
              f'Модель: {self.model}\nРежим работы: {Orgtehnika.work_color}\n'
              f'Цвет устройства: {self.color}\nГод выпуска: {self.year}\nАртикул: {self.articul}\n'
              f'Остаток на складе: {self.pce} {Orgtehnika.ci_orgteh}\n{Orgtehnika.n_podcherc}')


class Printer(Orgtehnika):
    def __init__(self, name_type, factory, model, year, articul, pce, color):
        Orgtehnika.__init__(self, name_type, factory, model, year, articul, pce, color)

    def carta_tovara(self, sposob_pechati, max_paper):  # sposob_pechati
        self.sposob_pechati = sposob_pechati
        self.max_paper = max_paper
        return (f'КАРТОЧКА ТОВАРА\nНаименование: {self.name_type}\nПроизводитель: {self.factory}\n'
                f'Способ печати: {self.sposob_pechati}\nМодель: {self.model}\nРежим работы: {Orgtehnika.work_color}\n'
                f'Формат бумаги: {self.max_paper}\nЦвет устройства: {self.color}\nГод выпуска: {self.year}\nАртикул: {self.articul}\n'
                f'Остаток на складе: {self.pce} {Orgtehnika.ci_orgteh}\n{Orgtehnika.n_podcherc}')


class Scaner(Orgtehnika):
    def __init__(self, name_type, factory, model, year, articul, pce, color):
        Orgtehnika.__init__(self, name_type, factory, model, year, articul, pce, color)

    def carta_tovara(self, tip_scanera, max_doc_format):
        self.tip_scanera = tip_scanera
        self.max_doc_format = max_doc_format
        return (f'КАРТОЧКА ТОВАРА\nНаименование: {self.name_type}\nПроизводитель: {self.factory}\n'
                f'Тип сканера: {self.tip_scanera}\nМодель: {self.model}\nРежим работы: {Orgtehnika.work_color}\n'
                f'Формат документа: {self.max_doc_format}\nЦвет устройства: {self.color}\nГод выпуска: {self.year}\nАртикул: {self.articul}\n'
                f'Остаток на складе: {self.pce} {Orgtehnika.ci_orgteh}\n{Orgtehnika.n_podcherc}')


class Xerox(Orgtehnika):
    def __init__(self, name_type, factory, model, year, articul, pce, color):
        Orgtehnika.__init__(self, name_type, factory, model, year, articul, pce, color)

    def carta_tovara(self, sposob_pechati, max_paper):  # sposob_pechati
        self.sposob_pechati = sposob_pechati
        self.max_paper = max_paper
        return (f'КАРТОЧКА ТОВАРА\nНаименование: {self.name_type}\nПроизводитель: {self.factory}\n'
                f'Способ печати: {self.sposob_pechati}\nМодель: {self.model}\nРежим работы: {Orgtehnika.work_color}\n'
                f'Формат документа: {self.max_paper}\nЦвет устройства: {self.color}\nГод выпуска: {self.year}\nАртикул: {self.articul}\n'
                f'Остаток на складе: {self.pce} {Orgtehnika.ci_orgteh}\n{Orgtehnika.n_podcherc}')


prin_1 = Printer('Принтер', 'HP', 'CW86', '2021', '45-89', '99', 'Black')
print(prin_1.carta_tovara('LASER', 'A3'))

scan_1 = Scaner('Сканер', 'EPSON', 'YM897-18', '2020', '50-73', '5', 'White')
print(scan_1.carta_tovara('Планшетный', 'A2'))

xero_1 = Printer('Ксерокс', 'Canon', 'CaXe91-02', '2021', '46-15a', '7', 'Black')
print(xero_1.carta_tovara('Струйный', 'A4'))
