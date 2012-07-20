from Tkinter import *
from ttk import *
import our_break

class Choice:
    def __init__(self, parent, blockData):
        self.myParent = parent
        self.myBlockData = blockData
        self.numTrials = 10 #set this
        self.container1 = Frame(parent, width=1000, height=1000)
        self.container1.grid(column=0, row=0)
        self.choice1 = Button(self.container1)
        self.choice2 = Button(self.container1)
        self.toBreak = Button(self.container1)
        self.choice1.configure(text="Choice 1")
        self.choice2.configure(text="Choice 2")
        self.toBreak.configure(text="Take a Break")
        self.choice1.bind("<Button-1>", self.choice1Callback)
        self.choice2.bind("<Button-1>", self.choice2Callback)
        self.toBreak.bind("<Button-1>", self.toBreakCallback)
        self.choice1.grid(column=0, row=1)
        self.choice2.grid(column=1, row=1)

    def choice1Callback(self, event):
        self.choice1.grid_forget()
        self.choice2.grid_forget()
        self.toBreak.grid(column=0, row=1)

    def choice2Callback(self, event):
        self.choice1.grid_forget()
        self.choice2.grid_forget()
        self.toBreak.grid(column=0, row=1)

    def toBreakCallback(self, event):
        self.container1.grid_forget()
        our_breakinstance = our_break.Break(self.myParent, self.myBlockData)
