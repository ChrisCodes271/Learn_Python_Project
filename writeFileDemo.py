text = 'Hello\nThis is a bit of text\nHave a good one.'  # the \n will put text on the next line.

with open('test.txt','w') as file: #the ,'w' will write a file. You can also pass ,'r' to read a file
    file.write(text) #this will pass whatever text is in my 'text' variable to the newly created file

text = 'Oops. File overwritten.\n' #the most recent text definition will overwrite it.

with open('test.txt','w') as file:
    file.write(text) #this will pass whatever text is in my 'text' variable to the newly created file


text = 'Thats okay.\nWe can just append what we want on the end\nHello\nThis is a bit of text\nHave a good one. '

with open('test.txt','a') as file: #the 'a' will append text's new definition to the end.
    file.write(text)