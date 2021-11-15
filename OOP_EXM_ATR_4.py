"""
ОТЛИЧИЕ ВЫЗОВА dir ВНУТРИ КЛАССА И ОБЪЕКТОВ
"""
class User:
    name = "Alex" # атрибут (переменная)
    age = 17      # атрибут (переменная)

    def get_name(self, name):
        print(self, name)

    def get_age(self, age):
        print(self, age)

a = User()
b = User()
c = User()
a.name = "Alex"
b.name = "name1"
c.name = "name2"

print(dir(User)) # В НАШЕМ КЛАССЕН ПОКАЖЕТ ДВА АТРИБУТА С НАШИМИ ПЕРЕМЕННЫМИ И ДВА АТРИБУТА - НАШИЫ МЕТОДЫ
print(dir(a)) # ТАКАЯ ЖЕ КАРТИНА В НАШЕМ ЭКЗЕМПЛЯРЕ

print(User.__dict__)
print(a.__dict__)
print(b.__dict__)