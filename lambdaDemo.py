# lambda function = function written in 1 line using lambda keyword
# accepts any number of arguments (only as 1 expression)

#def double(x):
    #return x * 2

#print(double(5)) #Lets lambda this bad boy!

double = lambda x:x * 2
multiply = lambda x, y: x * y
add = lambda x, y, z: x + y + z
full_name = lambda first_name, last_name: first_name+' '+last_name
age_check = lambda age:True if age >= 18 else False
print(age_check(12))
print(full_name('Chad', 'Thunder'))
print(double(8))
print(multiply(2,5))
print(add(1,2,3))




