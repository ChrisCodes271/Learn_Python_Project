#index operator [] = gives access to a sequence's elements (str,lists,tuples,etc.)

name = 'chad thunder'

if(name[0].islower()): #this if statement will check index 0 . in this case that's the letter c.
    name = name.capitalize()

first_name = name[0:4].upper() #remember that second value is exclusive
last_name = name[5:].lower() #remember second value is exclusive but you can leave blank to print to the end.
last_character = name[-1] #you can use a negative number to start at the end



print(last_character)
print(first_name)
print(last_name)
print(name)