#Make this template and each button display different name 
from tkinter import *
root = Tk()
root.geometry("240x100+300+300")
root.title("Task1")
B1=Button(text="Button1")
B1.grid(row=0,column=1)
B2=Button(text="Button2")
B2.grid(row=1,column=0)
B3=Button(text="Button3")
B3.grid(row=1,column=2)
B4=Button(text="Button4")
B4.grid(row=2,column=1)
root.mainloop()
