# map() = applies a function to each item in an iterable (list, tuple, etc.)

# map(function, iterable)

store = [('shirt', 20.00),
         ('pants', 35.00),
         ('jacket', 50.00),
         ('socks', 15.00)]

to_pound = lambda data: (data[0],data[1]*0.88) # create this process to pass in store and spit it out
                                               # in pounds instead of usd. (.88 Pound to 1.00 USD)

store_in_pounds = list(map(to_pound, store)) # Create list store_in_pounds that converts prices to pounds.

for i in store_in_pounds:
    print(i)