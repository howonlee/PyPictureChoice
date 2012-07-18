from Tkinter import *
from ttk import *
from . import *

class Choice:
    def __init__(self, parent):
        self.myParent = parent
        self.container1 = Frame(parent)
        self.container1.pack()
        self.choice1 = Button(self.container1)
        self.choice2 = Button(self.container1)
        self.toBreak = Button(self.container1)
        self.choice1.configure(text="Choice 1")
        self.choice2.configure(text="Choice 2")
        self.toBreak.configure(text="Take a Break")
        self.choice1.bind("<Button-1>", self.choice1Callback)
        self.choice2.bind("<Button-1>", self.choice2Callback)
        self.toBreak.bind("<Button-1>", self.toBreakCallback)
        self.choice1.pack()
        self.choice2.pack()

    def choice1Callback(self, event):
        self.choice1.pack_forget()
        self.choice2.pack_forget()
        self.toBreak.pack()

    def choice2Callback(self, event):
        self.choice1.pack_forget()
        self.choice2.pack_forget()
        self.toBreak.pack()

    def toBreakCallback(self, event):
        self.container1.pack_forget()
        our_break = Break(root)


