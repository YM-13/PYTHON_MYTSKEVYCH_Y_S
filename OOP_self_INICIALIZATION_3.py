"""
мы можем создать метод и вызвать его из __init__
"""
class User:
    def __init__(self, name):
        self.name = name
        self.get_name()

    def get_name(self):
        print(self.name)
""" Т.К. "name" НАХОДИТСЯ ВНУТРИ ЭКЗЕМПЛЯРА МЫ УКАЗЫВАЕМ "self", и т.к. НАШ МЕТОД тоже НАХОДИТСЯ ВНУТРИ
ЭКЗЕМПЛЯРА МЫ т.ж. УКАЗЫВАЕМ "self".
ЭТО НУЖНО ЗАПОМНИТЬ: ЕСЛИ АРГУМЕНТ НАХОДИТСЯ ВНУТРИ ЭКЗЕМПЛЯРА, то указываем "self"
"""
a = User("test")
"""В ИТОГЕ, ПОСЛЕ ИНИЦЫАЛИЗАЦИИ МЫ ПОЛУЧАЕМ СНАЧАЛА НАЗВАНИЯ, КОТОРОЕ ПЕРЕДАЕМ В КАЧЕСТВЕ АРГУМЕНТОВ ПРИ
СОЗДАНИИ ЭКЗЕМПЛЯРОВ, далее вызывая МЕТОД внутри нашего ЭКЗЕМПЛЯРА и получаем SELF.NAME
"""