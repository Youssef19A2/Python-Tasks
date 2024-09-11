#Write a program that asks the user to type a word and return him its reverse
from tkinter import *

def reverse_name():
    word = entry.get()
    reversed_word = word[::-1]
    label.config(text=reversed_word)

root = Tk()
root.title("Reverse Word")
root.geometry("230x200+300+300")

label = Label(root, text="Enter a word:")
label.pack()

entry = Entry(root)
entry.pack()

button = Button(root, text="Validate", command=reverse_name)
button.pack()

root.mainloop()
