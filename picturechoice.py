from Tkinter import *
from ttk import *

class MainApp:
    def __init__(self, parent):
        self.myParent = parent
        self.container1 = Frame(parent)
        self.container1.pack()
        self.mainLabel = Label(self.container1)
        self.mainLabel.configure(text="Welcome to the experiment. Do not press the HOME button for the duration of the experiment.\n\nYou will see a sequence of 50 pictures, broken into two blocks. At the end of each picture, there will be a checkerboard mask. Press \"YES\" if there is an animal in the picture (People count as animals). Press \"NO\" if there is no animal in the picture.\n\nAfter you press the \"YES\" or \"NO\" button, the next picture will be displayed.\n\n")
        self.mainLabel.pack()
        self.toBlock = Button(self.container1)
        self.toBlock.configure(text="Press to start game")
        self.toBlock.focus_force()
        self.toBlock.bind("<Button-1>", self.toBlockClick)
        self.toBlock.pack()
    
    def toBlockClick(self, event):
        ''' toBlockClick
         pressed in main screen, goes to block screens '''
        self.container1.pack_forget()
        block = Block(root)
 
class Block:
    def __init__(self, parent):
        self.myParent = parent
        self.container1 = Frame(parent)
        self.container1.pack()
        self.blockLabel = Label(self.container1)
        self.blockLabel.configure(text="Block #: 0")
        self.blockLabel.pack()
        self.toChoice = Button(self.container1)
        self.toChoice.configure(text="Press to start block")
        self.toChoice.bind("<Button-1>", self.toChoiceCallback)
        self.toChoice.pack()

    def toChoiceCallback(self, event):
        ''' toChoiceCallback
        pressed in block screen, goes to choice screen'''
        self.container1.pack_forget()
        choice = Choice(root)

class Choice:
    def __init__(self, parent):
        self.myParent = parent
        self.container1 = Frame(parent)
        self.container1.pack()
        self.choice1 = Button(self.container1)
        self.choice2 = Button(self.container1)
        self.toBreak = Button(self.container1)
        self.choice1.configure(text="Choice 1")
        self.choice2.configure(text="Choice 2")
        self.toBreak.configure(text="Take a Break")
        self.choice1.bind("<Button-1>", self.choice1Callback)
        self.choice2.bind("<Button-1>", self.choice2Callback)
        self.toBreak.bind("<Button-1>", self.toBreakCallback)
        self.choice1.pack()
        self.choice2.pack()

    def choice1Callback(self, event):
        self.choice1.pack_forget()
        self.choice2.pack_forget()
        self.toBreak.pack()

    def choice2Callback(self, event):
        self.choice1.pack_forget()
        self.choice2.pack_forget()
        self.toBreak.pack()

    def toBreakCallback(self, event):
        self.container1.pack_forget()
        our_break = Break(root)

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

root = Tk()
app = MainApp(root)
root.mainloop()
