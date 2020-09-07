from tkinter import *

root = Tk()

e = Entry(root, width=50, borderwidth=5,bg="yellow")
e.pack()
e.insert(0, "eka jina")

def myClick():
    myLabel = Label(root, text =e.get())
    myLabel.pack()


def myName():
    named = Label(root, text="my name is stanslaus wanderi")
    named.pack()


myButton = Button(root, text="click me", command=myClick, fg="green", bg="black")
myButton.pack()

root.mainloop()
