from Tkinter import *
from ttk import *
from picchoice.mainapp import *
import httplib, urllib

params = urllib.urlencode({'android_machine': 'PC', 'serial': 0})
headers = {"Content-type" : "application/x-www-form-urlencoded",
           "Accept": "text/plain"}

connection = httplib.HTTPConnection("www.stanford.edu")
connection.request("POST", "/group/pdplab/cgi-bin/mobileexpscript.php", params, headers)
response = connection.getresponse()
print "response status: " + response.status
print "response reason: " + response.reason
data = response.read()
expId = int(data)
print expId
connection.close()

blockData = {'beginTime' : 0, 'endTime' : 0, 'breakBeginTime' : 0, 
            'breakEndTime' : 0, 'interrupted' : False, 'expId' : expId,
            'blockNum' : 1}

print "block data: " + blockData
version = 1 #for version checking

root = Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.overrideredirect(1)
root.geometry("%dx%d+0+0" % (w, h))
root.focus_set()
root.bind("<Escape>", lambda e: e.widget.quit())
app = MainApp(root, blockData)
root.mainloop()
