from tkinter import *
from random import choice, randint
import random
from tkinter import ttk

credits = random.randint(1, 20)
health = random.randint(1, 90)

color_red = "\033[91m"
color_default = "\033[0m"

window = Tk()
window.title("Pet Game")
window.geometry('600x400')
window.resizable(0, 0) # no resizeable

label = Label(window, text="Credits = " + str(credits))
label.grid(row=0, column=1, sticky='ne',columnspan=1)   # Change column to 2, sticky to 'ne'

healthlabel = Label(window, text="Health = " + str(health))
healthlabel.grid(row=0, column=1, sticky='nw',columnspan=1)   # Change column to 2, sticky to 'ne'

photo = PhotoImage(file='pet.png')
pet = Label(window, image=photo)
pet.grid(row=2, column=0, columnspan=3, pady=10)  # Added columnspan to span all columns


#progressbar = ttk.Progressbar()
#progressbar.place(x=30, y=20, width=200)
#progressbar.step(health) # this progress bar is abit suspiciouss


def openMoreCred():
    earn= Toplevel(window)
    earn.geometry("400x200")
    earn.title("Child Window")
    earn.resizable(0, 0) 
    question = Label(earn, text="Which game type would you like to play?")
    question.grid(row=0, column=1)
    math_button = Button(earn, text="Math Quiz", command = "mathquiz")
    math_button.place(x=30, y=60)
    typing_btn = Button(earn, text="Typing Game", command = "typinggame")
    typing_btn.place(x=200, y=60)

add = PhotoImage(file = 'add.png')
add_button = Button(window, image= add , command = openMoreCred)
add_button.grid(row=0, column=2, sticky='nw',columnspan=2) 

def open_popup():
   global warning
   top= Toplevel(window)
   top.geometry("400x200")
   top.title("Child Window")
   top.resizable(0, 0) 
   warning = Label(top, text="" ) # text is empty first
   warning.grid(row=1, column=1)
   question = Label(top, text="What would you like to feed the cat?")
   question.grid(row=0, column=1)
   water_button = Button(top, text="Water", command = feedwater)
   water_button.place(x=10, y=60)
   food_button = Button(top, text="Food", command = feedfish)
   food_button.place(x=90, y=60)



def feedwater():
    global credits
    global health
    global warning
    watercred = 2
    if credits >= watercred:
        credits = credits - watercred
        print("watertest health", health)
        health = health + 1
        label.config(text="Credits = " + str(credits))
        healthlabel.config(text = "Health = " + str(health))
        #progressbar.step(health)
        print("watertest health", health)
    else:
        warning.config(text="Insufficient credits: " + str(credits) + " Please quit this window, \n and click the add button to earn more credits")

def feedfish():
    global credits
    global health
    global warning
    fishcred = 4
    if credits >= fishcred:
        credits = credits - fishcred
        print("fishtest health", health)
        health = health + 1
        label.config(text="Credits = " + str(credits))
        healthlabel.config(text = "Health = " + str(health))
        #progressbar.step(health)
        print("fisttest health", health)
    else:
        warning.config(text="Insufficient credits: " + str(credits) + " Please quit this window, \n and click the add button to earn more credits")



button = Button(window, text="Feed the Cat", command=open_popup)
button.grid(column=1, row=1, pady=10)  # Added pady to add space between button and other elements



def mathquiz():
    pass

def triviaquiz():
    pass

window.mainloop()

