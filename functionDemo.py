#function = block of code executed when called

#def hello(): #this will define the hello function
    #print('Hello!')
    #print('Have a nice day!')
#hello()

#def hello_name(name): #if you list name in your definition of your function you can then pass that data in later.
   #print('Hello ' + name)
    #print('Have a nice day')


#my_name = 'Chad' You can also assign a new variable and pass it into your hello_name function
#hello_name((my_name))
#hello_name(input('What is your name? ')) #this will take user input and assign it to the name string in our hello_name function.

#def hello_full_name(first_name,last_name): #You can use the same concepts denoted above for two values!
    #print('Hello! ' + first_name + " " + last_name)
    #print('Have a nice day!')

#hello_full_name(input("What is your first name? "),input("What is your last name? ")) #pass two values and request 2 inputs.

def greetings_mortal(first_name,last_name,age): #You can also use different values like int!
    print('Hello! ' + first_name + " " + last_name)
    print('You are ' + str(age) + ' years old!')
    print('Have a nice day!')

greetings_mortal(input("What is your first name? "),input("What is your last name? "),input('What is your age? ')) #pass 3 values and request 3 inputs, one of which is an integer