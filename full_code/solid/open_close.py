class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __str__(self):
		return f"{self.name} is {self.age} years old."


class Storage:
	def save(self, person):
		raise NotImplementedError

	@staticmethod
	def convert_to_dict(person):
		return {"name": person.name, "age": person.age}


class FileStorage(Storage):
	def save(self, person):
		print("Saving to file")


class DatabaseStorage(Storage):
	def save(self, person):
		print("Saving to database")


class CSVStorage(Storage):
	def save(self, person):
		print("Saving to csv")


class JsonStorage(Storage):
	def save(self, person):
		print("Saving to json")


# class SaveData:
# 	def save_db(self, person):
# 		# Db connnection, db logic etc.
# 		print(f"Saving {person.name} to database.")
#
# 	def save_json(self, person):
# 		# serialize logic
# 		print(f"Saving {person.name} to json.")
#
# 	def save_csv(self, person):
# 		# csv logic
# 		print(f"Saving {person.name} to csv.")


person1 = Person("abc", 10)
person2 = Person("xyz", 20)

file_storage = FileStorage()
json_storage = JsonStorage()
csv_storage = CSVStorage()

file_storage.save(person1)
file_storage.save(person2)

json_storage.save(person1)
json_storage.save(person2)


class Shape:
	def __init__(self, name, x=None, y=None, radius=None):
		self.name = name
		self.x = x
		self.y = y
		self.radius = radius

	def calc_volume(self):
		pass

	def calc_area(self):
		# All attributes are not used in each case.
		# Code might break with new modifications.

		if self.name.lower() == "circle":
			return 3.14 * self.radius * self.radius

		elif self.name.lower() == "rectangle":
			return self.x * self.y

		# elif for triangle. Keep adding new code for new scenarios.

		else:
			raise Exception("Invalid shape")


circle = Shape("circle", radius=10)
rectangle1 = Shape("rectangle", x=10, y=20)
rectangle2 = Shape("rectangle", x=25, y=50)

print(f"Area of circle - {circle.calc_area()}")
print(f"Area of rectangle1 - {rectangle1.calc_area()}")
print(f"Area of rectangle2 - {rectangle2.calc_area()}")
