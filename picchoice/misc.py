#misc utilities
import os, httplib, urllib, sys, random, time, string
import Image, ImageTk

def getExpId():
    params = urllib.urlencode({'android_machine': 'PC', 'serial': 0})
    headers = {"Content-type" : "application/x-www-form-urlencoded",
           "Accept": "text/plain"}

    connection = httplib.HTTPConnection("www.stanford.edu")
    connection.request("POST", "/group/pdplab/cgi-bin/mobileexpscript.php", params, headers)
    response = connection.getresponse()
    print "response status: " + str(response.status)
    print "response reason: " + response.reason
    data = response.read()
    expId = int(data)
    return expId
    connection.close()

def postData(datadict, urlbase, urlpath):
    #certainly more boilerplaty than the above, but it get repeated a lot
    params = urllib.urlencode(datadict)
    headers = {"Content-type" : "application/x-www-form-urlencoded", "Accept": "text/plain"}
    connection = httplib.HTTPConnection(urlbase)
    connection.request("POST", urlpath, params, headers)
    #debugging follows
    #response = connection.getresponse()
    #print "response status: " + str(response.status)
    #print "response reason: " + response.reason
    connection.close()

def getpics():
    pics = []
    pics.append(getCat('.\\first\\changesixes','.\\second\\changesixes'))
    pics.append(getCat('.\\first\\changeothers','.\\second\\changeothers'))
    pics.append(getCat('.\\first\\nochangesixes','.\\second\\nochangesixes'))
    pics.append(getCat('.\\first\\nochangeothers','.\\second\\nochangeothers'))
    return pics

def getCat(firstdir, seconddir):
    firstlist = os.listdir(firstdir)
    firstlist.sort()
    secondlist = os.listdir(seconddir)
    secondlist.sort()
    cat = []
    for f in range(len(firstlist)):
        firstimage = os.path.join(firstdir, firstlist[f])
        secondimage = os.path.join(seconddir, secondlist[f])
        cat.append((firstimage, secondimage, firstlist[f]))
    random.shuffle(cat)
    return cat 

def getCode():
    chars = string.ascii_uppercase + string.digits
    code = ""
    return code.join(random.choice(chars) for x in range(6))

def getCurrTime():
    return int(time.time() * 1000)

def getWidth(root):
    return root.winfo_screenwidth()

def getButtonWidth(root):
    return (root.winfo_screenwidth() / 22)
 
def getHeight(root):
    return root.winfo_screenheight()
