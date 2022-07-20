import tkinter
from tkinter import *

window = Tk()
window.geometry("310x410")
window.title("Calculator")
window.configure(bg="#B4F1F0")


def clicked(num):
    first_num = box.get()
    box.delete(0, END)
    box.insert(0, str(first_num) + str(num))


def add():
    first_number = box.get()
    global old_value
    old_value = int(first_number)
    global math
    math = "addition"
    box.delete(0, END)


def minus():
    first_number = box.get()
    global old_value
    old_value = int(first_number)
    global math
    math = "minus"
    box.delete(0, END)


def div():
    first_number = box.get()
    global old_value
    old_value = int(first_number)
    global math
    math = "division"
    box.delete(0, END)


def mul():
    first_number = box.get()
    global old_value
    old_value = int(first_number)
    global math
    math = "multiplication"
    box.delete(0, END)

def dot():
    first_number = box.get()
    global old_value
    old_value = int(first_number)
    global math
    math = "dot"
    box.delete(0, END)


def equal():
    if math == "addition":
        new_value = box.get()
        box.delete(0, END)
        box.insert(0, int(old_value) + int(new_value))
    if math == "minus":
        new_value = box.get()
        box.delete(0, END)
        box.insert(0, int(old_value) - int(new_value))
    if math == "division":
        new_value = box.get()
        box.delete(0, END)
        box.insert(0, int(old_value) / int(new_value))
    if math == "multiplication":
        new_value = box.get()
        box.delete(0, END)
        box.insert(0, int(old_value) * int(new_value))


def clear():
    box.delete(0, END)


box = Entry(window, bg="#A8CBCA", border=5, borderwidth=6)
box.grid(row=0, column=0, columnspan=20, sticky=W + E, padx=10, pady=10, ipady=15, ipadx=72)

button1 = Button(window, text='7', command=lambda: clicked(7), height=3, width=6, fg="blue", bg="#65ABCB", border=5, activebackground="#BDD7D7")
button2 = Button(window, text='8', command=lambda: clicked(8), height=3, width=6, fg="blue", bg="#65ABCB", border=5, activebackground="#BDD7D7")
button3 = Button(window, text='9', command=lambda: clicked(9), height=3, width=6, fg="blue", bg="#65ABCB", border=5, activebackground="#BDD7D7")
bdiv = Button(window, text='/', command=div, height=3, width=6, fg="blue", bg="#65ABCB", border=5, activebackground="#BDD7D7")
button4 = Button(window, text='4', command=lambda: clicked(4), height=3, width=6, fg="blue", bg="#65ABCB", border=5, activebackground="#BDD7D7")
button5 = Button(window, text='5', command=lambda: clicked(5), height=3, width=6, fg="blue", bg="#65ABCB", border=5, activebackground="#BDD7D7")
button6 = Button(window, text='6', command=lambda: clicked(6), height=3, width=6, fg="blue", bg="#65ABCB", border=5, activebackground="#BDD7D7")
bmult = Button(window, text='*', command=mul, height=3, width=6, fg="blue", bg="#65ABCB", border=5, activebackground="#BDD7D7")
button7 = Button(window, text='1', command=lambda: clicked(1), height=3, width=6, fg="blue", bg="#65ABCB", border=5, activebackground="#BDD7D7")
button8 = Button(window, text='2', command=lambda: clicked(2), height=3, width=6, fg="blue", bg="#65ABCB", border=5, activebackground="#BDD7D7")
button9 = Button(window, text='3', command=lambda: clicked(3), height=3, width=6, fg="blue", bg="#65ABCB", border=5, activebackground="#BDD7D7")
bmin = Button(window, text='-', command=minus, height=3, width=6, fg="blue", bg="#65ABCB", border=5, activebackground="#BDD7D7")
bdot = Button(window, text='.', command=dot, height=3, width=6, fg="blue", bg="#65ABCB", border=5, activebackground="#BDD7D7")
bzero = Button(window, text="0", command=lambda: clicked(0), height=3, width=6, fg="blue", bg="#65ABCB", border=5, activebackground="#BDD7D7")
badd = Button(window, text='+', command=add, height=3, width=6, fg="blue", bg="#65ABCB", border=5, activebackground="#BDD7D7")
bequal = Button(window, text='=', command=equal, height=3, width=6, fg="blue", bg="#65ABCB", border=5, activebackground="#BDD7D7")
bclear = Button(window, text="CLEAR", command=clear, height=1, width=6, fg="blue", bg="#65ABCB", border=5, activebackground="#BDD7D7")

button1.grid(row=2, column=0, padx=10, pady=5)
button2.grid(row=2, column=1, padx=10, pady=5)
button3.grid(row=2, column=2, padx=10, pady=5)
bdiv.grid(row=2, column=3, padx=10, pady=5)
button4.grid(row=3, column=0, padx=10, pady=5)
button5.grid(row=3, column=1, padx=10, pady=5)
button6.grid(row=3, column=2, padx=10, pady=5)
bmult.grid(row=3, column=3, padx=10, pady=5)
button7.grid(row=4, column=0, padx=10, pady=5)
button8.grid(row=4, column=1, padx=10, pady=5)
button9.grid(row=4, column=2, padx=10, pady=5)
bmin.grid(row=4, column=3, padx=10, pady=5)
bdot.grid(row=5, column=0, padx=10, pady=5)
bzero.grid(row=5, column=1, padx=10, pady=5)
badd.grid(row=5, column=2, padx=10, pady=5)
bequal.grid(row=5, column=3, padx=10, pady=5)
bclear.grid(row=1, column=0, padx=10, pady=5)

window.mainloop()
