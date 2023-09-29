class Shape:
	def calc_area(self):
		raise NotImplementedError


class Shape2D(Shape):
	def calc_area(self):
		raise NotImplementedError


class Shape3D(Shape):
	def calc_volume(self):
		raise NotImplementedError

	def calc_area(self):
		raise NotImplementedError


class Circle(Shape2D):
	def __init__(self, radius):
		self.radius = radius

	def calc_area(self):
		return 3.14 * self.radius * self.radius


class Rectangle(Shape2D):
	def __init__(self, length, breadth):
		self.length = length
		self.breadth = breadth

	def calc_area(self):
		return self.length * self.breadth


class Sphere(Shape3D):
	def __init__(self, radius):
		self.radius = radius

	def calc_area(self):
		return 4 * 3.14 * self.radius * self.radius

	def calc_volume(self):
		return 4/3 * 3.14 * self.radius * self.radius * self.radius


class Cube(Shape3D):
	def __init__(self, side):
		self.side = side

	def calc_area(self):
		return 6 * self.side * self.side

	def calc_volume(self):
		return self.side * self.side * self.side