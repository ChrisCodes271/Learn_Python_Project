#list = store multiple items in a variable

food = ['pizza','nachos','hotdog','hamburger'] #each item in this list is an element
food[0] = 'sushi' #this replaces element 0 in food with sushi
#print(food[2]) #this will print "hotdog" because pizza is 0 and it counts up.
#print(food[0])

food.append('ice cream') #adds ice cream
food.remove("hotdog") #removes hotdog
food.pop() #removes last element
food.insert(0,'cake') #adds at element position. Will shift entire list to the right.
food.sort() #sort alphabetically
food.clear() #will clear list

for x in food: #this will print each element. In this case x is a variable that takes the place of an element and counts up.
    print(x)
