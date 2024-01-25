from tkinter import *
import time

root = Tk()
root.title('Timer and clock')
root.geometry('600x400')

def clock():
    hour = time.strftime('%I')#you can replace the %H with %I that writes the hours in 1 to 12 hours while %H  writes the houres according to /24
    minute = time.strftime('%M')
    second = time.strftime('%S')
    day = time.strftime('%A')#day of the week
    am_pm = time.strftime('%p')
    time_zone = time.strftime('%Z')#it prints the time that your country is working on

    label.config(text=hour + ':' + minute + ':' + second + ' ' + am_pm)
    label.after(1000, clock)

    label2.config(text=time_zone + ' ' + day)

def update():
    label.config(text='5 seconds later')

label = Label(root, text='', font=('Helvetica', 48), fg='green', bg='black')
label.pack(pady=20)

label2 = Label(root, text='', font=('Helvetica', 14))
label2.pack(pady=20)
# label.after(5000, update)#after its like sleep but it works in a different way from sleep in time module and takes the time in millisecond
#  so 5000 is 5 second
clock()

root.mainloop()
