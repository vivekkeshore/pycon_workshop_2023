# Attributes ?
# Methods ?

class EmptyCartridgeError(Exception):
	pass


class InkCartridge:
	def __init__(self, tip_size='0.5', ink_color='Blue', ink_volume=1000, total_volume=1000, brand='Pycon'):
		self.tip_size = tip_size
		self.ink_color = ink_color
		self.ink_volume = ink_volume
		self.total_volume = total_volume
		self.brand = brand


class Pen:  # Composite object
	def __init__(self, ink_cartridge, brand='Pycon'):
		self.ink_cartridge = ink_cartridge
		self.brand = brand
