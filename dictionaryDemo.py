#dictionary = a changeable, unordered collection of unique key:value pairs. fast because they use hashing to allow quick access

capitals = {'USA':'Washington,DC',
            'India':'New Dehli',
            'China':'Beijing',
            'Russia':'Moscow'}  #the colon applies the key value pair

capitals.update({'Germany':'Berlin'}) #this will add to your dictionary
capitals.update({'USA':'Las Vegas'}) #this will also edit existing values
capitals.pop('China') #will remove the Key value pair . You can also use .clear to empty it out

print(capitals['Russia']) #will print Moscow - isn't safe because you will get keyerrors if value input doesn't exist
print(capitals.get('Russia')) #this is safer and wont throw keyerror if value doesn't exist
print(capitals.keys()) #you can print all the keys!
print(capitals.values()) #you can print the values too
print(capitals.items()) #print errthang.

#you can print everything with a for loop

for key,value in capitals.items(): #the .items concept prints the entire dictionary. This forloop just prints individual keys and values more cleanly.
    print(key,value)