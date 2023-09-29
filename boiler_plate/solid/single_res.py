# Design Principles: SOLID

#  1. Single Responsibility Principle

class EmployeeSalary:
	def __init__(self, base=10000):
		self.base = base

	def calculate_salary(self):
		raise NotImplementedError


class BonusSalary(EmployeeSalary):
	def __init__(self, base=10000, bonus=1000):
		super().__init__(base)
		self.bonus = bonus

	def calculate_salary(self):
		pass


class StockSalary(EmployeeSalary):
	price_per_stock = 100

	def __init__(self, base=10000, stocks=10):
		super().__init__(base)
		self.stocks = stocks

	def calculate_salary(self):
		pass


class ContractSalary(EmployeeSalary):
	pass


class InternSalary(EmployeeSalary):
	pass


class Employee:
	def __init__(self, name: str, age: int, salary: EmployeeSalary):
		self.name = name
		self.age = age
		self.salary = salary  # Composition is preferred over inheritance


class PermanentEmployee(Employee):
	def __init__(self, name: str, age: int, salary: EmployeeSalary):
		super().__init__(name, age, salary)


class ContractEmployee(Employee):
	def __init__(self, name: str, age: int, salary: EmployeeSalary, contract_duration: int):
		super().__init__(name, age, salary)
		self.contract_duration = contract_duration


# e1 = PermanentEmployee("John", 30, BonusSalary(base=10000, bonus=1000))
# e2 = PermanentEmployee("John", 30, StockSalary(base=20000, stocks=20))
# e6 = PermanentEmployee("John", 30, StockSalary(base=50000, stocks=100))
# e3 = ContractEmployee("John", 30, ContractSalary(), 6)
# e4 = ContractEmployee("John", 30, InternSalary(), 3)


print(e1.salary.calculate_salary())
