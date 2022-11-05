# sort() method = used with lists
# sort() function = used with iterables

#students = ['Squidward','Sandy','Patrick','Spongebob','Mr. Krabs'] #students list

#students.sort() #sort the list

#for i in students:
    #print(i)

#students.sort(reverse=True)

#for j in students:
    #print(j)

#sorted_students = sorted(students)

#for k in sorted_students:
    #print(k)

#sorted_students_rev = sorted(students,reverse=True)
#for l in sorted_students_rev:
    #print(l)

students = [('Squidward', 'F', 60), #Think of this like a spreadsheet with "rows" and "Columns"
            ('Sandy', 'A', 33),
            ('Spongebob', 'B', 20),
            ('Patrick', 'D', 70)]

students.sort() #The default sort will sort alphabetically the names in the tuple.
grade = lambda grades:grades[1] #Establish grade variable as first index of whatever is used
students.sort(key=grade,reverse=True) #If you pass key=grade you're going to tell it to use index 1 to sort. Giving you sort by grades.
for i in students:
    print(i)