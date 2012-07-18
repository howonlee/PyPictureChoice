from Tkinter import *
from ttk import *
from block import *
from choice import *
from our_break import *

class Block:
    def __init__(self, parent):
        self.myParent = parent
        self.container1 = Frame(parent)
        self.container1.pack()
        self.blockLabel = Label(self.container1)
        self.blockLabel.configure(text="Block #: 0")
        self.blockLabel.pack()
        self.toChoice = Button(self.container1)
        self.toChoice.configure(text="Press to start block")
        self.toChoice.bind("<Button-1>", self.toChoiceCallback)
        self.toChoice.pack()

    def toChoiceCallback(self, event):
        ''' toChoiceCallback
        pressed in block screen, goes to choice screen'''
        self.container1.pack_forget()
        choice = Choice(root)


