try:
    with open('C:\\Users\\Christopher\\OneDrive\\Desktop\\test.txt') as file:
        print(file.read()) #files auto-close if you use with open. Exceptions won't be caught

except FileNotFoundError as e:  #catch the exception.
    print(e)
    print('File not found')