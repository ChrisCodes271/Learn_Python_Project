#tuple = collection in order that is unchangeable

student = ('Chris',25,'Male') #different from a list because you use ()

print(student.count('Chris')) 
print(student.index(25))

for x in student:
    print(x)

if 'Chris' in student:
    print('Chris is here!')


