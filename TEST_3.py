class Circle:
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def get_area(self):
        return self.pi * (self.radius ** 2)

    def get_circumference(self):
        return 2 * self.pi * self.radius


circle_1 = Circle()
print(circle_1.get_area())
print(circle_1.get_circumference())

circle_2 = Circle(3)
print(circle_2.get_area())

circle_3 = Circle(5)
circle_area = circle_3.get_area()
print(circle_area)