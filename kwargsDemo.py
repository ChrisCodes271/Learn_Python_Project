#kwargs = parameter that will pack all arguments into a dictionary
#useful for a function to accept a varying amount of keyword arguments.

def hello(**polite_name): #Remember when creating kwargs use two asterisks. Name doesn't matter. kwargs will work most cases as they are local scope variables
    print('Hello',end=' ')
    for key,value in polite_name.items():
        print(value,end='')


hello(title ='Mr. ',first='Chris ',middle='Ryan ',last='Walker ')

