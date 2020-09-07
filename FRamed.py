from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learn how to code')
frame = LabelFrame(root, text="This is my frame", padx=50, pady=5)
frame.pack(padx=10, pady=10)

b = Button(frame, text="Don't click")
b.grid(row=0, column=0)
be = Button(frame, text="Don't click")
be.grid(row=0, column=1)

r = IntVar()
r.set(2)
Radiobutton(frame, text='option 1', variable=r, value=1, command=lambda: clicked(r.get())).grid(row=2, column=0)
Radiobutton(frame, text='option 2', variable=r, value=2, command=lambda: clicked(r.get())).grid(row=3, column=0)
label = Label(frame, text=r.get())
label.grid(row=4, column=0)


def clicked(value):
    label = Label(frame, text=value)
    label.grid(row=4, column=0)


button1 = Button(root, text='exit', command=frame.quit()).pack()

root.mainloop()
