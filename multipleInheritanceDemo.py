#Where a child derives from multiple parents.

class Prey:

    def flee(self):
        print('This {} flees!'.format(self.__class__.__name__))

class Predator:

    def hunt(self):
        print('This {} is hunting'.format(self.__class__.__name__))

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator): #In this instance the fish has access to the hunt, and flee method.
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()
fish.hunt()
fish.flee()