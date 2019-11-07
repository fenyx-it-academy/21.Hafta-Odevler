from tkinter import *
from string import ascii_uppercase
from tkinter import messagebox
import random
window=Tk()
window.title('Hangman')



word_list=["AMSTERDAM","ROTTERDAM","ASSEN","GRONINGEN","ISTANBUL","MILAN"]

photos=[PhotoImage(file="C:/Users/Gebruiker/Desktop/Python/Kivy_project2/Week21/hangman/hang0.png"),PhotoImage(file="C:/Users/Gebruiker/Desktop/Python/Kivy_project2/Week21/hangman/hang1.png"),
        PhotoImage(file="C:/Users/Gebruiker/Desktop/Python/Kivy_project2/Week21/hangman/hang2.png"),PhotoImage(file="C:/Users/Gebruiker/Desktop/Python/Kivy_project2/Week21/hangman/hang3.png"),
        PhotoImage(file="C:/Users/Gebruiker/Desktop/Python/Kivy_project2/Week21/hangman/hang4.png"),PhotoImage(file="C:/Users/Gebruiker/Desktop/Python/Kivy_project2/Week21/hangman/hang5.png"),
        PhotoImage(file="C:/Users/Gebruiker/Desktop/Python/Kivy_project2/Week21/hangman/hang6.png"),PhotoImage(file="C:/Users/Gebruiker/Desktop/Python/Kivy_project2/Week21/hangman/hang7.png"),
        PhotoImage(file="C:/Users/Gebruiker/Desktop/Python/Kivy_project2/Week21/hangman/hang8.png"),PhotoImage(file="C:/Users/Gebruiker/Desktop/Python/Kivy_project2/Week21/hangman/hang9.png"),
        PhotoImage(file="C:/Users/Gebruiker/Desktop/Python/Kivy_project2/Week21/hangman/hang10.png"),PhotoImage(file="C:/Users/Gebruiker/Desktop/Python/Kivy_project2/Week21/hangman/hang11.png")]


def newGame():
    global the_word_withSpaces
    global numberOfGuesses
    numberOfGuesses=0
    imgLabel.config(image=photos[0])
    the_word= random.choice(word_list)
    the_word_withSpaces=" ".join(the_word)
    lblWord.set(" ".join(("_"*len(the_word))))

def guess(letter):
    global numberOfGuesses
    if numberOfGuesses<11:
        txt = list(the_word_withSpaces)
        guessed=list(lblWord.get())
        if the_word_withSpaces.count(letter)>0:
            for c in range(len(txt)):
                if txt[c] == letter:
                    guessed[c]=letter
                lblWord.set("".join(guessed))
                if lblWord.get()== the_word_withSpaces:
                    messagebox.showinfo("Hangman","You won!!!")
                    newGame()
                    numberOfGuesses += 1
        else:
            numberOfGuesses+=1
            imgLabel.config(image=photos[numberOfGuesses])
            if numberOfGuesses == 11:
                messagebox.showwarning("Hangman", "Game Over :(")

imgLabel= Label(window)
imgLabel.grid(row=0, column=0,columnspan=3, padx=10, pady=40)
imgLabel.config(image=photos[0])

lblWord=StringVar()
Label(window, textvariable=lblWord, font=("Consolas 18 bold")).grid(row=0, column=3,columnspan=6,padx=10)

n=0
for c in ascii_uppercase:
    Button (window, text=c, command=lambda c=c: guess(c), font =("Helvetica 18"), width=5).grid(row= 1+n//9 ,column = n % 9)
    n+=1

Button(window,text= "New\nGame", command=lambda :newGame(),font=("Helvetica 12 bold")).grid(row=3, column=8, sticky="NSWE")
newGame()
window.mainloop()