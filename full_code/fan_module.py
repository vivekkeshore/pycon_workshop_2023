# Fan
# Fan - Attributes or Properties
# color, brand, no of blades, size of blades, speed, state on or off

# Fan - Function or Actions
# switch it on or off, change or regulate the speed


class Fan:
	def __init__(self, color='Black', brand='Pythonista', blades=3, size_of_blades=1200, speed=0):  # Magic method or dunder methods. It is an instance method.
		self.color = color
		self.brand = brand
		self.no_of_blades = blades
		self.size_of_blades = size_of_blades  # in millimeters
		self.speed = speed
		self.is_on = False  # Boolean. False is off and True is on.

	def toggle_switch(self):  # Instance method or Bound methods
		if self.is_on:
			self.is_on = False
			print('Fan is switched off.')
		else:  # Fan is off
			self.is_on = True
			print('Fan is switched on.')

	def set_speed(self, speed):
		if speed == 0 and self.is_on:
			print('Fan stopped')

		if not self.is_on and speed:
			print('Fan is switched off. Speed is set. Switch on the fan.')

		self.speed = speed


fan = Fan()
fan.toggle_switch()
fan.set_speed(0)
fan.toggle_switch()
fan.set_speed(1)
fan.set_speed(2)
fan.set_speed(3)
fan.set_speed(4)
fan.set_speed(5)
fan.set_speed(0)
fan.toggle_switch()
