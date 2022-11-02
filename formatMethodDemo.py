#str.format() method available to strings. Optional but gives more control

animal = 'cow'
item = 'moon'

#print('The ' + animal + ' jumped over the ' + item)

#print('The {} jumped over the {}'.format('Cow','Moon')) #the {} is a format field. They are read in order when values are placed.
#print('The {} jumped over the {}'.format(animal,item)) #you can pass varibles into format fields
#print('The {1} jumped over the {0}'.format(animal,item)) #if you put a number in format fields, it will index in that order.
#print('The {animal} jumped over the {item}'.format(animal='cow',item='moon')) #you can also do a keyword argument. These keywords can be reused. Remember the keyword argument isn't a variable.

text = 'The {} jumped over the {}'
print(text.format(animal,item))

name = 'Chris'

print('Hello! my name is {}'.format(name))
print('Hello! my name is {:10}.'.format(name)) #you can put padding around your format input. You simply use the :# to shift a number of spaces
print('Hello! my name is {:>10}.'.format(name)) #the < sign aligns left, the > sign aligts right, and the ^ will center all within the padding

number = 3.14159
number2 = 1000000

print('The number pi is {:.2f}'.format(number)) #this will display first 2 digits. 2f gives you the first two floating point numbers. It will round!
print('The number is {:b}'.format(number2)) #give binary number!
print('The number is {:o}'.format(number2)) #octal
print('The number is {:x}'.format(number2)) #hexadecimal
print('The number is {:,}'.format(number2)) #put commas in appropriate place
print('The number is {:E}'.format(number2)) #scientific notation
