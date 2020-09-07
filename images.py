from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("This is my code")
# root.iconbitmap('C/')


my_img = ImageTk.PhotoImage(Image.open("stans.jpg"))
my_img1 = ImageTk.PhotoImage(Image.open("stans1.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("stans2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("stans3.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("stans4.jpg"))

image_list = [my_img, my_img1, my_img2, my_img3, my_img4]
my_label = Label(image=my_img, width=300, height=300)
my_label.grid(row=0, column=0, columnspan=3)

status = Label(root, text='image 1 of ' + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
status.grid(row=2, column=0, columnspan=3, sticky=W + E)


def forwarding(number):
    global my_label
    global buttonforward
    global buttonreverse
    my_label.grid_forget()
    my_label = Label(image=image_list[number - 1], width=300, height=300)
    my_label.grid(row=0, column=0, columnspan=3)
    buttonforward = Button(root, text=">>", command=lambda: forwarding(number + 1))
    buttonforward.grid(column=2, row=1)
    buttonreverse = Button(root, text="<<", command=lambda: backwarding(number-1))
    buttonreverse.grid(column=0, row=1)

    status = Label(root, text='image ' + str(number) + ' of ' + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


def backwarding(number):
    global my_label
    global buttonforward
    global buttonreverse
    my_label = Label(image=image_list[number - 1], width=300, height=300)
    my_label.grid(row=0, column=0, columnspan=3)
    buttonforward = Button(root, text=">>", command=lambda: forwarding(number + 1))
    buttonforward.grid(column=2, row=1)
    buttonreverse = Button(root, text="<<", command=lambda: backwarding(number - 1))
    buttonreverse.grid(column=0, row=1)
    status = Label(root, text='image ' + str(number) + ' of ' + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


buttonforward = Button(root, text=">>", command=lambda: forwarding(number=2))
buttonforward.grid(column=2, row=1)

# buttonreverse = Button(root, text="<<", command=lambda: forwarding(number=2))
# buttonreverse.grid(column=0, row=1)

button_quit = Button(root, text='Exit program', command=root.quit)
button_quit.grid(column=1, row=1)
root.mainloop()
