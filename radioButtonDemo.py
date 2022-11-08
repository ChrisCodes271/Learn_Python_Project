# Radio button = similar to checkboxes, but you can only select one from a grouping

from tkinter import *

food = ["Pizza", "Hamburger", "Hotdog"]

def order():
    if(x.get()==0):
        print('You ordered pizza!')
    elif(x.get()==1):
        print('You ordered a hamburger')
    elif(x.get()==2):
        print('You ordered a hotdog')
    else:
        print('Huh?')


window = Tk()

pizza_Image = PhotoImage(file='C:\\Users\\Christopher\\Downloads\\pizza.png')
hamburger_Image = PhotoImage(file='C:\\Users\\Christopher\\Downloads\\hamburger.png')
hotdog_Image = PhotoImage(file='C:\\Users\\Christopher\\Downloads\\hotdog.png')

pizza_Image.configure(height=250, width=250)
hamburger_Image.configure(height=250, width=250)
hotdog_Image.configure(height=250, width=250)

food_Images = [pizza_Image, hamburger_Image, hotdog_Image]

x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index],  # Add text to radio buttons
                              variable=x,  # Groups radio buttons together if they share the same variable
                              value=index,  # You have to add a value to your radio button to work.
                              padx=25,
                              pady=15,
                              font=('Arial', 30),
                              image=(food_Images[index]),  # Adds image to radio button
                              indicatoron=0,
                              command=order) # Set command of radio button to function.
    radiobutton.pack(anchor=W)




window.mainloop()