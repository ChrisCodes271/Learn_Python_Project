#creates substring by extracting elements from a string
#use indexing operation[] or slice()
#3 optional arguments [start:stop:step]

name = 'Chad Thunder'

first_name = name[:4] #Index 0 - 3 wouldn't spit out 4 letter name because stop index is exclusive. Can start at 0 or leave blank for auto start at 0
print(first_name)

last_name = name[5:] #Index 5 starts at 'T' and you can leave end blank to run to end or set end value. Remember its exclusive
print(last_name)

messy_name = name[::2] #print every "second" character in a step. You can leave start and end value empty in order to use entire string
print(messy_name)

reversed_name = name[::-1] #if you set step to -1 you get reversed value.
print((reversed_name))

google = 'http://google.com'
duckduckgo = 'http://duckduckgo.com'
default_slice = slice(7,-4) #This slice operator just creates a slice named default slice you still need to set it equal to a variable or call the slice
google_slice = google[default_slice] #set google_slice equal to the google website after it's been sliced
duck_slice = duckduckgo[default_slice]

print(google_slice)
print(duck_slice)
print(google[default_slice])
print(duckduckgo[default_slice])
