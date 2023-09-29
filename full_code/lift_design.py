class Button:
	def __init__(self, name):
		self.name = name
		self.is_pressed = False

	def press(self):  # Every derived class must implement this method
		raise NotImplementedError


class FloorButton(Button):
	def press(self):
		return self.name


class AlarmButton(Button):
	def press(self):
		print("Beep Beep Beep ...")


class Door:
	def __init__(self):
		self.is_open = False

	def open(self):
		print("door opened")
		self.is_open = True

	def close(self):
		print("door closed")
		self.is_open = False


class Lift:
	def __init__(self):
		self.capacity = 0
		self.weight = 0.0
		self.floor_1 = FloorButton(1)
		self.floor_2 = FloorButton(2)
		self.floor_3 = FloorButton(3)
		self.floor_4 = FloorButton(4)
		self.floor_5 = FloorButton(5)
		self.alarm_button = AlarmButton("Alarm")
		self.door = Door()

	def move(self, floor_button):
		print(f"Moving to floor {floor_button.name}")
		self.door.open()
		print(f"Arrived at floor {floor_button.name}")
		self.door.close()


lift = Lift()
pressed_floor_button = lift.floor_1.press()
lift.move(pressed_floor_button)

pressed_floor_button = lift.floor_2.press()
lift.move(pressed_floor_button)

pressed_floor_button = lift.floor_5.press()
lift.move(pressed_floor_button)
