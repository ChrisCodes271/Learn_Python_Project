from tkinter import *

def submit():
    print('The temparature is: ' + str(scale.get()) + ' degrees C')

window = Tk()

hot_Image = PhotoImage(file='pixelFlame.png')
cold_Image = PhotoImage(file='pixelIce.png')
hot_Label = Label(image=hot_Image)
cold_label = Label(image=cold_Image)


hot_Label.pack()

scale = Scale(window,
              from_=100, #From value denotes bottom
              to=0,
              length=500,
              orient=VERTICAL,
              font=('Consolas',25),
              tickinterval=10,
              showvalue=FALSE,
              troughcolor='Black')

scale.pack()

cold_label.pack()

button = Button(window,
                text='Submit',
                command=submit)
button.pack()




window.mainloop()