class Dog():

    species = 'mammal'

    def __init__(self, breed, name):

        self.breed = breed
        self.name = name

    def bark(self,number):
        print("Foof. My name is {} and my number {}".format(self.name, number))

my_dog = Dog('Lab', 'Franky')
print(type(my_dog))

print(my_dog.breed)
print(my_dog.name)
print(my_dog.species)
print(my_dog.bark(2))


class Circle():

    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius * radius * Circle.pi

    def get_circumfrence(self):
        return self.radius * self.pi * 2

my_circle = Circle()


print(my_circle.area)
print(my_circle.get_circumfrence())