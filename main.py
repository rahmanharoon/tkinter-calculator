from tkinter import *

window=Tk()

button=Button(window,text="OK",width=5,height=5,bg="black",fg="white")
label=Label(window,text="Welcome")


button.pack()
label.pack()
window.mainloop()
