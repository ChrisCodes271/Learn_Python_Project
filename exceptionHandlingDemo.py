#exception = event detected during execution that interrupts the normal flow of a program

try:
    num = int(input('Enter a number to divide: '))
    denom = int(input('Enter a number to divide by '))
    result = num / denom

except ZeroDivisionError as e:
    print(e)
    print('You cant divide by zero...')


except ValueError as e:
    print(e)
    print('Enter only numbers please...')


except Exception as e: #single except blocks aren't best practice cause you can't use them.
    print('Something went wrong...')
    print(e)

else:
    print(result)

finally:
    print('You will always see this message')