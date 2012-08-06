from Tkinter import *
from ttk import *
import block, misc

class MainApp:
    def __init__(self, parent, blockData, pics):
        self.myParent = parent
        self.myBlockData = blockData
        self.myPics = pics
        self.container1 = Frame(parent, style="Card.TFrame")
        self.container1.rowconfigure(0, minsize=misc.getHeight(parent) * 0.75)
        self.container1.rowconfigure(1, minsize=misc.getHeight(parent) * 0.05)
        self.container1.rowconfigure(2, minsize=misc.getHeight(parent) * 0.2)
        self.container1.grid()
        self.container2 = Frame(self.container1, style="Card.TFrame")
        self.container2.configure(padding = (misc.getWidth(parent) * 0.12, misc.getHeight(parent) * 0.12, 0, 0))
        self.container2.grid()
        self.mainLabel = Label(self.container2, text="Welcome to the experiment.\nThis is a change detection task.\nYou will see two images presented one after another.\nIn each image, there will be several colored squares scattered over the entire image.\nSometimes one of the squares will change in color from the 1st image to the 2nd image.\nPress the YES button if there is such a change, and press the NO button if there is no change.\nYou will receive feedback on whether your judgement is correct or incorrect.\nAfter the feedback, the next trial will start.\nEnter your Mechanical Turk ID below.", style='MainLabel.TLabel')
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
 
