#2d lists = a list of lists

drinks = ['coffee', 'soda', 'tea']
dinner = ['pizza','hamburger','hotdog']
dessert = ['cake','ice-cream']

food = [drinks,dinner,dessert]

print(food[0][0]) #this list of lists will index each list first, you can put a second [] to pick a specific item.
print(food[1][1])
print(food[2][1])