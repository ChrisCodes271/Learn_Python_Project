#scope = the region that a variable is recognized
#a variable is only available inside the region its created
#a global and locally scoped version of a var can be made

def display_name():
    name = 'Chris'
    print(name) #this instance of name is local to the display_name function

display_name()

name = 'Chad'
print(name) #this will print Chad because the Chris variable isn't accessed globally.

def name_display(): #if no local variable is provided. A global variable will be used instead. In this instance you are using Chad!
    print(name)

name_display()