import sys
import antlr3
import codecs
import os
import re
import time
from AS3_exLexer import AS3_exLexer
jiacc=["Layer","Action","Object","Sprite","Point","Scene","Node","MoveTo","Director","Application","Size","Touch","Event"]
dic={}
dic["__Array"]="CCArray"
dic["__Integer"]="CCInteger"
dic["__Float"]="CCFloat"

for one in jiacc:
    dic[one]="CC"+one
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
def convert(s):
    global dic
    if dic.get(s):
        return dic[s]
    return s	
def treadfile(inputFileName,srcpath,outputpath):
    print inputFileName
    (path,filename)=os.path.split(inputFileName)
    path=path[len(srcpath):]
    (leftname,ext)=os.path.splitext(filename)
    s=codecs.open(inputFileName,"r","utf-8").read()
    if ord(s[0])>256:
    	s=s[1:]
    cStream = antlr3.ANTLRStringStream(s)
    lexer = AS3_exLexer(cStream)
    tStream = antlr3.CommonTokenStream(lexer)
    ts=tStream.getTokens()
    if path!="":
        path=outputpath+"/"+path
    else:
        path=outputpath
    print path+"/"+filename
    f=codecs.open(path+"/"+filename,"w","utf-8")
    for t in ts:
        f.write(convert(t.text))
    f.close()
    #parser = AS3_exParser(tStream)
    #parser.fileContents();
if __name__=="__main__":
    #print sys.argv
    if len(sys.argv) == 2:
        treadfile(sys.argv[1],"output")

