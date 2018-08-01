from tkinter import *

#creating a window object

window = Tk()

#define labels
l1 = Label(window, text="Face Recognition and Detection System")
l1.grid(row=0, column=0)

l2 = Label(window, text ="Detect Face")
l2.grid(row=10, column=2)

l3 = Label(window, text ="Train Face")
l3.grid(row=10,column=3)

l4 = Label(window, text ="Recognize Face")
l4.grid(row=10,column=4)


window.mainloop()

