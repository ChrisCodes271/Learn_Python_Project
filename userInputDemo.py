name = input('What is your name?: ')
age = input('What is your age?:')  ##user input is always taken as a string.

age = int(age) #convert it to an int so you can manipulate it.
age = str(age*4)

print('Hello ' + name)
print('You are 1/4 of the way to ' + age + ' years old!')