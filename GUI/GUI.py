from tkinter import *
import tkinter.messagebox as showMsg

root = Tk()
root.title("My first GUI!")


def onPress(event):
    showMsg.showinfo("Warning", "Hello there"+textField.get(), )


label = Label(root, text="Enter your name")
label.grid(row=0, column=2)
textField = Entry()
textField.grid(row=1, column=2)
button1 = Button(root, text="Greetings", fg="Red")
button1.grid(row=2, column=2)
textField.bind("<Return>", onPress)

root.mainloop()
