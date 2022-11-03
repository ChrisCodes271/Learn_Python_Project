# duck typing = concept where class of an object is less important than the method / attributes
# class type is not checked if minimum methods/attributes are present
# 'If it walks like a duck, and quacks like a duck, it must be a duck!'

class Duck:

    def walk(self):
        print('This duck is walking') #Both duck and chicken have walk/talk methods that are different. They have the same name

    def talk(self):
        print('This duck is talking')

    def __str__(self):
        return 'duck'

class Chicken:

    def walk(self):
        print("This Chicken is talking")

    def talk(self):
        print('This chicken is talking')

    def __str__(self):
        return 'chicken'


class Person(): #declare Person class with a catch method that passes in an argument 'duck'

    def catch(self, duck):
        duck.walk()
        duck.talk()
        print('You caught the {}.'.format(duck))

duck = Duck() #create some ducks, chickens, and people
chicken = Chicken()
person = Person()

person.catch(duck) #you can pass duck
person.catch(chicken) #you can also pass chicken because they have the same methods/attricutes