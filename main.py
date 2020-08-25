from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("Simple Calculator")
root.configure(bg="#676361")

e=Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
e.insert(0, "Enter Your Name: ")


def myClick():
    hello = "Hello" + e.get()
    myLabel = label(root, text=hello)
    myLabel.pack()

myButton = Button(root, text="Enter our Stack Quote", command=myClick)

root.mainloop()
