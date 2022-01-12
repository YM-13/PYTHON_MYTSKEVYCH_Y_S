class Animal():

    def __init__(self):
        print("Animal Created")


    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")

my_animal = Animal()

#print(my_animal.__init__())

class Dog(Animal):
