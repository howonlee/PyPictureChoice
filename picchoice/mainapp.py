from Tkinter import *
from ttk import *
import block

class MainApp:
    def __init__(self, parent, blockData, pics):
        self.myParent = parent
        self.myBlockData = blockData
        self.myPics = pics
        self.container1 = Frame(parent)
        self.screenwidth = self.myParent.winfo_screenwidth()
        self.screenheight = self.myParent.winfo_screenheight()
        self.container1.rowconfigure(0, minsize=self.screenheight * 0.8)
        self.container1.rowconfigure(1, minsize=self.screenheight * 0.2)
        self.container1.grid()
        self.mainLabel = Label(self.container1)
        self.mainLabel.configure(text="Welcome to the experiment.\n\nYou will see a sequence of 50 pictures, broken into two blocks. At the end of each picture, there will be a checkerboard mask. Press \"YES\" if there is an animal in the picture (People count as animals). Press \"NO\" if there is no animal in the picture.\n\nAfter you press the \"YES\" or \"NO\" button, the next picture will be displayed.\n\n")
        self.mainLabel.grid(column=0, row=0, sticky=(N, W, E))
        self.toBlock = Button(self.container1)
        self.buttonwidth = self.screenwidth / 8
        self.toBlock.configure(text="Press to start game", width=self.buttonwidth)
        self.toBlock.focus_force()
        self.toBlock.bind("<Button-1>", self.toBlockClick)
        self.toBlock.grid(column=0, row=1, sticky=(N, W, E, S))
    
    def toBlockClick(self, event):
        ''' toBlockClick
         pressed in main screen, goes to block screens '''
        self.container1.grid_forget()
        blockinstance = block.Block(self.myParent, self.myBlockData, self.myPics)
 
