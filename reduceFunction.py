# reduce = apply func to an iterable and reduce it to a single cumulative value
# performs function on first two elements and repeats process until 1 value remains

# reduce(function, iterable)

import functools as funkytown #To do this you need to import functools... I wanted to name it funkytown for this demo.

letters = ['H', 'E', 'L', 'L', 'O']
word = funkytown.reduce(lambda x, y: x + y, letters) #reducing x and y by adding to give you HELLO

print(word)

factorial = [i * i for i in range(1, 11)]
result = funkytown.reduce(lambda x,y: x * y,factorial) #You can reduce by multiplication, or other functions as well.

print(result)