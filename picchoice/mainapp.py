from Tkinter import *
from ttk import *
import block

class MainApp:
    def __init__(self, parent, blockData):
        self.myParent = parent
        self.myBlockData = blockData
        self.container1 = Frame(parent, width=10000, height=10000)
        self.container1.grid()
        self.mainLabel = Label(self.container1)
        self.mainLabel.configure(text="Welcome to the experiment. Do not press the HOME button for the duration of the experiment.\n\nYou will see a sequence of 50 pictures, broken into two blocks. At the end of each picture, there will be a checkerboard mask. Press \"YES\" if there is an animal in the picture (People count as animals). Press \"NO\" if there is no animal in the picture.\n\nAfter you press the \"YES\" or \"NO\" button, the next picture will be displayed.\n\n")
        self.mainLabel.grid(column=0, row=0, sticky=(N))
        self.toBlock = Button(self.container1)
        self.toBlock.configure(text="Press to start game")
        self.toBlock.focus_force()
        self.toBlock.bind("<Button-1>", self.toBlockClick)
        self.toBlock.grid(column=0, row=1, sticky=(N, W, E, S))
    
    def toBlockClick(self, event):
        ''' toBlockClick
         pressed in main screen, goes to block screens '''
        self.container1.grid_forget()
        blockinstance = block.Block(self.myParent, self.myBlockData)
 
