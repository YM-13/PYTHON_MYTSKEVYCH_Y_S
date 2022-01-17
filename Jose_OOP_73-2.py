class Cylinder:
	pi = 3.14

	def __init__(self, height=1, radius=1):
		self.height = height
		self.radius = radius

	def volume(self):
		return Cylinder.pi * self.radius ** 2 * self.height

	def surface_area(self):
		return 2 * Cylinder.pi * self.radius ** 2 + 2 * Cylinder.pi * self.radius * self.height


# EXAMPLE OUTPUT
c = Cylinder(2, 3)

print(c.volume())  # 56.52

print(c.surface_area())  # 94.2
