from tkinter import *

window = Tk()

def display():
    if(x.get()==1):
        print('You agree')
    else:
        print('You dont agree')

x = IntVar()  # Can also use StrVar
photo = PhotoImage(file='Boj.png')

check_button = Checkbutton(window,
                           text='I agree to this',
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=display,
                           font=('Times New Roman', 30),
                           fg='green',
                           bg='black',
                           activebackground='green',
                           activeforeground='black',
                           padx=25,
                           pady=15,
                           image=photo,
                           compound="top")
check_button.pack()

window.mainloop()