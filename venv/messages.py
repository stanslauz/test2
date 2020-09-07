from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog
root = Tk()
root.title('Learn how to message')
root.geometry("1280x720")
def size(var):
    my_label=Label(root, text=horizon.get()).pack()
    root.geometry(str(horizon.get())+"x"+str(vertical.get()))

vertical = Scale(root, from_=0, to=200)
vertical.pack()
horizon = Scale(root, from_=0, to=2000, orient=HORIZONTAL)
horizon.pack()
def popup():
    swet = messagebox.askyesno("Error", 'This is errored')
    # if swet == 1:
    #     label = Label(root, text='you clicked yes').pack()
    # elif swet == 0:
    #     label1 = Label(root, text='you clicked no').pack()


def open():
    top = Toplevel()
    text = Label(top, text='hello world').pack()
    but = Button(top, text='close', command=top.destroy).pack()

def filed():
    global my_img
    root.filename = filedialog.askopenfilename()
    my_img = ImageTk.PhotoImage(Image.open(root.filename))

    my_label = Label(image=my_img).pack()
def check():
    mylabel=Label(root, text=var.get()).pack()

button1 = Button(root, text="pop up", command=popup).pack()
button2 = Button(root, text='open window', command=open).pack()
button3 = Button(root, text='open the file', command=filed).pack()
button4 = Button(root, text='resize', command=(size)).pack()
var = StringVar()

c=Checkbutton(root, text='click if you dare', variable=var, onvalue='stans', offvalue='wanderi')
c.deselect()
c.pack()
button5 = Button(root, text='context', command=check)
button5.pack()

sas = StringVar()
sas.set('one')
items = OptionMenu(root, sas, 'one','two', 'three').pack()
root.mainloop()