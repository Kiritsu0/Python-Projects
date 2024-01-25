from tkinter import *
root = Tk()
root.title('Calculator')
frame = Frame()
# root.configure(bg='black')
e = Entry(frame, width=45, borderwidth=5, font=('Arial', 8))
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def click_button(number):
    # current = e.get()
    # e.delete(0, END)
    # e.insert(0, str(current) + str(number))
    e.insert(END, number)

def click_clear():
    e.delete(0, END)

def click_add():
    first_number = e.get()
    global f_num
    global math
    math = 'addition'
    f_num = int(first_number)
    e.delete(0, END)

def click_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == 'addition':
        e.insert(0, f_num + int(second_number))
    if math == 'subtraction':
        e.insert(0, f_num - int(second_number))
    if math == 'multiplication':
        e.insert(0, f_num * int(second_number))
    if math == 'division':
        e.insert(0, f_num / int(second_number))
def click_subtract():
    first_number = e.get()
    global f_num
    global math
    math = 'subtraction'
    f_num = int(first_number)
    e.delete(0, END)

def click_multiply():
    first_number = e.get()
    global f_num
    global math
    math = 'multiplication'
    f_num = int(first_number)
    e.delete(0, END)

def click_divide():
    first_number = e.get()
    global f_num
    global math
    math = 'division'
    f_num = int(first_number)
    e.delete(0, END)

#Define Buttons

b1 = Button(frame, text='1', padx=10, pady=15, command=lambda: click_button(1), font=('Arial', 15)) #,we cant add paranthesis to the call function inside the command and so no parameters
#,so we use lambda that with it we can add paranthesis with parameters
b2 = Button(frame, text='2', padx=10, pady=15, command=lambda: click_button(2), font=('Arial', 15))
b3 = Button(frame, text='3', padx=10, pady=15, command=lambda: click_button(3), font=('Arial', 15))
b4 = Button(frame, text='4', padx=10, pady=15, command=lambda: click_button(4), font=('Arial', 15))
b5 = Button(frame, text='5', padx=10, pady=15, command=lambda: click_button(5), font=('Arial', 15))
b6 = Button(frame, text='6', padx=10, pady=15, command=lambda: click_button(6), font=('Arial', 15))
b7 = Button(frame, text='7', padx=10, pady=15, command=lambda: click_button(7), font=('Arial', 15))
b8 = Button(frame, text='8', padx=10, pady=15, command=lambda: click_button(8), font=('Arial', 15))
b9 = Button(frame, text='9', padx=10, pady=15, command=lambda: click_button(9), font=('Arial', 15))
b0 = Button(frame, text='0', padx=10, pady=15, command=lambda: click_button(0), font=('Arial', 15))

b_add = Button(frame, text='+', padx=9, pady=15, command=click_add, font=('Arial', 15))
b_subtract = Button(frame, text='-', padx=9, pady=15, command=click_subtract, font=('Arial', 15))
b_multiply = Button(frame, text='x', padx=9, pady=15, command=click_multiply, font=('Arial', 15))
b_divide = Button(frame, text='/', padx=9, pady=15, command=click_divide, font=('Arial', 15))

b_equal = Button(frame, text='=', padx=60, pady=15, command=click_equal, font=('Arial', 15))
b_clear = Button(frame, text='Clear', padx=49, pady=15, command=click_clear, font=('Arial', 15))

# Put the Buttons on the screen

b1.grid(row=3, column=0, sticky=E+W)
b2.grid(row=3, column=1, sticky=E+W)
b3.grid(row=3, column=2, sticky=E+W)

b4.grid(row=2, column=0, sticky=E+W)
b5.grid(row=2, column=1, sticky=E+W)
b6.grid(row=2, column=2, sticky=E+W)

b7.grid(row=1, column=0, sticky=E+W)
b8.grid(row=1, column=1, sticky=E+W)
b9.grid(row=1, column=2, sticky=E+W)
b0.grid(row=4, column=0, sticky=E+W)

b_clear.grid(row=4, column=1, sticky=E+W, columnspan=2)
b_equal.grid(row=5, column=1, sticky=E+W, columnspan=2)

b_add.grid(row=5, column=0, sticky=E+W)
b_subtract.grid(row=6, column=0, sticky=E+W)
b_multiply.grid(row=6, column=1, sticky=E+W)
b_divide.grid(row=6, column=2, sticky=E+W)

frame.pack()

root.mainloop()
