from Tkinter import *
from ttk import *

class Break:
    def __init__(self, parent):
        self.myParent = parent
        self.container1 = Frame(parent)
        self.container1.pack()
        self.breakLabel = Label(self.container1)
        self.breakLabel.configure(text="Take a break")
        self.toBlock = Button(self.container1)
        self.toBlock.configure(text="Press to go to the next block")
        self.toBlock.bind("<Button-1>", self.toBlockCallback)
        self.toBlock.pack()
    
    def toBlockCallback(self, event):
        self.container1.pack_forget() 
        block = Block(root)


