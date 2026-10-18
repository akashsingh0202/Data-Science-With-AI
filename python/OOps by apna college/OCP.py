# Definition (English): Software entities should be open for extension, but closed for modification.
# Hinglish: Naya feature add kar sakein, bina existing code ko baar-baar change kiye.


class Payment:
    def pay(self):
        pass

class UpiPayment(Payment):
    def pay(self):
        print("Paid using UPI")

class CardPayment(Payment):
    def pay(self):
        print("Paid using Card")