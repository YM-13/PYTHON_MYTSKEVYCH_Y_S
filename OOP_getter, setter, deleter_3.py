"""
deleter
"""


class User:
    def __init__(self, name="test"):  # Можно указать значение по-умолчанию в __init__, тогда если мы
        self._name = name  # не передаем никаких значений, инит сам возьмет то, что по-умолчанию

    # Реализуем метод для вывода нашего атрибута, а так же для записи в него:
    @property  # - повысит безопасность. Здесь он подходит, т.к. "get_name" используется только для чтения
    def name(self):
        print("Вернули значение атрибута!")
        return self._name

    @name.setter  # Название методов одно и тоже - "name", но с помощью property и setter вызывается
    def name(self, value):  # только "name" и для чтения и для записи (см. ниже)
        print("Атрибут изменен!")
        self._name = value  # ЗДЕСЬ ПЕРЕНАЗНАЧАЕМ ЗНАЧЕНИЕ АТРИБУТА через "value"

    @name.deleter
    def name(self):
        print("Атрибут удален!")
        del self._name


a = User()
print(a.name)  # ВЫВЕЛИ ЗНАЧЕНИЕ АТРИБУТА по-умолчанию "test". Здесь "name" - метод на чтение в @property

a.name = 1  # ПЕРЕОПРЕДЕЛИЛИ ЗНАЧЕНИЕ АТРИБУТА - "1". Здесь "name" - метод на запись в @name.setter
print(a.name)

del a.name
