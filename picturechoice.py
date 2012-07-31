from Tkinter import *
import ttk as ttk
from picchoice.mainapp import *
import picchoice.misc
import Image, ImageTk
import httplib, urllib, os, sys

expId = picchoice.misc.getExpId()
blockData = {'time_begin' : 0, 'time_end' : 0, 'break_time_begin' : 0, 
            'break_time_end' : 0, 'interruption' : False, 'exp_id' : expId,
            'block_num' : 0}
pics = picchoice.misc.getpics()

version = 1 #for version checking, later

root = Tk()
style = ttk.Style()
style.configure('TLabel', font=('Helvetica', 36))
style.configure('MainLabel.TLabel', font=('Helvetica', 16), background= "#8c1515", foreground = "#ddcf99")
style.configure('Card.TLabel', background="#8c1515", foreground="#ddcf99")
style.configure('TButton', font=('Helvetica', 24))
style.configure('Card.TFrame', background="#8c1515")
style.configure('TFrame', background="black")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.configure(background="black")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.overrideredirect(1)
root.geometry("%dx%d+0+0" % (w, h))
root.focus_set()
root.bind("<Escape>", lambda e: e.widget.quit()) #need to bind this to an interruptor
app = MainApp(root, blockData, pics)
root.mainloop()
