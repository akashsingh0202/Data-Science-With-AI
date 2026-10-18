# Liskov Substitution Principle (LSP)
# Definition (English): Objects of a superclass should be replaceable with objects of its subclasses without breaking the program.
# Hinglish: Child class ka object, parent class ke object ki jagah use karne par program sahi kaam karna chahiye.

class Bird:
    def eat(self):
        print("Bird is eating")

class Sparrow(Bird):
    def fly(self):
        print("Sparrow is flying")

def feed_bird(bird):
    bird.eat()

feed_bird(Sparrow())