# Abstract classes prevent a user from creating an object of that class
# Tells user to override abstract methods in child class.
# Think of this like a shell of a class, or an image of one that isn't there, but can be used with additional steps

from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod #This will prevent us from creating a Vehicle object
    def go(self):
        pass
    @abstractmethod #Both methods must be used by Car and Motorcycle
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print('You drive the car') #Having an abstract parent forces this overriden method to be here. Otherwise you get a TypeError.
        return self

    def stop(self):
        print("This car is stopped")
        return self


class Motorcycle(Vehicle):

    def go(self):
        print('You ride the motorcycle')
        return self

    def stop(self):
        print("This motorcycle is stopped")
        return self

#vehicle = Vehicle() Because vehicle is abstract this won't work!
car = Car()
motorcycle = Motorcycle()

car.go().stop()

motorcycle.go().stop()