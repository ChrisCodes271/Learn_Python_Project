from tkinter import *
from tkinter import colorchooser    #This is a submodule

def click():
    color = colorchooser.askcolor()
    colorHex = color[1]
    window.config(bg=str(colorHex)) #Change Color of background

window = Tk()
window.geometry('400x400')
button = Button(text='Click me',command=click)
button.pack()
window.mainloop()