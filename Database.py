from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title('Database')
root.geometry('400x400')

conn = sqlite3.connect('address_book.db')
c = conn.cursor()

# c.execute(""" CREATE TABLE addresses(
#         first_name text,
#         last_name text,
#         address text,
#         city text,
#         state text,
#         zipcode integer
#         )""")


# declaring
global f_name
global address
global city
global state
global zipcode


# global delete_box

def submit():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
              {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'address': address.get(),
                  'city': city.get(),
                  'state': state.get(),
                  'zipcode': zipcode.get()

              })

    conn.commit()
    conn.close()

    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


def query():
    global delete_box
    global top
    top = Toplevel()
    top.title('RECORDS')
    top.geometry('400x400')
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    print_records = ''

    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + "\t" + str(record[6]) + "\n"
    queryable = Label(top, text=print_records)
    queryable.grid(row=0, column=1, columnspan=2)

    conn.commit()
    conn.close()

    dlt = Button(top, text='delete', command=delete)
    dlt.grid(row=4, column=1)
    delete_box = Entry(top, width=30)
    delete_box.grid(row=4, column=0)

    but = Button(top, text='close', command=top.destroy)
    but.grid(row=5, column=0)


def delete():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    c.execute("DELETE from addresses WHERE oid=" + delete_box.get())
    records = c.fetchall()
    print_records = ''

    conn.commit()
    conn.close()
    # f_name.delete(0, END)
    # l_name.delete(0, END)
    # address.delete(0, END)
    # address.delete(0, END)
    # city.delete(0, END)
    # state.delete(0, END)
    # zipcode.delete(0, END)


def edited():
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    c.execute("SELECT * from addresses WHERE oid=" + editxt.get())
    records = c.fetchall()
    for record in records:
        f_name.insert(0, record[0])
        l_name.insert(0, record[1])
        address.insert(0, record[2])
        city.insert(0, record[3])
        state.insert(0, record[4])
        zipcode.insert(0, record[5])
    c.close()


def save():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    # record_id = delete_box.get()
    c.execute("""UPDATE addresses SET
        first_name = :first,
        last_name = :last,
        address = :address,
        city = :city,
        state = :state,
        zipcode = :zipcode     
     
        WHERE oid = :oid""",
              {'first': f_name.get(),
               'last': l_name.get(),
               'address': address.get(),
               'city': city.get(),
               'state': state.get(),
               'zipcode': zipcode.get(),
               'oid': delete_box.get()

               })
    conn.commit()
    conn.close()


f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)

address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)

city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)

state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)

# labels

first_namelabel = Label(root, text='First Name:')
first_namelabel.grid(row=0, column=0)

last_namelabel = Label(root, text='Last Name:')
last_namelabel.grid(row=1, column=0)

addresslabel = Label(root, text='Address:')
addresslabel.grid(row=2, column=0)

citylabel = Label(root, text='City:')
citylabel.grid(row=3, column=0)

statelabel = Label(root, text='State:')
statelabel.grid(row=4, column=0)

zipcodelabel = Label(root, text='Zipcode:')
zipcodelabel.grid(row=5, column=0)

sub = Button(root, text='Submit', command=submit)
sub.grid(row=6, column=0, columnspan=2, pady=10, padx=10)

querybtn = Button(root, text='show record', command=query)
querybtn.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

editbtn = Button(root, text='Edit', command=edited)
editbtn.grid(row=7, column=1)
savebtn = Button(root, text='Save', command=save)
savebtn.grid(row=7, column=2)

editxt = Entry(root, width=30)
editxt.grid(row=7, column=0)

conn.commit()
conn.close()

root.mainloop()
