# nterface Segregation Principle (ISP)
# Definition (English): Clients should not be forced to depend on methods they do not use.
# Hinglish: Kisi class ko aise methods implement karne ke liye force nahi karna chahiye jinki use usse zaroorat hi nahi hai.
class Machine:
    def print_document(self):
        pass

    def scan_document(self):
        pass

    def fax_document(self):
        pass