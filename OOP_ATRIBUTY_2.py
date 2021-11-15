""" 3:00 5.Атрибуты
delatter - используется, если необходимо удалить какой-то атрибут или метод (5:00).
Удаляет из класса глобально.
"""
class User:
    name = "Test"
    age = 17

a = User()
b = User()
c = User()
a.name = "Max"
b.name = "name1"
c.name = "name2"
print(User.name)
print(dir(User))

delattr(User, "name")
print(dir(User))
#print(User.name)
delattr(User, "age")
print(dir(User))
