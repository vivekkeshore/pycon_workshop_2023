# Liskov Substitution

# Promotes flexibility, maintainability, and robustness.
# Encourages strong adherence to interfaces and contracts.

class Notification:
	def __init__(self, message, recipient):
		self.message = message
		self.recipient = recipient
	def notify(self):
		raise NotImplementedError


class EmailNotification(Notification):
	pass
	# def notify(self, email):


class SMSNotification(Notification):
	pass
	# def notify(self, phone_number):


class SlackNotification(Notification):
	pass
	# def notify(self, slack_user):


notification1 = EmailNotification("Hello", "abc@xyz.com")
notification2 = SMSNotification("Hello", "123456789")

notification1.notify()
notification2.notify()


class NotificationManager:
	def __init__(self, notification, user):
		self.notification = notification
		self.user = user

	def send_notifications(self):
		pass


# notification_manager1 = NotificationManager(notification1, user)
# notification_manager2 = NotificationManager(notification2, user)
# notification_manager1.send_notifications()
# notification_manager2.send_notifications()

