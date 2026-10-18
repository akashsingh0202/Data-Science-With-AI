# Dependency Inversion Principle (DIP)
# Definition (English): High-level modules should not depend on low-level modules. Both should depend on abstractions.
# Hinglish: Main business logic ko kisi ek specific class par directly depend nahi karna chahiye. Dono ko ek common abstraction par depend karna chahiye.
class EmailService:
    def send(self):
        print("Email sent")

class Notification:
    def __init__(self, service):
        self.service = service

    def notify(self):
        self.service.send()

email = EmailService()
notification = Notification(email)
notification.notify()