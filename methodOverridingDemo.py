#Method overriding allows you to change a specific instance of a method in a class.

class Animal:

    def eat(self):
        print('This {} is eating'.format(self.__class__.__name__))

class Rabbit(Animal):
    def eat(self):
        print('The {} is eating a carrot'.format(self.__class__.__name__)) #The eat method has been replaced with a more specifically defined method. 

rabbit = Rabbit()
rabbit.eat()