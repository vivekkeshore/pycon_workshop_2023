class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __str__(self):
		return f"{self.name} is {self.age} years old."

	def to_dict(self):
		return {"name": self.name, "age": self.age}


class Storage:
	def save(self, person):
		raise NotImplementedError


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


person1 = Person("abc", 10)
person2 = Person("xyz", 20)

file_storage = FileStorage()
json_storage = JsonStorage()
csv_storage = CSVStorage()

file_storage.save(person1)
file_storage.save(person2)

json_storage.save(person1)
json_storage.save(person2)
