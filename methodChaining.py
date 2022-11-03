# method chaining = calling multiple methods sequentially
# each call performs and action on the same object and returns self.

class Car:

    def turn_on(self):
        print('You start the engine')
        return self #you need to include return self. This will pass self in the method chain

    def drive(self):
        print('You drive the car')
        return self

    def brake(self):
        print('You step on the brakes')
        return self

    def turn_off(self):
        print('You turn off the engine')
        return self


car = Car()

car.turn_on().drive().drive().brake().turn_off()
# the \ is a non-linebreak space . To make things easier to read.