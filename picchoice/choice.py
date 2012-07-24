from Tkinter import *
from ttk import *
import our_break
import Image, ImageTk 
import time

class Choice:
    def __init__(self, parent, blockData, pics, trialNum):
        self.myParent = parent
        self.myBlockData = blockData
        self.myPics = pics
        self.thisTrial = trialNum
        self.numTrials = 4 
        self.visState = 0
        self.container1 = Frame(parent)
        self.container1.grid()
        self.picLabel = Label(self.container1)
        self.choice1 = Button(self.container1)
        self.choice2 = Button(self.container1)
        self.choice1.configure(text="Choice 1")
        self.choice2.configure(text="Choice 2")
        self.choice1.bind("<Button-1>", self.choice1Callback)
        self.choice2.bind("<Button-1>", self.choice2Callback)
        self.cycleVis()

    #choice screen is a state machine

    def cycleVis(self):
        #pics have been shuffled already
        if (self.visState == 0):
            self.image1 = self.myPics.pop()[0]
            self.photoimage1 = ImageTk.PhotoImage(self.image1)
            self.picLabel.configure(image = self.photoimage1)
            self.picLabel.grid(column=0, row=0)
            self.myParent.after(500, self.cycleVis)
        elif (self.visState == 1):
            self.imageFile = "./checkerboard.jpg"
            self.image1 = Image.open(self.imageFile)
            self.photoimage1 = ImageTk.PhotoImage(self.image1)
            self.picLabel.configure(image = self.photoimage1)
            self.picLabel.grid(column=0, row=0)
            self.myParent.after(500, self.cycleVis)
        elif (self.visState == 2):
            self.picLabel.grid_forget()
            self.choice1.grid(column=0, row=1, sticky=(N, W, S))
            self.choice2.grid(column=1, row=1, sticky=(N, E, S))
        self.visState += 1
        if (self.visState > 2):
            self.visState = 0

    def choice1Callback(self, event):#eventually, we can just call choice again
        self.checkTrial()
        
    def choice2Callback(self, event):
        self.checkTrial()

    def checkTrial(self):
        if (self.thisTrial < self.numTrials):
            self.container1.grid_forget()
            self.myBlockData['endTime'] = int(time.time() * 1000)
            another_trial = Choice(self.myParent, self.myBlockData, self.myPics, (self.thisTrial + 1))
        else:
            self.container1.grid_forget()
            our_breakinstance = our_break.Break(self.myParent, self.myBlockData, self.myPics)
