#Write a program in Python that displays a window to the user that asks them to enter an integer N and displays its factorial
from tkinter import *

def calculate_factorial():
    try:
        n = int(entry.get())
        if n < 0:
            print("Error", "Factorial is not defined for negative numbers.")
        elif n == 0:
            factorial = 1
        else:
            factorial = 1
            for i in range(1, n + 1):
                factorial *= i
        result_label.config(text=f"Factorial of {n} is: {factorial}")
    except ValueError:
        print("Error", "Please enter a valid integer.")

root = Tk()
root.geometry("250x300+300+300")
root.title("Factorial Calculator")

label =Label(root, text="Enter an integer N:")
label.pack()

entry = Entry(root)
entry.pack()

button = Button(root, text="Calculate Factorial", command=calculate_factorial)
button.pack()

result_label = Label(root, text="")
result_label.pack()

root.mainloop()