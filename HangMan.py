from tkinter import *
from string import ascii_uppercase
from tkinter import messagebox
import random

window = Tk()
window.title('Hangman Game')

word_list = ["MARS", "JUPITER", "URANUS", "NEPTUNE", "MERCURY", "SATURN", "VENUS", "EARTH", "PLUTO"]

images = [PhotoImage(file="/Users/HTunctepe/PycharmProjects/Kivy_Projects/21.Hafta-Odevler/image1.png"),
          PhotoImage(file="/Users/HTunctepe/PycharmProjects/Kivy_Projects/21.Hafta-Odevler/image2.png"),
          PhotoImage(file="/Users/HTunctepe/PycharmProjects/Kivy_Projects/21.Hafta-Odevler/image3.png"),
          PhotoImage(file="/Users/HTunctepe/PycharmProjects/Kivy_Projects/21.Hafta-Odevler/image4.png"),
          PhotoImage(file="/Users/HTunctepe/PycharmProjects/Kivy_Projects/21.Hafta-Odevler/image5.png"),
          PhotoImage(file="/Users/HTunctepe/PycharmProjects/Kivy_Projects/21.Hafta-Odevler/image6.png"),
          PhotoImage(file="/Users/HTunctepe/PycharmProjects/Kivy_Projects/21.Hafta-Odevler/image7.png"),
          PhotoImage(file="/Users/HTunctepe/PycharmProjects/Kivy_Projects/21.Hafta-Odevler/image8.png"),
          PhotoImage(file="/Users/HTunctepe/PycharmProjects/Kivy_Projects/21.Hafta-Odevler/image9.png"),
          PhotoImage(file="/Users/HTunctepe/PycharmProjects/Kivy_Projects/21.Hafta-Odevler/image10.png")]


def newGame():
    global spaacedWord
    global noOfGuesses
    noOfGuesses = 0
    imgLabel.config(image=images[0])
    chosen_word = random.choice(word_list)
    spaacedWord = " ".join(chosen_word)
    hiddenWord.set(" ".join(("_" * len(chosen_word))))

def Hint():
    global noOfGuesses
    messagebox.showwarning("Hint Message", "A planet of the Solar System!")
    noOfGuesses += 1
    imgLabel.config(image=images[noOfGuesses])


def guess(letter):
    global noOfGuesses
    if noOfGuesses < 9:
        txt = list(spaacedWord)
        guessed = list(hiddenWord.get())
        if spaacedWord.count(letter) > 0:
            for i in range(len(txt)):
                if txt[i] == letter:
                    guessed[i] = letter
                hiddenWord.set("".join(guessed))
                if hiddenWord.get() == spaacedWord:
                    messagebox.showinfo("Hangman", "Congratulations! You guessed the word!!!")
                    newGame()
                    noOfGuesses += 1
        else:
            noOfGuesses += 1
            imgLabel.config(image=images[noOfGuesses])
            if noOfGuesses == 9:
                messagebox.showwarning("Hangman", "Oops! You just hanged the man.\n" + "Game Over :(".center(40))


imgLabel = Label(window)
imgLabel.grid(row=0, column=0, columnspan=6, padx=10, pady=100)
imgLabel.config(image=images[0])

hiddenWord = StringVar()
Label(window, textvariable=hiddenWord, font="Garamond 18 bold").grid(row=0, column=6, columnspan=6, padx=10)

n = 0
Button(window, text="Hint", command=lambda: Hint(), font="Garamond 20 bold").grid(row=1, column=0, columnspan=2,
                                                                                          sticky="NSWE")
for i in ascii_uppercase:
    Button(window, text=i, command=lambda c=i: guess(c), font="Garamond 18",
           width=6).grid(row=2 + n // 9, column=n % 9)
    n += 1

Button(window, text="New\nGame", command=lambda: newGame(), font="Garamond 12 bold").grid(row=4, column=8,
                                                                                          sticky="NSWE")
newGame()
window.mainloop()
