#nested function calls = function calls inside other function calls
#innermost function calls happen first
#returned value is used as argument for next function

num = input('Enter a whole positive number: ')
num = float(num)
num = abs(num)
num = round(num)
print(num)

print(round(abs(float(num))))