


############# IMPORT LIBRARIES  ##########
import turtle
import tkinter as tk
from tkinter.ttk import *
from tkinter import messagebox 
from string import ascii_uppercase
import random
import csv


############ FUNCTIONS DEFINITION ########

def howToPlay():
    instructions = ("""
---How to play---
  * With the given category, word length and visible letters, guess the word!
  * You hve 5 lives !
  1) On every turn, enter your guess!
    - If the letter is found in the word, the letter will fill the dashes.
    - If the letter is not found in the word, you have one less chance and the stroke will increase
  2) The guessing continues until the word is solved or when the game is over.
  3) The game ends when the hangman is fully drawn.
\n""")


    howToPlayWindow = tk.Toplevel(window)
    howToPlayWindow.title("How to play Hangman")
    howToPlayWindow.geometry("800x300")
    Label(howToPlayWindow, text= instructions, font = ("Comic Sans MS", 11)).pack()
    return


## Read csv file that has 3 columns - word, hint, fun fact   
def generateSecretWord():
    with open('words.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
        print(data) 
   # for i in range (0, len(data)):
    #    newdata= data[i]
     #   print(data[i])
      #  data[i] = newdata
    print(data[1])
    rand_index = random.randint(1, len(data)-1)
    secretWord = data[rand_index][0]
    secretHint = data[rand_index][1]
    secretFact = data[rand_index][2]
    secretWord.strip(" ")
    return secretWord,secretHint,secretFact


## Set up for new games 
def newGame():
    global secret_word_withSpaces
    global wrong_guess
    global attempted_guesses
    global secret_word
    global secret_fact
    attempted_guesses =[]
    ## Reset
    screen.bgcolor(35,155,86)
    draw.reset()
    wrong_guess = 0
    
    secret_word, secret_hint, secret_fact = generateSecretWord()
    secret_word_withSpaces = " ".join(secret_word)
    lblWord.set(" ".join("_"*len(secret_word)))
    lblHint.set("Hint: " + "".join(secret_hint))
    lblLives.set("You have 5 lives left!")
    
    ## Set up initial stage  0 hangman
    draw.penup()
    draw.goto(-100,150)
    draw.speed(10)
    draw.pendown()
    draw.forward(200)
    draw.penup()
    draw.goto(-100,150)
    draw.right(90)
    draw.pendown()
    draw.forward(300)
    

def drawHangman(wrong_guess):
    
    if wrong_guess == 1: ##draw string 
        screen.bgcolor(130,224,170)   ## light green
        draw.penup()
        draw.goto(0,150)
        draw.pendown()
        draw.forward(50)
        #livesleft = 5-wrong_guess
        #lblLives.set( "You have {} lives left!".format(livesleft))
        
    elif wrong_guess == 2:  ##draw head 
        screen.bgcolor(241,196,15)  ##yellow
        draw.speed(10) 
        draw.penup()
        draw.goto(-50,50)
        draw.pendown()
        draw.circle(50)
        #livesleft = 5-wrong_guess
        #lblLives.set( "You have {} lives left!".format(livesleft))
        
    elif wrong_guess == 3: ## draw body + hands
        screen.bgcolor(243,156,18)  ## light orange
        draw.speed(8) 
        draw.penup()
        draw.goto(0,0)
        draw.pendown()
        draw.forward(100)
        livesleft = 5-wrong_guess
        lblLives.set( "You have {} lives left!".format(livesleft))

    elif wrong_guess == 4: ## draw hands 
        ## change bg color to dark oragne
        screen.bgcolor(211,84,0)   
        draw.penup()
        draw.goto(0,-20)
        draw.left(45)
        draw.pendown()
        draw.forward(50)
        draw.penup()
        draw.goto(0,-20)
        draw.right(90)
        draw.pendown()
        draw.forward(50)
        livesleft = 5-wrong_guess
        lblLives.set( "You have {} lives left!".format(livesleft))

    elif wrong_guess == 5:
        ## change bg color to red
        screen.bgcolor(255,0,0) 
        ## draw legs
        draw.penup()
        draw.goto(0,-100)
        draw.pendown()
        draw.forward(50)
        draw.penup()
        draw.goto(0,-100)
        draw.left(90)
        draw.pendown()
        draw.forward(50)

        ## draw left
        draw.penup()
        draw.goto(-25,70)
        draw.pendown()
        draw.forward(20)
        draw.penup()
        draw.goto(-15,70)
        draw.right(90)
        draw.pendown()
        draw.forward(20)
        
        ## right eye 
        draw.penup()
        draw.goto(25,70)
        draw.pendown()
        draw.forward(20)
        draw.penup()
        draw.goto(15,70)
        draw.left(90)
        draw.pendown()
        draw.forward(20)
    

        ## draw mouth
        draw.penup()
        draw.goto(-5,30)
        draw.right(45)
        draw.pendown()
        draw.circle(5)
        turtle.RawTurtle.hideturtle(draw)

        livesleft = 5-wrong_guess
        lblLives.set( "You have {} lives left!".format(livesleft))
        messagebox.showinfo("Correct answer is {}".format(secret_word),secret_fact)
        secondgame = messagebox.askretrycancel("Result","You Lost! Try again?")
        if secondgame == True:
            newGame()
        
    livesleft = 5-wrong_guess
    lblLives.set( "You have {} lives left!".format(livesleft))

            
    

def guessLetter (letter):
    global wrong_guess
    global attempted_guesses


    if wrong_guess <5:
        if letter in attempted_guesses:
            messagebox.showerror("Error", "You guessed this letter before, try again!")
        else: 
            text = list(secret_word_withSpaces)
            guessed = list(lblWord.get())
            identicalLetter = secret_word_withSpaces.count(letter)
            if  identicalLetter >0:
                for i in range (0,len(text)):
                    if text[i]==letter:
                        guessed[i] =letter
                        attempted_guesses.append(letter)
                    lblWord.set("".join(guessed))
                    if guessed == text:
                        messagebox.showinfo("Fun fact",secret_fact)
                        secondgame=messagebox.askretrycancel("Result", "You won! Try again?")
                        if secondgame == True:
                            newGame()
                        else:
                            break
            else:
                wrong_guess+=1
                drawHangman (wrong_guess)
                attempted_guesses.append(letter)
    else:
         drawHangman (wrong_guess)      



############## SET UP WINDOW AND CANVAS ############
window = tk.Tk()   ## creating window
window.title('Hangman-ANIMALS') ## windows name 
canvas = tk.Canvas(window)  ## create tkinter canvas
canvas.config(width=400, height = 400) 
canvas.grid(row = 1, column = 11, rowspan = 2, columnspan =2) ## placing canvas at top right
screen = turtle.TurtleScreen(canvas)   ## defines the window for turtle
draw = turtle.RawTurtle(canvas, shape = "turtle")
screen.colormode(255)
screen.bgcolor(35,155,86)


####### KEYBOARD WIDGET + NEW GAME BUTTON  #######
n = 0 
for a in ascii_uppercase: ## create keyboard at the bottom 
    button=tk.Button(window, text = a, command = lambda a=a: guessLetter(a), width = 10, height = 4).grid(row = 5+(n//9), column = 1+n%9)
    n+=1

button_newgame = tk.Button(window,text = "New Game", command = newGame, width = 10, height = 4).grid(row = 7, column = 9)
button_howtoplay = tk.Button(window,text = "How to Play", command = howToPlay, width = 10, height = 4).grid(row = 7, column = 10)


######## DASHES WIDGET #########
lblWord = tk.StringVar()
tk.Label(window, textvariable = lblWord, font = ("Comic Sans MS", 24, "bold")).grid(row = 2, column = 2, columnspan= 7) ## display dashes 
lblHint = tk.StringVar()
tk.Label(window, textvariable = lblHint, font = ("Comic Sans MS", 18)).grid(row = 1, column = 2, columnspan= 7)  ## display hints 
lblLives = tk.StringVar()
tk.Label(window, textvariable = lblLives, font = ("Comic Sans MS", 18)).grid(row = 5, column = 10, columnspan= 3)  ## display hints
tk.Label(window, text = "Welcome! Let's play hangman!", font = ("Comic Sans MS", 18)).grid(row = 0, column = 0, columnspan= 6) ## welcome message

############# GAME STARTS ###############
newGame()
window.mainloop()
    

