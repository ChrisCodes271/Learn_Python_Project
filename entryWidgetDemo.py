# Entry widget accepts a single line of user input

from tkinter import  *

def submit():  # Define submit function.
    username = entry.get()
    print('Hello ' + username)
    entry.config(state=DISABLED) # You can use entry.config at end of button executed function to disable entry.

def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get())-1) # Get length of entry.get and subtract 1 to delete 1 character at the end.

window = Tk()

entry = Entry(window,
              font=('Times New Roman', 44),
              fg='Green',
              bg='Black',
              show='*')
entry.insert(0,'Your password here')
entry.pack(side=LEFT)

submit_button = Button(window,text='Submit',command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window,text='Delete',command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window,text='Backspace',command=backspace)
backspace_button.pack(side=RIGHT)

window.mainloop()