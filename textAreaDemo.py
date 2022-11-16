from tkinter import *

# Text widget = functions like a text area, you can enter multiple lines of text

def submit():
    input = text.get("1.0",END)
    print(input)

window = Tk()

text = Text(window)
text.pack()
button = Button(window,text='Submit',command=submit)
button.pack()

window.mainloop()