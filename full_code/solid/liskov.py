# Liskov Substitution

# Promotes flexibility, maintainability, and robustness.
# Encourages strong adherence to interfaces and contracts.

class Notification:
	def notify(self, recipient):
		raise NotImplementedError


class EmailNotification(Notification):
	def __init__(self, message):
		self.message = message

	def notify(self, email):
		print(f"Sending email to {email} with message {self.message}")


class SMSNotification(Notification):
	def __init__(self, message):
		self.message = message

	def notify(self, phone_number):
		print(f"Sending SMS to {phone_number} with message {self.message}")


class SlackNotification(Notification):
	def __init__(self, message):
		self.message = message

	def notify(self, slack_user):
		print(f"Sending Slack notification to {slack_user} with message {self.message}")


notification1 = EmailNotification("Hello", "abc@example.com")
# notification2 = EmailNotification("Hello", "9587687328")
notification3 = SMSNotification("Hello", "1234567890")

# notification1.notify()
# notification1.notify()


class NotificationManager:
	def __init__(self, notification, user):
		self.notification = notification
		self.user = user

	def send_notifications(self):
		if isinstance(self.notification, EmailNotification):
			self.notification.notify(self.user.email)
		elif isinstance(self.notification, SMSNotification):
			self.notification.notify(self.user.phone_number)
		elif isinstance(self.notification, SlackNotification):
			self.notification.notify(self.user.slack_user)
		else:
			raise Exception("Invalid notification type")


notification_manager1 = NotificationManager(notification1, user)
notification_manager2 = NotificationManager(notification3, user)
notification_manager1.send_notifications()
notification_manager2.send_notifications()

