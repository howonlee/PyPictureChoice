from Tkinter import *
from ttk import *
import block

class Break:
    def __init__(self, parent, blockData):
        self.myParent = parent
        self.myBlockData = blockData
        self.container1 = Frame(parent, width=1000, height=1000)
        self.container1.grid(column=0, row=0)
        self.breakLabel = Label(self.container1)
        self.breakLabel.configure(text="Take a break")
        self.breakLabel.grid(column=0, row=0)
        self.toBlock = Button(self.container1)
        self.toBlock.configure(text="Press to go to the next block")
        self.toBlock.bind("<Button-1>", self.toBlockCallback)
        self.toBlock.grid(column=0, row=1)
    
    def toBlockCallback(self, event):
        self.container1.grid_forget() 
        blockinstance = block.Block(self.myParent, self.myBlockData)

