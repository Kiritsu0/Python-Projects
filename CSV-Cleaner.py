from tkinter import *
from tkinter import filedialog
import pandas as pd

window = Tk()
window.geometry('300x200')
window.title('CSV Files Cleaner')
window.config(bg='Gray')

def save():
    save_file = filedialog.asksaveasfilename(initialdir='C:/', title='Save File', filetypes=(('csv files', '*.csv'), ('all files', '*.*')))
    modification.to_csv(save_file)

def return_back():
    if 'bs' in globals():
        bs.pack_forget()
    # if 'br' in globals():
    br.pack_forget()
    bo.pack_forget()
    label2.pack_forget()
    clean_buttons()

def drop_na():
    b1.pack_forget()
    b2.pack_forget()
    b3.pack_forget()
    b4.pack_forget()

    global modification
    modification = df.dropna()
    global bs, br
    bs = Button(window, text='Save', width=15, font=('Arial', 11), command=save)
    br = Button(window, text='Back', width=15, font=('Arial', 11), command=return_back)
    bs.pack(pady=5)
    br.pack(pady=5)

def drop_duplicates():
    b1.pack_forget()
    b2.pack_forget()
    b3.pack_forget()
    b4.pack_forget()

    global modification
    modification = df.drop_duplicates()
    global bs, br
    bs = Button(window, text='Save', width=15, font=('Arial', 11), command=save)
    br = Button(window, text='Back', width=15, font=('Arial', 11), command=return_back)
    bs.pack(pady=5)
    br.pack(pady=5)

def sort():
    b1.pack_forget()
    b2.pack_forget()
    b3.pack_forget()
    b4.pack_forget()

    global bs_values, bs_index
    bs_values = Button(window, text='Sort Values', width=15, font=('Arial', 11), command=sort_values)
    bs_index = Button(window, text='Sort Index', width=15, font=('Arial', 11), command=sort_index)
    bs_values.pack(pady=5)
    bs_index.pack(pady=5)
    
    global modification
    modification = df.drop_duplicates()

def sort_values():
    bs_values.pack_forget()
    bs_index.pack_forget()
    global entry
    entry = Entry(window, width=26, font=('Arial', 11))
    entry.insert(END, 'Name Column to Sort by')
    entry.pack(pady=5)

    def check_column_sort(event):
        if event.keysym == 'Return':
            if entry.get() in df.columns:
                entry.pack_forget()
                global modification
                modification = df.sort_values(entry.get())
                global bs, br
                bs = Button(window, text='Save', width=15, font=('Arial', 11), command=save)
                br = Button(window, text='Back', width=15, font=('Arial', 11), command=return_back)
                bs.pack(pady=5)
                br.pack(pady=5)
            else:
                entry.delete(0, END)
                entry.insert(END, 'Column Not Found')
    entry.bind('<Return>', check_column_sort)

def sort_index():
    bs_values.pack_forget()
    bs_index.pack_forget()
    global modification
    modification = df.sort_index()
    global bs, br
    bs = Button(window, text='Save', width=15, font=('Arial', 11), command=save)
    br = Button(window, text='Back', width=15, font=('Arial', 11), command=return_back)
    bs.pack(pady=5)
    br.pack(pady=5)

def merge():
    b1.pack_forget()
    b2.pack_forget()
    b3.pack_forget()
    b4.pack_forget()
    global bo, label2
    bo = Button(window, text='Open Folder', width=15, font=('Arial', 11), command=dialog2)
    label2 = Label(window, text='Select another file to merge it with the first', font=('Arail', 9), bg='gray')
    label2.pack()
    bo.pack(pady=10)
    global br
    br = Button(window, text='Back', width=15, font=('Arial', 11), command=return_back)
    br.pack(pady=5)

def merging():
    entry = Entry(window, width=26, font=('Arial', 11))
    entry.insert(END, 'Name Column to merge on')
    entry.pack(pady=5)
    try:
        def check_column_sort(event):
            if 'label3' in globals():
                label3.pack_forget()
            if event.keysym == 'Return':
                if entry.get() in df.columns and entry.get() in df2.columns:
                    entry.pack_forget()
                    global modification
                    modification = pd.merge(df, df2, on=entry.get())
                    global bs, br
                    bs = Button(window, text='Save', width=15, font=('Arial', 11), command=save)
                    br = Button(window, text='Back', width=15, font=('Arial', 11), command=return_back)
                    bs.pack(pady=5)
                    br.pack(pady=5)
                else:
                    entry.delete(0, END)
                    entry.insert(END, 'Column Not Found')
        entry.bind('<Return>', check_column_sort)
    except:
        global label3
        label3 = Label(window, text='Something wrong with the files')
        label3.pack()

def clean_buttons():
    global b1, b2, b3, b4
    b1 = Button(window, text='Drop NA', width=15, font=('Arial', 11), command=drop_na)
    b2 = Button(window, text='Drop Duplicates', width=15, font=('Arial', 11), command=drop_duplicates)
    b3 = Button(window, text='Sort', width=15, font=('Arial', 11), command=sort)
    b4 = Button(window, text='Merge', width=15, font=('Arial', 11), command=merge)

    b1.pack(pady=5)
    b2.pack(pady=5)
    b3.pack(pady=5)
    b4.pack(pady=5)

global second
second = False

def dialog():
    global label
    if 'label' in globals():
        label.pack_forget()
    global file_name
    file_name = filedialog.askopenfilename(initialdir='C:/', title='Open File',filetypes=(('csv files', '*.csv'), ('all files', '*.*')))

    if  not file_name.endswith('.csv') and file_name != None:
        label = Label(window, text='Invalid File\n Only csv Files', font=('Arial', 20), bg='grey')
        label.pack()

    elif second == True:
        worked =True
        try:
            global df2
            df2 = pd.read_csv(file_name)
        except:
            label = Label(window, text='Something Wrong with the file', font=('Arial', 20), bg='gray')
            label.pack()
            worked = False
        if worked == True:
            bo.pack_forget()
            label2.pack_forget()
            br.pack_forget()
            merging()
    else:
        worked =True
        try:
            global df
            df = pd.read_csv(file_name)
        except:
            label = Label(window, text='Something Wrong with the file', font=('Arial', 20), bg='gray')
            label.pack()
            worked = False
        if worked == True:
            b1.pack_forget()
            clean_buttons()

def dialog2():
    global second
    second = True
    dialog()

b1 = Button(window, text='Open Folder', width=15, font=('Arial', 11), command=dialog)
b1.pack(pady=50)


window.mainloop()