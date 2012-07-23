from Tkinter import *
from ttk import *
import choice
import time

class Block:
    def __init__(self, parent, blockData):
        self.myParent = parent
        self.myBlockData = blockData
        self.blockLabelText = "Block #: " + str(self.myBlockData['blockNum'])
        self.myBlockData['blockNum'] = self.myBlockData['blockNum'] + 1
        self.container1 = Frame(parent)
        self.container1.rowconfigure(0, weight=1)
        self.container1.columnconfigure(0, weight=1)
        self.container1.grid()
        self.blockLabel = Label(self.container1)

        self.blockLabel.configure(text=self.blockLabelText)
        self.blockLabel.grid(column=0, row=0, sticky=(N, E, W))
        self.toChoice = Button(self.container1)
        self.toChoice.configure(text="Press to start block")
        self.toChoice.bind("<Button-1>", self.toChoiceCallback)
        self.toChoice.grid(column=0, row=1, sticky=(E, W, S))

    def toChoiceCallback(self, event):
        ''' toChoiceCallback
        pressed in block screen, goes to choice screen'''
        self.container1.grid_forget()
        self.myBlockData['beginTime'] = int(time.time() * 1000)
        choiceinstance = choice.Choice(self.myParent, self.myBlockData, 0)
