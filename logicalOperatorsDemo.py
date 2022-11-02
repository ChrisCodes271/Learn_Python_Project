#lotical operators (and,or,not) = used to check conditional statements

temp = int(input("What temp is it outside? "))

if not(temp >= 45 and temp <= 70):
    print("It's cold!")
    print('Bring a jacket!')
elif not(temp <= 44 and temp >= 0): #the not operator acts to reverse statements.
    print('The temp is great today!')
    print('Go touch some grass!')
