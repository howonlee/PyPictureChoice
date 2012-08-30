from Tkinter import *
from ttk import *
import choice
import misc

class Block:
    def __init__(self, parent, blockData, pics):
        self.myParent = parent
        self.myBlockData = blockData
        self.myPics = pics
        self.myBlockData['block_num'] = self.myBlockData['block_num'] + 1
        self.blockLabelText = ("Block #: " + str(self.myBlockData['block_num']) + " of 6")
        self.container1 = Frame(parent, style="Card.TFrame")
        self.container1.rowconfigure(0, minsize = misc.getHeight(parent) * 0.8)
        self.container1.rowconfigure(1, minsize = misc.getHeight(parent) * 0.2)
        self.container1.grid()
        self.blockLabel = Label(self.container1, text=self.blockLabelText, style="Card.TLabel")
        self.blockLabel.grid(column=0, row=0)
        self.toChoice = Button(self.container1, text="Press to start block", width=misc.getButtonWidth(parent))
        self.toChoice.bind("<Button-1>", self.toChoiceCallback)
        self.toChoice.grid(column=0, row=1, sticky=(N, E, W, S))

    def toChoiceCallback(self, event):
        ''' toChoiceCallback
        pressed in block screen, goes to choice screen'''
        self.container1.grid_forget()
        self.myBlockData['time_begin'] = misc.getCurrTime()
        choiceinstance = choice.Choice(self.myParent, self.myBlockData, self.myPics, 0)
