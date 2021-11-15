""" 4:20 5.Атрибуты
delatter - используется, если необходимо удалить какой-то атрибут. Удаляет из класса глобально.

Удалить метод из экземпляра нельзя, тк он является ссылкой 5:30
"""
class User:
    name = "Test"
    age = 17

    def get_name(self):
        print(self.name)

print(getattr(User, "get_name")) # ПОЛУЧАЕМ АДРЕС ФУНКЦИИ <function User.get_name at 0x7fcc759968b0>
a = User()
print(getattr(a, "get_name")) # ПОЛУЧАЕМ МЕТОД НАШЕГО ЭКЗ.:
                        # <bound method User.get_name of <__main__.User object at 0x7fcc75cd2430>>
print(getattr(a, "get_name")()) # добавление вконце "()" вызывает наш метод

delattr(User, "get_name") # Удалили метод из класса
print(dir(User)) # Проверяем в классе.. и метода нет
print(User.__dict__)
print(dir(a))    # Проверяем в экз. .. и метода нет

print(a.__class__.__name__) # Узнаем класс экземпляра "а"