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
        self.blockLabelText = "Block #: " + str(self.myBlockData['block_num'])
        self.container1 = Frame(parent)
        self.screenheight = self.myParent.winfo_screenheight()
        self.container1.rowconfigure(0, minsize = self.screenheight * 0.8)
        self.container1.rowconfigure(1, minsize = self.screenheight * 0.2)
        self.container1.grid()
        self.blockLabel = Label(self.container1)

        self.blockLabel.configure(text=self.blockLabelText)
        self.blockLabel.grid(column=0, row=0, sticky=(N, W))
        self.buttonwidth = self.myParent.winfo_screenwidth() / 8
        self.toChoice = Button(self.container1)
        self.toChoice.configure(text="Press to start block", width=self.buttonwidth)
        self.toChoice.bind("<Button-1>", self.toChoiceCallback)
        self.toChoice.grid(column=0, row=1, sticky=(N, E, W, S))

    def toChoiceCallback(self, event):
        ''' toChoiceCallback
        pressed in block screen, goes to choice screen'''
        self.container1.grid_forget()
        self.myBlockData['time_begin'] = misc.getCurrTime()
        choiceinstance = choice.Choice(self.myParent, self.myBlockData, self.myPics, 0)
