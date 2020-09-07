from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("Calculator")
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_add(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def cleared():
    e.delete(0, END)


def addb():
    first = e.get()
    global sign
    sign = "+"
    global first_number
    first_number = int(first)
    e.delete(0, END)


def sub():
    first = e.get()
    global sign
    sign = "-"
    global first_number
    first_number = int(first)
    e.delete(0, END)


def mul():
    first = e.get()
    global sign
    sign = "*"
    global first_number
    first_number = int(first)
    e.delete(0, END)


def div():
    first = e.get()
    global sign
    sign = "/"
    global first_number
    first_number = int(first)
    e.delete(0, END)


def equal():
    second = e.get()
    e.delete(0, END)
    if sign == "+":
        result = int(second) + first_number
        e.insert(0, result)
    elif sign == "-":
        result = first_number - int(second)
        e.insert(0, result)
    elif sign == "*":
        result = int(second) * first_number
        e.insert(0, result)
    elif sign == "/":
        result = first_number / int(second)
        e.insert(0, result)
    messagebox.showinfo("Answer", result)

button1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_add(1))
button1.grid(row=3, column=0)

button2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_add(2))
button2.grid(row=3, column=1)

button3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_add(3))
button3.grid(row=3, column=2)

button4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_add(4))
button4.grid(row=2, column=0)

button5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_add(5))
button5.grid(row=2, column=1)

button6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_add(6))
button6.grid(row=2, column=2)

button7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_add(7))
button7.grid(row=1, column=0)

button8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_add(8))
button8.grid(row=1, column=1)

button9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_add(9))
button9.grid(row=1, column=2)

button0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_add(0))
button0.grid(row=4, column=0)

buttonaddd = Button(root, text="+", padx=40, pady=20, command=addb)
buttonaddd.grid(row=5, column=0)

buttonclear = Button(root, text="Clear", padx=77, pady=20, command=cleared)
buttonclear.grid(row=4, column=1, columnspan=2)

buttonequals = Button(root, text="=", padx=87, pady=20, command=equal)
buttonequals.grid(row=5, column=1, columnspan=2)

buttonsub = Button(root, text="-", padx=40, pady=20, command=sub)
buttonsub.grid(row=6, column=0)

buttondiv = Button(root, text="/", padx=40, pady=20, command=div)
buttondiv.grid(row=6, column=1)

buttonmul = Button(root, text="*", padx=40, pady=20, command=mul)
buttonmul.grid(row=6, column=2)
# button3 = Button(root, text="3")
# button3.grid(row=1, column=3)


root.mainloop()
