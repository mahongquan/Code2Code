import os
import re
import time
import upgrade2
def mylistdir(p,f):
    a=os.listdir(p)
    fs=myfind(a,f)
    return(fs)
def myfind(l,p):
    lr=[];
    #print p
    p1=p.replace(".",r"\.")
    p2=p1.replace("*",".*")
    p2=p2+"$"
    for a in l:
        #print a
        if  re.search(p2,a,re.IGNORECASE)==None :
           pass
           #print "pass"
        else:
           lr.append(a)
       #print "append"
    return lr
def myfindstr(a,p):
    p1=p.replace(".",r"\.")
    p2=p1.replace("*",".*")
    p2=p2+"$"
    return re.search(p2,a,re.IGNORECASE)
def fileAS(f):
    return(len(open(f).readlines()))
def outputAs():
    lt=time.localtime()
    path="../test_input"
    files=mylistdir(path,"*.cpp")
    files2=mylistdir(path,"*.h")
    for f in files2:
        files.append(f)
    print files
    for f in  files:
        fn=path+"/"+f
        upgrade2.treadfile(fn,path,"../test_output")
outputAs()