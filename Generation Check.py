# -------------------------------------------------------------------------
#   INFO
# -------------------------------------------------------------------------
# Name:         Generation Check
# Purpose:      A simple program that will tell what generation they are based on what year they were born in
# Programmer:   Kektsune
# Date:         01/16/2026
# -------------------------------------------------------------------------

from tkinter import *

window = Tk()
window.title("Generation Check")

userYear = 0

# ----------------------- FUNCTION ---------------------- #

#defining the "generationSubmit" function, and on button click
def generationSubmit():
    global userYear, yearReveal, generationEntry, subGeneration, warningLabel

    #Get the value, or error if incorrect type

    try:
        userYear = int(generationEntry.get())
        warningLabel.config(text="")
    except ValueError:
        warningLabel.config(text="Please enter a valid year.", fg='red')
        yearReveal.config(text="...")
        subGeneration.config(text="...")

    #Let the user know what generation they are

    if(userYear >= 1928 and userYear <= 1945):
        yearReveal.config(text="You are part of the Silent generation!")
    elif(userYear >= 1946 and userYear <= 1964):
        yearReveal.config(text="You are part of the Baby Boomer generation!")
    elif(userYear >= 1965 and userYear <= 1980):
        yearReveal.config(text="You are part of Gen X!")
    elif(userYear >= 1981 and userYear <= 1996):
        yearReveal.config(text="You are part of the Millenials!")
    elif(userYear >= 1997 and userYear <= 2012):
        yearReveal.config(text="You are part of Gen Z!")
    elif(userYear >= 2012 and userYear <= 2025):
        yearReveal.config(text="You are part of Gen Alpha!")
    else:
        warningLabel.config(text="Please enter a valid birth year.", fg='red')

    #Includes subgenerations if necessary
    if 1977 <= userYear <= 1983:
        subGeneration.config(text="You are also part of the Xennials!")
    elif 1993 <= userYear <= 1998:
        subGeneration.config(text="You are also part of the Zillenials!")

    #Clears entry/text box
    generationEntry.delete(0, END)
    userYear=0

# ----------------------- WIDGET SETUP ---------------------- #

title = Label(window, text="Welcome to Generation Check!")
title.pack()

directions = Label(window, text="Type your birth year in the text box below!")
directions.pack()

generationEntry = Entry(window)
generationEntry.pack()

submitButton = Button(window, text="Submit", command=generationSubmit)
submitButton.pack()

Label(window, text="").pack()

results = Label(window, text="The year you've gotten is: ")
results.pack()

yearReveal = Label(window, text="...")
yearReveal.pack()

subGeneration = Label(window, text="...")
subGeneration.pack()

warningLabel = Label(window, text="")
warningLabel.pack()

tagLabel = Label(window, text="By: Kektsune")
tagLabel.pack()

window.mainloop()