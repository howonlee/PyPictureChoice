from Tkinter import *
from ttk import *
import our_break, misc
import Image, ImageTk 
import random, gc

class Choice:
    def __init__(self, parent, blockData, pics, trialNum, possibleTimes=[], picQueue = []):
        self.myParent = parent
        self.myBlockData = blockData
        self.currTrialData = {"exp_id" : self.myBlockData["exp_id"], "block_num" : self.myBlockData["block_num"]} #and then insert everything else afterwards
        self.currTrialData['pic_id'] = -1 #to catch mistakes
        self.myPics = pics
        self.numTrials = 49 #it always does one more than this number
                            #everything else works fine, so go with 49
        self.numSixes = 18
        self.numOthers = 7 
        self.picqueue = []
        if (not picQueue):
            self.picqueue = self.formPicQueue(self.myPics)
        else:
            self.picqueue = picQueue
        self.possibleTimes = possibleTimes 
        self.thisTrial = trialNum
        self.visState = 0
        self.currAfter = None
        self.container1 = Frame(parent)
        self.container1.rowconfigure(1, minsize=misc.getHeight(parent))
        self.container1.grid()
        self.picLabel = Label(self.container1)
        self.feedbackLabel = Label(self.container1, style="Inversed.TLabel")
        self.choice1 = Button(self.container1, text="Yes", width=misc.getButtonWidth(parent) / 2)
        self.choice2 = Button(self.container1, text="No", width=misc.getButtonWidth(parent) / 2)
        self.leftLabel = Label(self.myParent, text="Yes", style="Inversed.TLabel")
        self.rightLabel = Label(self.myParent, text="No ", style="Inversed.TLabel")
        self.cycleVis()

    #choice screen is a state machine

    def cycleVis(self, event=None):
        #kill extraneous after stuff, in case of keyboard interrupt
        if (self.currAfter):
            self.myParent.after_cancel(self.currAfter)

        #default choice made
        #pics have been shuffled already
        if (self.visState == 0):
            self.currTrialData['choice_made'] = 0
            self.imageTuple = self.picqueue.pop()
            self.image1 = Image.open(self.imageTuple[0])
            self.currTrialData['pic_id'] = self.imageTuple[2]
            self.photoimage1 = ImageTk.PhotoImage(self.image1)
            self.picLabel.configure(image = self.photoimage1)
            self.picLabel.grid(column=1, row=1)
            #self.currTime = self.getNextTime()
            self.currTrialData['time_begin'] = misc.getCurrTime()
            self.currTrialData['pic_length'] = 2000000
            self.myParent.bind("<space>", self.cycleVis)
            self.currAfter = self.myParent.after(2000000, self.cycleVis)
        elif (self.visState == 1):
            self.currTrialData['time_pic_click'] = misc.getCurrTime()
            self.currTrialData['time_end'] = misc.getCurrTime()
            self.imageFile = "./blankscreen.jpg"
            self.image1 = Image.open(self.imageFile)
            self.photoimage1 = ImageTk.PhotoImage(self.image1)
            self.picLabel.configure(image = self.photoimage1)
            self.currTrialData['mask_begin'] = misc.getCurrTime()
            self.currAfter = self.myParent.after(1000, self.cycleVis)
            self.myParent.bind("<space>", self.doNothing)
        elif (self.visState == 2):
            self.currTrialData['mask_end'] = misc.getCurrTime()
            self.myParent.bind("<space>", self.doNothing)
            self.image2 = Image.open(self.imageTuple[1])
            self.photoimage2 = ImageTk.PhotoImage(self.image2)
            self.picLabel.configure(image = self.photoimage2)
            self.currTrialData['time2_begin'] = misc.getCurrTime()
            self.myParent.bind("<Control_L>", self.choice1Callback)
            self.myParent.bind("<Control_R>", self.choice2Callback)
            self.leftLabel.place(anchor=SW, rely=1, y=-2)
            self.rightLabel.place(anchor=SE, relx=1, rely=1, x=-2, y=-2)
            self.currAfter = self.myParent.after(2000000, self.cycleVis)
            gc.collect()
        elif (self.visState == 3):
            self.picLabel.grid_forget()
            self.currTrialData['time2_end'] = misc.getCurrTime()
            self.myParent.bind("<Control_L>", self.doNothing)
            self.myParent.bind("<Control_R>", self.doNothing)
            self.leftLabel.place_forget()
            self.rightLabel.place_forget()
            #self.choice1.grid_forget()
            #self.choice2.grid_forget()
            self.feedbackLabel.configure(text=self.getFeedback(self.currTrialData['choice_made'], self.currTrialData['pic_id']))
            self.feedbackLabel.grid(column=1, row=1)
            self.currAfter = self.myParent.after(500, self.checkTrial)
        self.visState += 1
        if (self.visState > 3):
            self.visState = 0

    def doNothing(self, event):
        pass

    #def getNextTime(self):
        #if not self.possibleTimes:
        #    for i in range(5):
        #        self.possibleTimes.append((i + 1) * 50)
        #    random.shuffle(self.possibleTimes)
        #print str(self.possibleTimes)
        #return self.possibleTimes.pop() 

    def choice1Callback(self, event):#eventually, we can just call choice again
        self.currTrialData["choice_made"] = 1 
        self.currTrialData['time_click'] = misc.getCurrTime()
        misc.postData(self.currTrialData, "www.stanford.edu", "/group/pdplab/cgi-bin/mobiletrialscript.php")
        self.cycleVis()
        
    def choice2Callback(self, event):
        self.currTrialData["choice_made"] = -1
        self.currTrialData['time_click'] = misc.getCurrTime()
        misc.postData(self.currTrialData, "www.stanford.edu", "/group/pdplab/cgi-bin/mobiletrialscript.php")
        self.cycleVis()
 
    def checkTrial(self):
        if (self.thisTrial < self.numTrials):
            self.container1.grid_forget()
            self.__init__(self.myParent, self.myBlockData, self.myPics, (self.thisTrial + 1), self.possibleTimes, self.picqueue)
        else:
            self.myBlockData['time_end'] = misc.getCurrTime() 
            self.container1.grid_forget()
            our_breakinstance = our_break.Break(self.myParent, self.myBlockData, self.myPics)

    def getFeedback(self, choice, currPicId):
        feedbackString = ""
        if (choice == 1 and "c" in currPicId):
            feedbackString = "Correct!"
        elif (choice == -1 and not "c" in currPicId):
            feedbackString = "Correct!"
        elif (choice == 0):
            feedbackString = "Too late!"
        else:
            feedbackString = "Incorrect!"
        return feedbackString

    def formPicQueue(self, pics):
        picQueue = []
        for i in range(self.numSixes): #18 is number of sixes
            picQueue.append(pics[0].pop(0))
            picQueue.append(pics[2].pop(0))
        for i in range(self.numOthers):
            picQueue.append(pics[1].pop(0))
            picQueue.append(pics[3].pop(0))
        random.shuffle(picQueue)
        return picQueue
