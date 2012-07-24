from Tkinter import *
from ttk import *
import our_break, misc
import Image, ImageTk 
import random

class Choice:
    def __init__(self, parent, blockData, pics, trialNum, possibleTimes=[]):
        self.myParent = parent
        self.myBlockData = blockData
        self.currTrialData = {"exp_id" : self.myBlockData["exp_id"], "block_num" : self.myBlockData["block_num"]} #and then insert everything else afterwards
        self.currTrialData['pic_id'] = -1 #to catch mistakes
        self.myPics = pics
        self.possibleTimes = possibleTimes 
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
            self.imageTuple = self.myPics.pop()
            self.image1 = self.imageTuple[0]
            self.currTrialData['pic_id'] = self.imageTuple[2]
            self.photoimage1 = ImageTk.PhotoImage(self.image1)
            self.picLabel.configure(image = self.photoimage1)
            self.picLabel.grid(column=0, row=0)
            self.currTime = self.getNextTime()
            self.currTrialData['time_begin'] = misc.getCurrTime()
            self.currTrialData['pic_length'] = self.currTime
            self.myParent.after(self.currTime, self.cycleVis)
        elif (self.visState == 1):
            self.currTrialData['time_end'] = misc.getCurrTime()
            self.imageFile = "./checkerboard.jpg"
            self.image1 = Image.open(self.imageFile)
            self.photoimage1 = ImageTk.PhotoImage(self.image1)
            self.picLabel.configure(image = self.photoimage1)
            self.picLabel.grid(column=0, row=0)
            self.currTrialData['mask_begin'] = misc.getCurrTime()
            self.myParent.after(500, self.cycleVis)
        elif (self.visState == 2):
            self.picLabel.grid_forget()
            self.currTrialData['mask_end'] = misc.getCurrTime()
            self.choice1.grid(column=0, row=1, sticky=(N, W, S))
            self.choice2.grid(column=1, row=1, sticky=(N, E, S))
        self.visState += 1
        if (self.visState > 2):
            self.visState = 0

    def getNextTime(self):
        if not self.possibleTimes:
            for i in range(5):
                self.possibleTimes.append((i + 1) * 50)
            random.shuffle(self.possibleTimes)
        print str(self.possibleTimes)
        return self.possibleTimes.pop()

    def choice1Callback(self, event):#eventually, we can just call choice again
        self.currTrialData["choice_made"] = 0
        self.currTrialData['time_click'] = misc.getCurrTime()
        misc.postData(self.currTrialData, "www.stanford.edu", "/group/pdplab/cgi-bin/mobiletrialscript.php")
        self.checkTrial()
        
    def choice2Callback(self, event):
        self.currTrialData["choice_made"] = 1
        self.currTrialData['time_click'] = misc.getCurrTime()
        misc.postData(self.currTrialData, "www.stanford.edu", "/group/pdplab/cgi-bin/mobiletrialscript.php")
        self.checkTrial()
 
    def checkTrial(self):
        if (self.thisTrial < self.numTrials):
            self.container1.grid_forget()
            self.myBlockData['time_end'] = misc.getCurrTime() 
            another_trial = Choice(self.myParent, self.myBlockData, self.myPics, (self.thisTrial + 1), self.possibleTimes)
        else:
            self.container1.grid_forget()
            our_breakinstance = our_break.Break(self.myParent, self.myBlockData, self.myPics)
