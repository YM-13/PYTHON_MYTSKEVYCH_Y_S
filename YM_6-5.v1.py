"""
5. Реализовать класс Stationery (канцелярская принадлежность).
● определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит
сообщение «Запуск отрисовки»;
● создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
● в каждом классе реализовать переопределение метода draw. Для каждого класса
метод должен выводить уникальное сообщение;
● создать экземпляры классов и проверить, что выведет описанный метод для каждого
экземпляра.
"""

class Stationery:

    def __init__(self, t):
        self.title = t

    def draw(self):
        print(f'\n{self.title} Запуск отрисовки!')

class Pen(Stationery):
    def pp(self, p):
        print(f'{p}')

class Pencil(Stationery):
    def pn(self, p):
        print(f'{p}')

class Handle(Stationery):
    def hn(self, p):
        print(f'{p}')

pe_n = Pen("Используем ручку!")
pe_n.draw()
pe_n.pp("Получается красиво!")

pen_n = Pencil("Карандаш хорош в работе!")
pen_n.draw()
pen_n.pn("Четкие линии!")

hen = Handle("Перьевая ручка.")
hen.draw()
hen.hn("Все запачкали чернилами!")