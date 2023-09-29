# Attributes
# catridge or ink refill
# brand

# MEthods
# write
# check ink
class EmptyCartridgeError(Exception):
	pass


class InkCartridge:
	def __init__(self, tip_size='0.5', ink_color='Blue', ink_volume=1000, total_volume=1000, brand='Pycon'):
		self.tip_size = tip_size
		self.ink_color = ink_color
		self.ink_volume = ink_volume
		self.total_volume = total_volume
		self.brand = brand

	def refill(self, vol):
		if self.ink_volume == self.total_volume:
			print('Cartridge is full. Cannot refill.')

		elif vol + self.ink_volume > self.total_volume:
			spill_over = (vol + self.ink_volume) - self.total_volume
			self.ink_volume = self.total_volume
			print(f'Ink spilled over. Spill over volume - {spill_over}')

		else:
			self.ink_volume += vol

	def __write(self, text):
		if not self.ink_volume:
			raise EmptyCartridgeError('No ink. Cannot write')

		print(f'Writing in ink color {self.ink_color}')
		if self.ink_volume < len(text):
			print(text[:self.ink_volume])
			self.ink_volume = 0
			print('Ink Over.')

		else:
			print(text)
			self.ink_volume -= len(text)


class Pen:  # Composite object
	def __init__(self, ink_cartridge, brand='Pycon'):
		self.ink_cartridge = ink_cartridge
		self.brand = brand

	def write(self, text):
		try:
			self.ink_cartridge._InkCartridge__write(text)
		except EmptyCartridgeError as ex:
			print(ex)
			print('Please refill or change the cartridge.')


cartridge = InkCartridge()
pen = Pen(cartridge)
pen.write('Hello World')
