#Label = area widget that holds text and/or an image within a window.

from tkinter import *

window = Tk()
window.resizable()
photo = PhotoImage(file='Boj.png')

label = Label(window,
              text="Hello World!",
              font=('Arial', 32, 'bold'),
              foreground='#260047',
              background='#272727',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound='top')
label.pack()  # will pack in the top middle
#label.place(x=0,y=0) # Place at coords.

window.mainloop()