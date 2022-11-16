from tkinter import *
from tkinter import messagebox

def click():
    pass
    #messagebox.showinfo(title="This is a message box",message='Hello World!')
    #messagebox.showwarning(title='OH NO!',message='You have a warning...')
    #messagebox.showerror(title='ERROR',message='Something went wrong...')
   #if messagebox.askokcancel(title='Ask ok cancel',message='Do you want to do the thing?') : <-- This will ask y/n
       #print('You did the thing')
   #else:
       #print('You cancelled...')

window = Tk()

button = Button(window,command=click,text='click me')

button.pack()

window.mainloop()