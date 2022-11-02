# a set is a collection which is unordered, unindexed. No duplicate values

utensils = {'fork','spoon','knife'}
dishes = {'plate','bowl','cup','knife'}

utensils.add('napkin') #add and remove
utensils.remove('fork')
# utensils.clear() will empty utensilts

# dishes.update(utensils) #will add all values from utensils to dishes

#dinner_table = utensils.union(dishes) #will merge the two!
#print(utensils.union(dishes))

print(utensils.difference(dishes)) #print the differences
print(utensils.intersection(dishes)) #print the items that are the same