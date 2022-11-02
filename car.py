# objects in POOP will have attributes that can be passed along to describe an object, and methods which is code that your object can do.

class Car:

    wheels = 4 # this is a class variable. All cars will have 4 wheels

    def __init__(self, make, model, year, color):
        self.make = make  # these are attributes that describe an object
        self.model = model # these variables are instanced variables. Declared inside the class, but outside of the constructor
        self.year = year
        self.color = color

    def drive(self):  # this is a method that describes what an object can do.
        print('This {} is driving.'.format(self.model))

    def stop(self):
        print('This ' + self.model + ' is stopped')
