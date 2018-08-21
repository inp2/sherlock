#Personal Assistant Utility Functions

from datetime import datetime
import time
import os
import shutil

def testworks():
    print "\n it worked"

#returns id of command NOTE -1 is an error
def parseComm(PAComm):

    PAComm=PAComm.strip()
    PAComm=PAComm.lower()

    words = PAComm.split()
    #for word in words:
        #print(word)
    #print len(words)
    numWords=len(words)
    if numWords <= 0:
        print "Unknown Command"
        return "-1"


    if len(words) >= 3:
        if words[0]== "graph" and words[1] == "observe":
            if "colorapart" in words:
                    return "1.1 " + words[2] + " " + words[words.index("colorapart")+1]
            if "accessorder" in words:
                return "1.2 " + words[2]
            return "1 " + words[2]
        if words[0]== "graph" and words[1] == "formulate":
            return "2 " + words[2]
        if words[0]== "graph" and words[1] == "evaluate":
            return "3 " + words[2] +" "+ words[3]

    elif len(words) ==2:
        if words[0]== "delete" and words[1] == "all":
            return "5"

    return "-1"

#takes dictionary entry of node and returns a string of its time data
def getTimeStr(dictEntry):
    nodeTime=str(dictEntry)
    nodeTime=nodeTime.replace('\'weight\':', '')
    nodeTime=nodeTime.replace('\'', '')
    nodeTime=nodeTime.replace('{', '')
    nodeTime=nodeTime.replace('}', '')
    nodeTime=nodeTime.strip()
    return nodeTime
    #return "29 June 2017 14:15"

#takes string of a node's time and returns it in Unix date/time formatting
def getDateTimeUnix(nodeTime):
    fmt = '%d %B %Y %H:%M'
    dt = datetime.strptime(nodeTime, fmt)
    dtUnix = time.mktime(dt.timetuple())
    return dtUnix

def deleteCaseFiles():
    dirList= os.listdir(os.getcwd())

    for dir in dirList:
        if "case" in dir:
            shutil.rmtree(dir)
