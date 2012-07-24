from Tkinter import *
from ttk import *
import block
import time

class Break:
    def __init__(self, parent, blockData, pics):
        self.myParent = parent
        self.myBlockData = blockData
        self.myPics = pics
        self.myBlockData['breakBeginTime'] = int(time.time() * 1000)
        self.totalNumBlocks = 2
        self.container1 = Frame(parent)
        self.container1.grid()
        self.breakLabel = Label(self.container1)
        self.breakLabel.grid(column=0, row=0)
        if (self.myBlockData['blockNum'] < self.totalNumBlocks):
            self.breakLabel.configure(text="Take a break")
            self.toBlock = Button(self.container1)
            self.toBlock.configure(text="Press to go to the next block")
            self.toBlock.bind("<Button-1>", self.toBlockCallback)
            self.toBlock.grid(column=0, row=1)
        else:
            self.breakLabel.configure(text="OK, you're done.")
            self.exitButton = Button(self.container1)
            self.exitButton.configure(text="Press to exit the experiment")
            self.exitButton.bind("<Button-1>", self.exitCallback)
            self.exitButton.grid(column=0, row=1)

    def toBlockCallback(self, event):
        self.container1.grid_forget() 
        blockinstance = block.Block(self.myParent, self.myBlockData, self.myPics)

    def exitCallback(self, event):
        self.myBlockData['breakEndTime'] = int(time.time() * 1000)
        print str(self.myBlockData)
        self.myParent.quit()
