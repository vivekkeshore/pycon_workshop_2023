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
