# list comprehension = a way to make a new list with less syntax
# can mimic certain lambda functions, easier to read
# list = [expression for item in iterable]

squares = []
for i in range(1,11):
    squares.append(i * i)

print(squares)

squares = [i * i for i in range(1, 11)] #condense the above code using list comprehension
print(squares)

grades = [100,90,80,70,60,50,40,30,0] #mimic a lambda function

#passed_students = list(filter(lambda x: x >= 60, grades)) basic lambda function

# passed_students = [i for i in grades if i >= 60] # same as above.

passed_students = [i if i >= 60 else 'FAILED' for i in grades] # same as above, but showing who failed

print(passed_students)
