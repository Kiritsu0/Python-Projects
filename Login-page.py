import re
from tkinter import *
from tkinter import messagebox
root = Tk()
root.title('Login Page')
root.geometry('380x440')
root.configure(bg='#234569')

def login():
    email = entry_name.get()
    password = entry_password.get()
    email_pattern = re.compile("^[a-zA-Z0-9]{3,35}@{1}gmail\.{1}com$")
    password_pattern = re.compile("^[a-zA-Z0-9]{5,40}$")
    if email_pattern.search(email) and password_pattern.search(password):
        messagebox.showinfo(title='Login Verification', message='Logged in  Successfully')
    elif email_pattern.search(email) and not password_pattern.search(password):
        if len(password) > 40:
            messagebox.showwarning(title='Login Verification', message='Very Long Password')
        elif len(password) < 5:
            messagebox.showwarning(title='Login Verification', message='Very short Password')
        else:
            messagebox.showerror(title='Login Verification', message='Invalid Password\n Only Letters and Numbers')

    elif not email_pattern.search(email) and password_pattern.search(password):
        if not email.endswith('@gmail.com'):
            messagebox.showwarning(title='Login Verification', message="Incomplete Email\n it should ends with '@gmail.com' ")
        elif len(email) > 35:
            messagebox.showwarning(title='Login Verification', message='Very Long Email')
        elif len(email)-10 < 3:
            messagebox.showwarning(title='Login Verification', message='Very short Email')
        else:
            messagebox.showerror(title='Login Verification', message='Invalid Email\n Only Letters and Numbers')
    else:
        messagebox.showerror(title='Login Verification', message='Invalid Email and Password')

frame = Frame(bg='#234569')

label = Label(frame, text='Login Here', font=('Arial', 30), bg='#234569', fg='#FFFFFF')
label_name = Label(frame, text='Email', font=('Arial', 15), bg='#234569', fg='#FFFFFF')
entry_name = Entry(frame, font=('Arial', 11), width=25, bd=3)
label_password = Label(frame, text='Password', font=('Arial', 15), bg='#234569', fg='#FFFFFF')
entry_password = Entry(frame, font=('Arial', 11), show='*', width=25, bd=3)
b = Button(frame, text='Login', font=('Arial', 15), command=login, bg='#234569')


def check():
    if entry_password.cget('show') == '*':
        entry_password.config(show='')
    else:
        entry_password.config(show='*')


b_show = Checkbutton(frame, text='Show Password', bg='#234569', command=check)

label.grid(row=0, column=0, columnspan=2, pady=40)
label_name.grid(row=1, column=0)
entry_name.grid(row=1, column=1, pady=20, ipady=4)
label_password.grid(row=2, column=0)
entry_password.grid(row=2, column=1, pady=20, ipady=4)
b.grid(row=4, column=0, columnspan=2, pady=40)
b_show.grid(row=3, column=0, pady=10)

frame.pack()

root.mainloop()
