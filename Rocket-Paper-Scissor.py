from tkinter import *
from random import randint
from tkinter import ttk

root = Tk()
root.title('Rock, Paper, Scissors')
root.geometry('500x600')

# Change the bg color to white
root.config(bg='white')

#Define our images
rock = PhotoImage(file='C:/Users/Hello/Documents/Downloads/Stone.png')
scissor = PhotoImage(file='C:/Users/Hello/Documents/Downloads/Scissor.png')
paper = PhotoImage(file='C:/Users/Hello/Documents/Downloads/Paper.png')

#Add Images to a list
image_list = [rock, paper, scissor]

#pick random number between 0 and 2
pick_number = randint(0, 2)

#Throw up an  image when the program starts
image_label = Label(root, image=image_list[pick_number], bg='white', bd=0)
image_label.pack(pady=20)

#Create spin Function
def spin():
    # Pick random number
    pick_number = randint(0, 2)
    # Show image
    image_label.config(image=image_list[pick_number])
    # 0 = Rock
    # 1 = Paper
    # 2 = Scissors

    # Determine if you win or lose or draw
    if user_choice.get() =='Rock':
        if pick_number == 1:
            win_lose_label.config(text='You Lose')
        elif pick_number == 2:
            win_lose_label.config(text='You Win')
        elif pick_number == 0:
            win_lose_label.config(text='Draw')

    elif user_choice.get() == 'Paper':
        if pick_number == 0:
            win_lose_label.config(text='You Win')
        elif pick_number == 2:
            win_lose_label.config(text='You Lose')
        elif pick_number == 1:
            win_lose_label.config(text='Draw')

    elif user_choice.get() == 'Scissor':
        if pick_number == 0:
            win_lose_label.config(text='You Lose')
        elif pick_number == 1:
            win_lose_label.config(text='You Win')
        elif pick_number == 2:
            win_lose_label.config(text='Draw')

#make our choice
user_choice = ttk.Combobox(root, value=('Rock', 'Paper', 'Scissor'))
user_choice.current(0)
user_choice.pack(pady=20)

#Create Spin Button
spin_button = Button(root, text='Spin', command=spin)
spin_button.pack(pady=10)

# label for showing if you won or not
win_lose_label = Label(root, text='', font=('Helvetica', 18), bg='white')
win_lose_label.pack(pady=50)

root.mainloop()