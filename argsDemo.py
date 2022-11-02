# *args = parameter will pack all arguments into a tuple
# useful so that a function can accept a varying amount of arguments

def add_one(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(add_one(1,2,3))

def add(*stuff): #the "*args" will accept multiple inputs. args are iterable
    stuff = list(stuff) #define tuple as a list so you can modify index's.
    sum = 0
    stuff[0] = 0
    for i in stuff:
        sum += i
    return sum

print(add(1,2,3))