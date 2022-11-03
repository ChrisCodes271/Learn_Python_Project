# Child class inherits from another class

class Organism:
    alive = True


class Animal(Organism):

    def eat(self):
        print('{} is eating!'.format(self.__class__.__name__))  # This self.__class__.__name__ will pass the class name in the {}


class Dog(Animal):  # This Dog will be alive, can eat, and can bark. This is multi-level inheritance.

    def bork(self):
        print('This dog is barking')


dog = Dog()

print(dog.alive)
dog.eat()
dog.bork()
