#Loop controls = changes a loops execution from normal sequence

#break - terminates the loop
while True:
    name = input("Enter your name: ")
    if name != "": #this break acts as input validation. If they don't enter anything, the sequence won't continue so you can't execute the break in the while statement
        break

#continue - skips the next iteration of a loop
phone_number = '773-202-6325'

for i in phone_number:
    if i == "-":
        continue
    print(i,end="")

#pass control acts as a placeholder. This will skip over 13 and then all other numbers can continue to the else statement.
for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i)