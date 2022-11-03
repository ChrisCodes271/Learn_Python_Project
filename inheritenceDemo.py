class Animal: #This will be the parent class

    alive = True #This attribute is for Animal and any of its Children

    def __init__(self):
        pass

    def eat(self):
        print('This animal is eating') #This method will also be passed down.

    def slumber(self):
        print('This animal is sleeping')

class Rabbit(Animal): #This will create a Rabbit class that inherits its attributes and methods from the Animal class
    def run(self):
        print('This rabbit is running!') #These methods in each child are unique to this class.

class Fish(Animal):
    def swim(self):
        print('This fish is swimming!')

class Hawk(Animal):
    def fly(self):
        print('This Hawk is Flying!')

rabbit = Rabbit() #Create rabbit!
fish = Fish()
hawk = Hawk()

print(rabbit.alive) #Notice how the Rabbit class is empty, but it still has all of the attributes and methods associated with Animal. Thats inheritance!
fish.eat()
hawk.slumber()
rabbit.run()
fish.swim()
hawk.fly()