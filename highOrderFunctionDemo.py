# High order functions =
# accepts function as argument or returns a function (in Python functions are also treated as objects)

def loud(text):
    return text.upper()


def quiet(text):
    return text.lower()


def hello(func):  # This is where you will pass in a function
    text = func('Hello')
    print(text)


hello(loud)
hello(quiet)


def divisor(x):
    def dividend(y):
        return y / x

    return dividend


divide = divisor(2)
print(divide(10))

# code explanation
# You can map the above starting at divide = divisor 2.
# When you input 2 into the divisor function it cannot execute the dividend function because it has no y value.
# You set this equal to the divide variable so when you pass 10 into the divide variable the 2 is already there.
# From there the 2 is already set, you can now divide 10 by 2!
