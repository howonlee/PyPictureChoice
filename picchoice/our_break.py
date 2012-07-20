from Tkinter import *
from ttk import *
import block

class Break:
    def __init__(self, parent, blockData):
        self.myParent = parent
        self.myBlockData = blockData
        self.totalNumBlocks = 2
        self.container1 = Frame(parent, width=1000, height=1000)
        self.container1.grid(column=0, row=0)
        self.breakLabel = Label(self.container1)
        self.breakLabel.grid(column=0, row=0)
        if (self.myBlockData['blockNum'] <= self.totalNumBlocks):
            self.breakLabel.configure(text="Take a break")
            self.toBlock = Button(self.container1)
            self.toBlock.configure(text="Press to go to the next block")
            self.toBlock.bind("<Button-1>", self.toBlockCallback)
            self.toBlock.grid(column=0, row=1)
        else:
            self.breakLabel.configure(text="OK, you're done.")
            self.exitButton = Button(self.container1)
            self.exitButton.configure(text="Press to exit the experiment")
            self.exitButton.bind("<Button-1>", lambda e: e.widget.quit())
            self.exitButton.grid(column=0, row=1)

    def toBlockCallback(self, event):
        self.container1.grid_forget() 
        blockinstance = block.Block(self.myParent, self.myBlockData)

        
