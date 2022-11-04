# walrus operator = assignment expression and uses a := / new to Python 3.8.
# assigns values to variables as part of a larger expression

# happy = True / Lets combine these two!
# print(happy)/

print(happy := True)

# foods = list()
# while True:
# food = input('What food would you like? or type quit to exit.').lower()
# if food == 'quit':
# break
# foods.append(food) LETS WALRUS THIS CODE

drinks = list()

while drink := input('What food do you like? (or type quit to exit').lower() != 'quit':
    drinks.append(drink)

# code explanation
# while loop setting drink equal to the input (lowercase) and then verifying it's not equal to quit.
# the end of the loop is simply appending the input. Hope you don't like 'quit' energy drink.
