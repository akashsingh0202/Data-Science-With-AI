# # Single Responsibility Principle (SRP) shuru karte hain.
# Definition (English): A class should have only one reason to change.
# Hinglish: Ek class ki ek clear responsibility honi chahiye.

# class Report:
#     def generate(self):
#         print("Report generated")

#     def save_to_file(self):
#         print("Report saved")

#     def send_email(self):
#         print("Email sent")

class Report:
    def generate(self):
        print("Report generated")

class FileSaver:
    def save(self):
        print("Report saved")

class EmailSender:
    def send(self):
        print("Email sent")