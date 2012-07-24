from Tkinter import *
from ttk import *
import block, misc

class Break:
    def __init__(self, parent, blockData, pics):
        self.myParent = parent
        self.myBlockData = blockData
        self.myPics = pics
        self.myBlockData['break_time_begin'] = misc.getCurrTime()
        self.totalNumBlocks = 2
        self.container1 = Frame(parent)
        self.container1.grid()
        self.breakLabel = Label(self.container1)
        self.breakLabel.grid(column=0, row=0)
        if (self.myBlockData['block_num'] < self.totalNumBlocks):
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
        self.myBlockData['break_time_end'] = misc.getCurrTime()
        misc.postData(self.myBlockData, "www.stanford.edu", "/group/pdplab/cgi-bin/mobileblockscript.php")
        self.container1.grid_forget() 
        blockinstance = block.Block(self.myParent, self.myBlockData, self.myPics)

    def exitCallback(self, event):
        self.myBlockData['break_time_end'] = misc.getCurrTime()
        misc.postData(self.myBlockData, "www.stanford.edu", "/group/pdplab/cgi-bin/mobileblockscript.php")
        misc.postData({'exp_id' : self.myBlockData['exp_id']}, "www.stanford.edu", "/group/pdplab/cgi-bin/expend.php")
        print str(self.myBlockData)
        self.myParent.quit()
