from tkinter import *
from tkinter.font import Font
from tkinter import filedialog
import pickle

root = Tk()
root.geometry('500x500')
root.title('A To-Do List')

font = Font(family='Elephant', size=30, weight='bold')

#Create frame
frame = Frame(root)
frame.pack(pady=20)

#Create listbox
list = Listbox(frame, font=font, width=15, height=5, bg='SystemButtonFace',bd=0,fg='#464646', highlightthickness=0,selectbackground='#a6a6a6', activestyle="none")

list.pack(side=LEFT, fill=BOTH)

#Create Scroll bar
scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=BOTH)

#Add scrollbar
list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=list.yview)

#Create entry box to add items to the list
entry = Entry(root, font=('Elephant', 20), width=20)
entry.pack(pady=20)

#create a button frame
button_frame = Frame(root)
button_frame.pack(pady=20)

#Functions
def enter(event):
    if event.keysym == 'Return':
        list.insert(END, entry.get())
        entry.delete(0, END)
entry.bind('<Return>', enter)

def delete_item():
    list.delete(ANCHOR)

def add_item():
    list.insert(END, entry.get())
    entry.delete(0, END)

def crossoff_item():
    #Cross off item
    try:
        list.itemconfig(ANCHOR, fg='#dedede')

    #Get rid of selection bar
        list.selection_clear(0, END)
    except:
        pass

def uncross_item():
    #Cross off item
    try:
        list.itemconfig(list.curselection(), fg='#464646')
    #Get rid of selection bar
        list.selection_clear(0, END)
    except:
        pass

def delete_crossed():
    count = 0
    while count < list.size():
        if list.itemcget(count, 'fg') == '#dedede':
            list.delete(list.index(count))
            count -= 1
        count += 1

def save_list():
    file_name = filedialog.asksaveasfilename(initialdir='C:/', title='Save File', filetypes=(('Dat Files', '*.dat'), ('All Files', '*.*')))
    if file_name:
        if file_name.endswith('.dat'):
            pass
        else:
            file_name = f'{file_name}.dat'

    #grab all stuff from the list
    stuff = list.get(0, END)

    #open the file
    output_file = open(file_name, 'wb')
    #Actually add the stuff to the file
    pickle.dump(stuff, output_file)

def open_list():
    file_name = filedialog.askopenfilename(initialdir='C:/', title='Open File', filetypes=(('Dat Files', '*.dat'), ('All Files', '*.*')))
    if file_name:
        #Delete currently open list
        list.delete(0, END)
        #open the file
        input_file = open(file_name, 'rb')
        #Load the data from the file
        stuff = pickle.load(input_file)
        #Output stuff to the screen
        for item in stuff:
            list.insert(END, item)

def clear_list():
    list.delete(0,END)
#Create Menu
menu = Menu(root)
root.config(menu=menu)

#Add items to the menu
file_menu = Menu(menu, tearoff=False)
menu.add_cascade(label='File', menu=file_menu)

#Add dropdown items
file_menu.add_command(label='Save List', command=save_list)
file_menu.add_command(label='Open List', command=open_list)
file_menu.add_separator()
file_menu.add_command(label='Clear List', command=clear_list)


#Add some buttons
delete_button = Button(button_frame, text='Delete Item', command=delete_item)
add_button = Button(button_frame, text='Add Item', command=add_item)
crossoff_button = Button(button_frame, text='Cross Off Item', command=crossoff_item)
uncross_button = Button(button_frame, text='Uncross Item', command=uncross_item)
delete_crossed_items = Button(button_frame, text='Delete Crossed Items', command=delete_crossed)

delete_button.grid(row=0, column=0, padx=5)
add_button.grid(row=0, column=1, padx=5)
crossoff_button.grid(row=0, column=2, padx=5)
uncross_button.grid(row=0, column=3, padx=5)
delete_crossed_items.grid(row=0, column=4, padx=5)

root.mainloop()
