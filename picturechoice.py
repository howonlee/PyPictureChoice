from Tkinter import *
from ttk import *
from picchoice.mainapp import *
import picchoice.misc
import Image, ImageTk
import httplib, urllib, os, sys

expId = picchoice.misc.getExpId()
blockData = {'beginTime' : 0, 'endTime' : 0, 'breakBeginTime' : 0, 
            'breakEndTime' : 0, 'interrupted' : False, 'expId' : expId,
            'blockNum' : 0}
pics = picchoice.misc.getpics()

version = 1 #for version checking, later

root = Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.overrideredirect(1)
root.geometry("%dx%d+0+0" % (w, h))
root.focus_set()
root.bind("<Escape>", lambda e: e.widget.quit())
app = MainApp(root, blockData, pics)
root.mainloop()
