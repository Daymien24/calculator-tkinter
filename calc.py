from tkinter import *

root = Tk()

entry = Entry(root,width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def click(number):
    #entry.delete(0, END)
    liczba = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(liczba) + str(number))

def add():
    first_number = entry.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    entry.delete(0, END)

def equal():
    second_number = entry.get()
    entry.delete(0, END)
    if math == "addition":
        entry.insert(0, f_num + int(second_number))
    if math == "substraction":
        entry.insert(0, f_num - int(second_number))
    if math == "multiplication":
        entry.insert(0, f_num * int(second_number))
    if math == "division":
        entry.insert(0, f_num / int(second_number))

def substract():
    first_number = entry.get()
    global f_num
    global math
    math = "substraction"
    f_num = int(first_number)
    entry.delete(0, END)

def multiply():
    first_number = entry.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    entry.delete(0, END)

def divide():
    first_number = entry.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    entry.delete(0, END)


button1 = Button(root, text='1', padx=40, pady=20, command=lambda: click(1))
button2 = Button(root, text='2', padx=40, pady=20, command=lambda: click(2))
button3 = Button(root, text='3', padx=40, pady=20, command=lambda: click(3))
button4 = Button(root, text='4', padx=40, pady=20, command=lambda: click(4))
button5 = Button(root, text='5', padx=40, pady=20, command=lambda: click(5))
button6 = Button(root, text='6', padx=40, pady=20, command=lambda: click(6))
button7 = Button(root, text='7', padx=40, pady=20, command=lambda: click(7))
button8 = Button(root, text='8', padx=40, pady=20, command=lambda: click(8))
button9 = Button(root, text='9', padx=40, pady=20, command=lambda: click(9))
button0 = Button(root, text='0', padx=40, pady=20, command=lambda: click(0))
add = Button(root, text='+', padx=38, pady=20, command=add)
substract = Button(root, text='-', padx=41, pady=20, command=substract)
multiply = Button(root, text='*', padx=38, pady=20, command=multiply)
divide = Button(root, text='/', padx=38, pady=20, command=divide)
equal = Button(root, text='=', padx=88, pady=20, command=equal)
clear = Button(root, text='Clear', padx=79, pady=20, command=lambda: click())
# Put the buttons on the screen
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0)

add.grid(row=5, column=0)
equal.grid(row=5, column=1, columnspan=2)
clear.grid(row=4, column=1, columnspan=2)

substract.grid(row=6, column=0)
multiply.grid(row=6, column=1)
divide.grid(row=6, column=2)

root.mainloop()
