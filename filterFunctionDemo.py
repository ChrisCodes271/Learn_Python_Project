# filter() = creates a collection of elements from an iterable for which a func returns true.

#filter(function, iterable)

friends = [('Rachel',19),
           ('Monica',18),
           ('Phoebe',17),
           ('Joey',16),
           ('Chandler',21),
           ('Ross',20)]

age = lambda data:data[1] >= 18 # pass something in checking first index >= 18

can_vote = list(filter(age, friends)) # create list filtered by age

for i in can_vote:
    print(i)