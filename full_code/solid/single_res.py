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
		return (self.base * 12) + self.bonus


class StockSalary(EmployeeSalary):
	def __init__(self, base=10000, stocks=10):
		super().__init__(base)
		self.stocks = stocks
		self.price_per_stock = 100

	def calculate_salary(self):
		return (self.base * 12) + self.stocks * self.price_per_stock


class BonusStocksSalary(EmployeeSalary):
	def __init__(self, base=10000, bonus=1000, stocks=50):
		super().__init__(base)
		self.bonus = bonus
		self.stocks = stocks
		self.price_per_stock = 100

	def calculate_salary(self):
		return (self.base * 12) + self.bonus + (self.stocks * self.price_per_stock)


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


e1 = PermanentEmployee("John", 30, BonusSalary(base=10000, bonus=1000))
e2 = PermanentEmployee("John", 30, StockSalary(base=20000, stocks=20))
e6 = PermanentEmployee("John", 30, StockSalary(base=50000, stocks=100))
e7 = PermanentEmployee("John", 30, BonusStocksSalary(base=50000, bonus=10000, stocks=100))
e3 = ContractEmployee("John", 30, ContractSalary())
e4 = ContractEmployee("John", 30, InternSalary())


print(e1.salary.calculate_salary())
print(e6.salary.calculate_salary())


class Interest:
	pass

class Account:
	def __init__(self, account_holder, balance=0):
		self.account_holder = account_holder
		self.balance = balance

	def deposit(self, amount):
		raise NotImplementedError

	def withdraw(self, amount):
		raise NotImplementedError

	def get_balance(self):
		raise NotImplementedError


class SavingsAccount(Account):
	def __init__(self, account_holder, balance=0):
		super().__init__(account_holder, balance)

	def calculate_simple_interest(self):
		pass

	def calculate_compound_interest(self):
		pass


class CurrentAccount(Account):
	def __init__(self, account_holder, balance=0):
		super().__init__(account_holder, balance)



