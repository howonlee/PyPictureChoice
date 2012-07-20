from Tkinter import *
from ttk import *
import choice

class Block:
    def __init__(self, parent, blockData):
        self.myParent = parent
        self.myBlockData = blockData
        self.container1 = Frame(parent, width=1000, height=1000)
        self.container1.grid(column=0, row=0)
        self.blockLabel = Label(self.container1)
        self.blockLabel.configure(text="Block #: 0")
        self.blockLabel.grid(column=0, row=0)
        self.toChoice = Button(self.container1)
        self.toChoice.configure(text="Press to start block")
        self.toChoice.bind("<Button-1>", self.toChoiceCallback)
        self.toChoice.grid(column=0, row=1)

    def toChoiceCallback(self, event):
        ''' toChoiceCallback
        pressed in block screen, goes to choice screen'''
        self.container1.grid_forget()
        choiceinstance = choice.Choice(self.myParent, self.myBlockData)
