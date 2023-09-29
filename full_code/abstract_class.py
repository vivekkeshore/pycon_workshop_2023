class Soldier:
	def __init__(self, soldier_type, name, weapon):
		self.soldier_type = soldier_type
		self.name = name
		self.weapon = weapon

	def __new__(cls, *args, **kwargs):
		if cls.__name__ == "Soldier":
			raise TypeError("Can't instantiate abstract class Soldier")
		return super().__new__(cls)

	def shout_war_cry(self, war_cry="For honor and glory!"):
		print(f"{self.soldier_type} | {self.name} shouts: {war_cry}")

	def attack(self):
		raise NotImplementedError

	def defend(self):
		raise NotImplementedError

	def patrol(self):
		raise NotImplementedError


class Archer(Soldier):
	def __init__(self, name):
		super().__init__("Archer", "Bob", "Bow and Arrow")
		self.name = name

	def attack(self):
		print(f"{self.name} releasing arrows.")

	def defend(self):
		print(f"{self.name} defends with {self.weapon}")

	def patrol(self):
		print(f"{self.name} patrols with {self.weapon}")


class Spearman(Soldier):
	def __init__(self, name):
		super().__init__("Spearman", "Alice", "Spear")
		self.name = name

	def attack(self):
		print(f"{self.name} thrusts with {self.weapon}")

	def defend(self):
		print(f"{self.name} defends with {self.weapon}")

	def patrol(self):
		print(f"{self.name} patrols with {self.weapon}")
