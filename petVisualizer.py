from tkinter import *
from tkinter import messagebox
from random import choice, randint
import random
from tkinter import ttk


#set credits and health as a random number
credits = random.randint(1, 50)
health = random.randint(1, 90)


#Main Window - set title, size and set to not resizeable
window = Tk()
window.title("Virtual Jerry Game")
window.geometry('600x400')
window.resizable(0, 0) 

#display credits to top right corner
label = Label(window, text="Credits = " + str(credits))
label.grid(row=0, column=1, sticky='ne',columnspan=1)   

#display health to top left
healthlabel = Label(window, text="Health = " + str(health))
healthlabel.grid(row=0, column=1, sticky='nw',columnspan=1)  

# i need a real image of hostel cat
#set cat image as bottom center
# declare happy and sad cat images.
sadCat = PhotoImage(file='sadCat.png')
pet = Label(window, image=sadCat)
pet.grid(row=2, column=0, columnspan=3, pady=10)  # Added columnspan to span all columns
happyCat = PhotoImage(file='test.png')

#if health is less than 50, display sad cat else happy cat
def updateImage():
    global health
    if health < 50:
        pet.config(image=sadCat)
    else:
        pet.config(image=happyCat)

updateImage()

#need to fix progressbar
progressbar = ttk.Progressbar()
progressbar.place(x=30, y=20, width=200)
progressbar.step(health) # this progress bar is abit suspiciouss

#open a pop up window to choose game type
def openMoreCred():
    earn= Toplevel(window)
    earn.geometry("400x200")
    earn.title("Choose Game Type")
    earn.resizable(0, 0) 
    question = Label(earn, text="Which game type would you like to play?")
    question.grid(row=0, column=1)
    math_button = Button(earn, text="Math Quiz", command = "mathquiz")
    math_button.place(x=30, y=60)
    typing_btn = Button(earn, text="Typing Game", command = "typinggame")
    typing_btn.place(x=200, y=60)

# display add button beside the credits, call the openMoreCred function when the button is clicked
add = PhotoImage(file = 'add.png')
add_button = Button(window, image= add , command = openMoreCred, bd = 0)
add_button.grid(row=0, column=2, sticky='nw',columnspan=2) 

#new pop up window when user clicks "feed jerry" button, display 2 buttons: water & food
def open_popup():
   global warning
   top= Toplevel(window)
   top.geometry("400x200")
   top.title("Earn Credits")
   top.resizable(0, 0) 
   warning = Label(top, text= "" ) # text is empty first
   warning.grid(row=1, column=1)
   question = Label(top, text="What would you like to feed the cat?")
   question.grid(row=0, column=1)
   water_button = Button(top, text="Water", command = feedwater)
   water_button.place(x=10, y=60)
   food_button = Button(top, text="Food", command = feedfish)
   food_button.place(x=90, y=60)



#Choice of food : Fish (4 credits to buy) , Water (2 credits to buy)
#If enough credits, immediately deduct,else prompt to choose option 2 to earn more credits
# Once pet is fed, health increases based on the choice of food [fish - increase by 10 , water - increase by 2 ]

def feedwater():
    global credits
    global health
    global warning
    watercred = 2
    if credits >= watercred:
        credits = credits - watercred
        print("watertest health", health)
        
        health = health + 1
        health = max(0, min(health, 100))
        label.config(text="Credits = " + str(credits))
        healthlabel.config(text = "Health = " + str(health))
        updateImage()
        #progressbar.step(health)
        print("watertest health", health)
    else:
        warning.config(text="Insufficient credits: " + str(credits) + " Please quit this window, \n and click the add button to earn more credits")

def feedfish():
    global credits
    global health
    global warning
    fishcred = 4
    if credits >= fishcred and health < 100:
        credits = credits - fishcred
        print("fishtest health", health)
        health = health + 10
        health = max(0, min(health, 100))
        label.config(text="Credits = " + str(credits))
        healthlabel.config(text = "Health = " + str(health))
        updateImage()
        #progressbar.step(health)
        print("fisttest health", health)
    else:
        if health >= 100: 
            # or show fat image
            #warning.config(text="Health is Full, Credits Available:  " + str(credits) + " Please quit this window, \n and dont make the cat overeat!")
            messagebox.showinfo("Health is Full", "Credits Available:  " + str(credits) + " Please quit this window, \n and dont make the cat overeat!")

        else: 
            warning.config(text="Insufficient credits: " + str(credits) + " Please quit this window, \n and click the add button to earn more credits")


button = Button(window, text= "Feed Jerry", command=open_popup)
button.grid(column=1, row=1, pady=10)  # Added pady to add space between button and other elements



def mathquiz():
    # about 80 lines
    pass

def typingGame():
    #about 80 lines
    pass

#other word games - cognitive thinking
def hangman():
    pass

## have more games till hits 400 lines code specified in docs lol

window.mainloop()

