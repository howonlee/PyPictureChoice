#misc utilities
import os, httplib, urllib, sys, random
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
    #no response needed, thankyouverramuch
    connection.close()

def getpics():
    animallist = os.listdir('.\\animals') #still has all sort of cruft in
    animallist.sort()
    noanimallist = os.listdir('.\\noanimals')
    noanimallist.sort()#note that animallist and noanimallist must be equal lengths
    pics = []
    for f in range(len(animallist)):
        animalimage = Image.open(os.path.join('.\\animals', animallist[f]))
        noanimalimage = Image.open(os.path.join('.\\noanimals', noanimallist[f]))
        pics.append((animalimage, noanimalimage))
    random.shuffle(pics)
    return pics


