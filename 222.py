from datetime import date


# random Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)

    def display(self):
        print(self.name + "'s age is: " + str(self.age))


person = Person('Adam', 19)  # Объект "person" класса "class Person", передано два аргумента
person.display()  # использование обычного метода (функции)

person1 = Person.fromBirthYear('John', 1985) # Объект "person1" для метода "fromBirthYear" в "class Person"
person1.display()