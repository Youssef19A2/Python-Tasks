#Create a graphical application in Python Tkinter that asks the user to enter two integers and displays their sum

from tkinter import *
T=Tk()
T.geometry("350x150+350+350")
T.title("calculator")
T.resizable(True,True)


operation = StringVar(value="none")
result_label = Label(T, text="Result:")
result_label.grid(row=6,column=1)

L_1=Label(text="Enter First Number: ",fg="black")
L_1.grid(row=0,column=0)
L_2=Label(text="Enter Second Number: ",fg="black")
L_2.grid(row=1,column=0)
E_1=Entry(T)
E_1.grid(row=0,column=1)
E_2=Entry(T)
E_2.grid(row=1,column=1)
v1=IntVar()
R_1=Radiobutton(T,text="sum",variable=operation,value="sum")
R_1.grid(row=6,column=0)
R_2=Radiobutton(T,text="sub",variable=operation,value="sub")
R_2.grid(row=7,column=0)


def calculate():
    num1 = E_1.get()
    num2= E_2.get()
    if num1.isdigit() and num2.isdigit():
        num1 = int(num1)
        num2 = int(num2)
        if operation.get() == "sum":
            result = num1 + num2
        elif operation.get() == "sub":
            result = num1 - num2
        else:
            result = "Select an operation"
    
        result_label.config(text=f"Result: {result}")
    else:
        result_label.config(text="Please enter valid integers.")

B=Button(T,text="get result",fg="black",command=calculate)
B.grid(row=7,column=1)
T.mainloop()
