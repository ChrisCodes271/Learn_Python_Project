from tkinter import *

# This will import everything related to the tkinter module
# widgets - GUI elements: buttons, textboxes, labels, images
# windows - serves as a container to hold or contain widgets

window = Tk()  # instantiate and instance of a window
window.geometry("1920x1080")  # set resolution
window.title("My first GUI program.")
icon = PhotoImage(file='Boj.png')  # make variable icon referencing Boj.
window.iconphoto(True, icon)  # change icon
window.config(background='#260047')  # window.config that lets you change things, like the background color

window.mainloop()  # Place window on screen
