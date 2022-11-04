def hello():
    print('Hello')


print(hello) #this will print the memory address
hi = hello #You can assign this memory address to a variable
hi() #this is as if hi and hello are the same function.
hello()

say = print #make print() a variable
say('Whoa... this works!')