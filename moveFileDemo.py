import os

source = 'test.txt'
destination = 'D:\\Programming\\externalPythonProjectFiles\\test.txt' #You can't os.replace with a destinaiton on a different dist. (C:\,D:\,OneDrive)

try:
    if os.path.exists(destination): #check if your file already exists. Then let the user know
        print('File possessing the name {}  already exists. at {}'.format(source, destination))

    else:
        os.replace(source, destination) #os.replace will move your source test.txt to your destination with the name you want
        print('{} was moved'.format(source))
except FileNotFoundError as e:
    print(e)
    print('File not found...')
