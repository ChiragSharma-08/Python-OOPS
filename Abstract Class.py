# Abstract Class: A class that cannot be instantiated on its own; Ment to be subclassed.
#                 They can contain abstract methods, which are declared but have no implementation.
#                 Abstract classes benifits:
#                 1. Prevents instantiation of the class itself
#                 2. Requiress children to use inherited abstract methods

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("You are driving a car")

    def stop(self):
        print("You are stopping a car")

class Motorcycle(Vehicle):
    def go(self):
        print("You are riding a motorcycle")
    def stop(self):
        print("You are stopping a motorcycle")

class Boat(Vehicle):
    def go(self):
        print("You are sailing a boat")
    def stop(self):
        print("You are ancoring a boat")


car = Car()
car.go()

boat = Boat()
boat.stop()