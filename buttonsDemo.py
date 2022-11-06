# Button = You click it, it executes some code.

from tkinter import *

window = Tk()

count = 0


def click():
    global count
    count += 1
    click_window = Tk()
    label = Label(click_window,
                  text='You clicked the button {} times'.format(count))
    label.pack()

    click_window.mainloop()



photo = PhotoImage(file='Boj.png')

button = Button(window,
                text='Click me!',
                command=click,
                font=('Comic Sans', 30),
                fg='#00FF00',
                bg='Black',
                activeforeground='Black',
                activebackground='#00FF00',
                state=ACTIVE,
                image=photo,
                compound='top')
button.pack()

window.mainloop()
