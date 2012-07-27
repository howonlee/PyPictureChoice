from Tkinter import *
from ttk import *
import block, misc

class MainApp:
    def __init__(self, parent, blockData, pics):
        self.myParent = parent
        self.myBlockData = blockData
        self.myPics = pics
        self.container1 = Frame(parent)
        self.container1.rowconfigure(0, minsize=misc.getHeight(parent) * 0.75)
        self.container1.rowconfigure(1, minsize=misc.getHeight(parent) * 0.05)
        self.container1.rowconfigure(2, minsize=misc.getHeight(parent) * 0.2)
        self.container1.grid()
        self.mainLabel = Label(self.container1, text="Welcome to the experiment.\n\nYou will see a sequence of 50 pictures, broken into two blocks. At the end of each picture, there will be a checkerboard mask. Press \"YES\" if there is an animal in the picture (People count as animals). Press \"NO\" if there is no animal in the picture.\n\nAfter you press the \"YES\" or \"NO\" button, the next picture will be displayed.\n\nEnter your Mechanical Turk ID below.")
        self.mainLabel.grid(column=0, row=0, sticky=(N, W, E))
        self.mTurkText = Entry(self.container1)
        self.mTurkText.grid(column = 0, row=1)
        self.toBlock = Button(self.container1, text="Press to start game", width=misc.getButtonWidth(parent))
        self.toBlock.focus_force()
        self.toBlock.bind("<Button-1>", self.toBlockClick)
        self.toBlock.grid(column=0, row=2, sticky=(N, W, E, S))
    
    def toBlockClick(self, event):
        ''' toBlockClick
         pressed in main screen, goes to block screens '''
        self.mTurkData = {'mturk_id' : self.mTurkText.get(), 'exp_id' : self.myBlockData['exp_id']}
        misc.postData(self.mTurkData, 'www.stanford.edu', '/group/pdplab/cgi-bin/mturkid.php') 
        self.container1.grid_forget()
        blockinstance = block.Block(self.myParent, self.myBlockData, self.myPics)
 
