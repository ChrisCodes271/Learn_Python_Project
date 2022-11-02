#for loop = statement that executes a limited number of times
import time #time import lets things count in seconds (as well as other stuff)

#for i in range(10):
    #print(i+1) #remember computers count at 0!

#for i in range(50, 100): #remember end value is exclusive for end point. So you'll only get 50-99!
    #print(i)

#for i in range (10,1000,2): #the third value will count by 2!
    #print(i)

for seconds in range (10,0,-1): #you can use i, seconds, dinosaurs, any variable will work here.
    print(seconds)
    time.sleep(1) #default unit is seconds. So this will wait 1 second

print('Happy New Year!')