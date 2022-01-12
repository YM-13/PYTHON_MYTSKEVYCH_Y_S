# class Animal():
#
#     def __init__(self):
#         print("Animal Created")
#
#
#     def who_am_i(self):
#         print("I am an animal")
#
#     def eat(self):
#         print("I am eating")
#
# #print(my_animal.__init__())
#
# class Dog(Animal):
#     def __init__(self):
#         Animal.__init__(self)
#         print("Dog created")
#
#     def who_am_i(self):
#         print("I am Dog!!!")
#
#     def bark(self):
#         print("Woof")
#
# my_animal = Animal()
# my_dog = Dog()
# print(my_dog.bark())

# class Dog():
#
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return self.name + " says Woof!"
#
#
# class Cat():

#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         return self.name + " says Meow!"
#
# nico = Dog("nico")
# felix = Cat("felix")
#
# print(nico.speak())

# print(felix.speak())
#
# for pet in [nico, felix]:
#
#     print(type(pet))
#     print(type(pet.speak()))
#
# def pet_speak(pet):
#     print(pet.speak())
#
# pet_speak(nico)
# pet_speak(felix)

class Animals():

    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")

class Dog(Animals):

    def speak(self):
        return self.name + " says woof!"

class Cat(Animals):

    def speak(self):
        return self.name + " says moew!"

fido = Dog("Fido")

isis = Cat("Isis")

print(fido.speak())

print(isis.speak())