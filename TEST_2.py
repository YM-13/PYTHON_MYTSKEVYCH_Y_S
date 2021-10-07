class Car:

    wheels_number = 4

    def __init__(self, name, color, year, is_crashed):
        self.name = name
        self.color = color
        self.year = year
        self.is_crashed = is_crashed

    def drive(self, city):
        print(self.name + ' is driving to ' + city)

    def change_color(self, new_color):
        self.color = new_color

opel_car = Car('Opel Tigra', 'grey', '2015', True)
opel_car.drive('LONDON')
print(opel_car.color)

mazda_car = Car('Mazda CX7', 'green', '2019', False)
mazda_car.drive('PARISE')
print(mazda_car.year)

mazda_car.change_color('yellow')
print(mazda_car.color)