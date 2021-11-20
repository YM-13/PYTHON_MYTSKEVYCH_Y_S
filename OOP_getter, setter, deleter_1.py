"""
Нужно создать метод, чтобы получить атрибут. Мы получаем атрибут напрямую, но мы не контролируем
запись и чтение нашего атрибута, а это не безопасно. Поэтому для безопасности и удобства мы будем
использовать методы getter и setter
"""

class User:
    def __init__(self, name):
        self._name = name
# Реализуем метод для вывода нашего атрибута, а так же для записи в него:
    def get_name(self):
        print("Вернули значение атрибута!")
        return self._name  # ОДНО НИЖНЕЕ ПОДЧЕРКИВАНИЕ ДЕЛАЕТ НАШ АТРИБУТ ПРИВАТНЫМ

    def set_name(self, value):
        print("Атрибут изменен!")
        self._name = value # ЗДЕСЬ ПЕРЕНАЗНАЧАЕМ ЗНАЧЕНИЕ АТРИБУТА через "value"

a = User("test") # ЗАДАЛИ ЗНАЧЕНИЕ АТРИБУТА "test"
#print(a.name)

print(a.get_name()) # ВЫВЕЛИ ЗНАЧЕНИЕ АТРИБУТА "test"

a.set_name("NEW") # ПЕРЕНАЗНАЧИЛИ ЗНАЧЕНИЕ АТРИБУТА НА "NEW"

print(a.get_name()) # ВЫВЕЛИ НОВОЕ ЗНАЧЕНИЕ АТРИБУТА "NEW"
