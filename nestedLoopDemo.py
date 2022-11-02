#nested loops = Using a loop inside another (for, while)

rows = int(input('How many rows do you want? '))
columns = int(input('How many columns do you want? '))
symbol = input('Enter a symbol to use' )

for i in range(rows): #this is our outer loop
    for j in range(columns): #this is our inner loop. j is used cause... its next
        print(symbol, end = "") #the end= stops your cursor from moving.
    print()