import sys
import antlr3
import codecs
from AS3_exParser import AS3_exParser
from AS3_exLexer import AS3_exLexer
def testfile():
	s=open("winJingle.as","rb").read()
	print type(s)
	print s[0]
	print hex(ord(s[0]))
	print hex(ord(s[1]))
	print hex(ord(s[2]))
	
	print hex(ord("p"))
	
def treadfile(inputFileName):
    s=codecs.open(inputFileName,"r","utf-8").read()
    if ord(s[0])>256:
    	s=s[1:]
    cStream = antlr3.ANTLRStringStream(s)
    lexer = AS3_exLexer(cStream)
    tStream = antlr3.CommonTokenStream(lexer)
    print tStream,dir(tStream)
    ts=tStream.getTokens()
    for t in ts:
        print t.text
    print "====================="
    parser = AS3_exParser(tStream)
    parser.fileContents();
if __name__=="__main__":
    #print sys.argv
    if len(sys.argv) == 2:
        treadfile(sys.argv[1])

