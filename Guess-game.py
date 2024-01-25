from tkinter import *
from random import randint

root = Tk()
root.geometry('500x500')
root.title('Guess Game')

level_num = 1
level = Label(root, text=f'Level {level_num}', font=('Elephant', 25))
level.pack(pady=5)

num_label = Label(root, text='Pick A Number\nBetween 1 and 10',font=('Elephant', 30))
num_label.pack(pady=10)
guess_num = 3

def replay():
    global level_num
    level_num = 1
    level.config(text=f'Level {level_num}')
    b.pack_forget()
    quit.pack_forget()
    play_game()

def play_game():
    def guesser_button():
        global guess_num
        global bc
        if level.cget('text') == 'Level 1':
            if guess_box.get().isdigit() and guess_num > 0:
                if int(guess_box.get()) >= 1 and int(guess_box.get()) <= 10:
                    #reset our label
                    num_label.config(text="Pick A Number\nBetween 1 and 10")
                    #Find out how far away our pick was from the actual number
                    dif = abs(num - int(guess_box.get()))

                    #check to see if correct
                    if int(guess_box.get()) == num:
                        bc = 'SystemButtonFace'
                        num_label.config(text='Correct')
                        guess_button.config(state=DISABLED)
                        global level_num
                        level_num = level_num + 1
                        level.config(text=f'Level {level_num}')

                    elif dif == 5:
                        #set background color to white
                        bc = 'purple'
                    elif dif < 5:
                        bc = f'#ff{dif}{dif}{dif}{dif}'
                         #change the background of the app
                        root.config(bg=bc)
                        #change background of label
                        num_label.config(bg=bc)
                        num_guess.config(bg=bc)
                        level.config(bg=bc)
                    elif dif < 5:
                        bc = f'#{dif}{dif}{dif}{dif}ff'
                        #change the background of the app
                        root.config(bg=bc)
                        #change background of label
                        num_label.config(bg=bc)
                        num_guess.config(bg=bc)
                        level.config(bg=bc)

                    # #change the background of the app
                    # root.config(bg=bc)
                    # #change background of label
                    # num_label.config(bg=bc)
                    # num_guess.config(bg=bc)
                    # level.config(bg=bc)

                    if num_label.cget('text') != 'Correct' and guess_box.get().isdigit():
                        guess_num = guess_num - 1
                        num_guess.config(text=f'Guess:{guess_num}')

                    if guess_num <= 0 and guess_box.get().isdigit():
                        bc = 'SystemButtonFace'
                        num_label.config(text='You Lose\nYou Are Out Of Guesses')
                        guess_button.config(state=DISABLED)

                elif int(guess_box.get()) > 10 or int(guess_box.get()) < 1:
                    bc = 'SystemButtonFace'
                    num_label.config(text='Invalid Number\nOnly Between 1 and 10')

            else:
                #Delete entry and throw error message
                num_label.config(text="That's not a Number")


        elif level.cget('text') == 'Level 2':
                if guess_box.get().isdigit() and guess_num > 0:
                    if int(guess_box.get()) >= 1 and int(guess_box.get()) <= 10:
                        #reset our label
                        num_label.config(text="Pick A Number\nBetween 1 and 10")
                        #Find out how far away our pick was from the actual number
                        dif = abs(num - int(guess_box.get()))

                        #check to see if correct
                        if int(guess_box.get()) == num:
                            bc = 'SystemButtonFace'
                            num_label.config(text='Correct')
                            guess_button.config(state=DISABLED)
                            level_num = level_num + 1
                            level.config(text=f'Level {level_num}')

                        elif dif == 5:
                            #set background color to white
                            bc = 'purple'
                        elif dif < 5:
                            bc = f'#ff{dif}{dif}{dif}{dif}'
                        elif dif < 5:
                            bc = f'#{dif}{dif}{dif}{dif}ff'

                        #change the background of the app
                        root.config(bg=bc)
                        #change background of label
                        num_label.config(bg=bc)
                        num_guess.config(bg=bc)
                        level.config(bg=bc)

                        if num_label.cget('text') != 'Correct' and guess_box.get().isdigit():
                            guess_num = guess_num - 1
                            num_guess.config(text=f'Guess:{guess_num}')

                        if guess_num <= 0 and guess_box.get().isdigit():
                            bc = 'SystemButtonFace'
                            num_label.config(text='You Lose\nYou Are Out Of Guesses')
                            guess_button.config(state=DISABLED)

                    elif int(guess_box.get()) > 10 or int(guess_box.get()) < 1:
                        bc = 'SystemButtonFace'
                        num_label.config(text='Invalid Number\nOnly Between 1 and 10')

                else:
                    #Delete entry and throw error message
                    num_label.config(text="That's not a Number")

        elif level.cget('text') == 'Level 3':
            if guess_box.get().isdigit() and guess_num > 0:
                if int(guess_box.get()) >= 1 and int(guess_box.get()) <= 10:
                    #reset our label
                    num_label.config(text="Pick A Number\nBetween 1 and 10")
                    #Find out how far away our pick was from the actual number
                    dif = abs(num - int(guess_box.get()))

                    #check to see if correct
                    if int(guess_box.get()) == num:
                        bc = 'SystemButtonFace'
                        num_label.config(text='You Win')
                        guess_button.pack_forget()
                        guess_box.delete(0, END)
                        guess_box.pack_forget()
                        num_guess.pack_forget()
                        rand_button.pack_forget()
                        global b
                        global quit
                        b = Button(root, text='Play Again', command=replay)
                        quit = Button(root, text='Quit', command=root.destroy)
                        b.pack(pady=20)
                        quit.pack(pady=20)

                    elif dif == 5:
                        #set background color to white
                        bc = 'purple'
                    elif dif < 5:
                        bc = f'#ff{dif}{dif}{dif}{dif}'
                    elif dif < 5:
                        bc = f'#{dif}{dif}{dif}{dif}ff'

                    #change the background of the app
                    root.config(bg=bc)
                    #change background of label
                    num_label.config(bg=bc)
                    num_guess.config(bg=bc)
                    level.config(bg=bc)

                    if num_label.cget('text') != 'You Win' and guess_box.get().isdigit():
                        guess_num = guess_num - 1
                        num_guess.config(text=f'Guess:{guess_num}')

                    if guess_num <= 0 and guess_box.get().isdigit():
                        bc = 'SystemButtonFace'
                        num_label.config(text='You Lose\nYou Are Out Of Guesses')
                        guess_button.config(state=DISABLED)

                elif int(guess_box.get()) > 10 or int(guess_box.get()) < 1:
                    bc = 'SystemButtonFace'
                    num_label.config(text='Invalid Number\nOnly Between 1 and 10')

            else:
                #Delete entry and throw error message
                num_label.config(text="That's not a Number")
        guess_box.delete(0, END)

    def rando_button():
        global guess_num
        guess_num = 3
        num_guess.config(text=f'Guess:{guess_num}')
        if level.cget('text') == 'Level 2':
            guess_num = 2
        if level.cget('text') == 'Level 3':
            guess_num = 1
        num_guess.config(text=f'Guess:{guess_num}')
        global num
        num = randint(1, 10)
        #clear the guess box
        guess_box.delete(0, END)
        #change the colors back to normal
        num_label.config(bg='SystemButtonFace', text='Pick A Number\nBetween 1 and 10')
        root.config(bg='SystemButtonFace')
        num_guess.config(bg='SystemButtonFace')
        level.config(bg='SystemButtonFace')
        guess_button.config(state=NORMAL)

    num_guess = Label(root, text='Guess:3', font=('Elephant', 20))
    num_guess.pack(pady=5)

    guess_box = Entry(root, font=('Elephant',50), width=2)
    guess_box.pack(pady=20)

    guess_button = Button(root, text='Submit', command=guesser_button)
    guess_button.pack(pady=20)

    rand_button = Button(root, text='New Number', command=rando_button)
    rand_button.pack(pady=20)

    #Generate a random number on start
    rando_button()

    root.mainloop()
play_game()