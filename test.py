from tkinter import *

root = Tk()

root.geometry("800x300")


def callback(*args):
    print("Activated.")

print("banane") if option_text.get()=="banana"


myList = ["apple", "banana", "carrot"]

option_text = StringVar()
option_text.set("Select option")

options = OptionMenu(root, option_text, *myList, command=callback)

options.pack()


root.mainloop()
