import math

class Line:

	def __init__(self, coor1, coor2):
		self.coor1 = coor1
		self.coor2 = coor2
		self.ab = ()
		self.bc = ()
		for i in zip(self.coor1, self.coor2):
			a = i[1] - i[0]
			if self.ab == ():
				self.ab = a
			else:
				self.bc = a


	def distance(self):

		return str((self.ab ** 2 + self.bc ** 2) ** 0.5)

	def slope(self):

		return self.bc / self.ab



coordinate1 = (3, 2)
coordinate2 = (8, 10)

li = Line(coordinate1, coordinate2)


print(li.distance())

print(li.slope())
