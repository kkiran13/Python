import Tkinter
import tkMessageBox

top = Tkinter.Tk()
# Code to add widgets will go here...
def hello():
    tkMessageBox.showinfo("Say Hello", "Hello World")

    B1 = Tkinter.Button(top, text = "Say Hello", command = hello)
    B1.pack()
    
top.mainloop()