from tkinter import *

window=Tk()
window.geometry("500x500")
window.title("Simple Calculator")
window.configure(bg="#676361")
button=Button(window,text="OK",width=3,height=2,bg="black",fg="white")
label=Label(window,text="submit")


button.pack()
label.pack()

window.mainloop()
