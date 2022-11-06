# If a number is divisible by 2 - print Fizz
# If a number is divisible by 3 - print Buzz
# If a number is divisible by both - print FizzBuzz

for i in range(31):
    x = i
    if x % 2 == 0 and x % 3 == 0:
        print('FizzBuzz')
    elif x % 3 == 0:
        print('Buzz')
    elif x % 2 == 0:
        print('Fizz')
    else:
        print(x)