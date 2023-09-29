class Movable:
	def move(self):
		raise NotImplementedError


class Flyable(Movable):
	def fly(self):
		raise NotImplementedError


class Plane(Flyable):
	def fly(self):
		print("Flying")

	def move(self):
		print("Taxxing on runway")


class Train(Movable):
	def move(self):
		print("Moving on rails")

