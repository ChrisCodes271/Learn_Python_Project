# listbox = a listing of selectable text items within its own container

from tkinter import *

def submit():
    order = []
    for index in my_listbox.curselection():
        order.insert(index,my_listbox.get(index))
    for index in order:
        print('You have ordered {}'.format(index))

def add():
    my_listbox.insert(my_listbox.size(),entry_box.get())
    my_listbox.config(height=my_listbox.size())

def delete():
    for index in reversed(my_listbox.curselection()):
        my_listbox.delete(index)
    my_listbox.config(height=my_listbox.size())

window = Tk()

my_listbox = Listbox(window,
                     bg='#f7ffde',
                     font=('Arial', 24),
                     width=12,
                     selectmode=MULTIPLE)
my_listbox.pack()

my_listbox.insert(1,'Pizza')
my_listbox.insert(2,'Pasta')
my_listbox.insert(3,'Garlic Bread')
my_listbox.insert(4,'Soup')
my_listbox.insert(5,'Salad')

my_listbox.config(height=my_listbox.size())

entry_box = Entry(window)
entry_box.pack()

submit_button = Button(window,
                       text='Submit',
                       command=submit)
submit_button.pack()

add_button = Button(window,
                    text='Add',
                    command=add)
add_button.pack()

delete_button = Button(window,
                    text='Delete',
                    command=delete)
delete_button.pack()


window.mainloop()
