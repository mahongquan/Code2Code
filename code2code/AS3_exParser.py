# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 AS3_ex.g 2014-02-25 23:33:47

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *

 
madict={}
madict["Number"]="float"
madict["Array"]= "CCArray * "
madict["MovieClip"]="CCSprite * "
madict["Boolean"]="bool"
madict["Point"]="CCPoint"



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
SHR=29
LOR=37
DOLLAR=42
DEC=27
EXPONENT=71
LT=13
LBRACK=9
STAR=23
BACKSLASH_SEQUENCE=66
MOD=25
SHL=28
REGULAR_EXPR_BODY=65
MOD_ASSIGN=44
GTE=16
SUB=22
IDENT_ASCII_START=75
NOT=34
HEX_NUMBER_LITERAL=69
AND=31
EOF=-1
LTE=15
DIV_ASSIGN=43
LPAREN=7
ESCAPE_SEQUENCE=56
RPAREN=8
INC=26
UNICODE_ESCAPE=55
EOL=57
SHL_ASSIGN=47
DEC_NUMBER_LITERAL=72
COMMA=12
IDENTIFIER=74
REGULAR_EXPR_FIRST_CHAR=63
IDENT_NAME_ASCII_START=73
PLUS=21
EQ=17
DOT=11
JING=48
SHU=30
RBRACK=10
XOR=33
ADD_ASSIGN=45
INV=35
ALPHABET=50
NSAME=20
NUMBER=51
REGULAR_EXPR_FLAG=68
DOUBLE_QUOTE_LITERAL=62
WHITESPACE=58
HEX_DIGIT=52
LCURLY=5
UNDERSCORE=41
ZHI=49
SEMI=4
SAME=19
REGULAR_EXPR_CHAR=64
COLON=39
NEQ=18
SINGLE_QUOTE_LITERAL=61
QUE=38
RCURLY=6
OR=32
ASSIGN=40
IDENT_PART=67
GT=14
DEC_NUMBER=70
DIV=24
CR=53
SUB_ASSIGN=46
LAND=36
COMMENT_MULTILINE=59
COMMENT_SINGLELINE=60
LF=54

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "SEMI", "LCURLY", "RCURLY", "LPAREN", "RPAREN", "LBRACK", "RBRACK", 
    "DOT", "COMMA", "LT", "GT", "LTE", "GTE", "EQ", "NEQ", "SAME", "NSAME", 
    "PLUS", "SUB", "STAR", "DIV", "MOD", "INC", "DEC", "SHL", "SHR", "SHU", 
    "AND", "OR", "XOR", "NOT", "INV", "LAND", "LOR", "QUE", "COLON", "ASSIGN", 
    "UNDERSCORE", "DOLLAR", "DIV_ASSIGN", "MOD_ASSIGN", "ADD_ASSIGN", "SUB_ASSIGN", 
    "SHL_ASSIGN", "JING", "ZHI", "ALPHABET", "NUMBER", "HEX_DIGIT", "CR", 
    "LF", "UNICODE_ESCAPE", "ESCAPE_SEQUENCE", "EOL", "WHITESPACE", "COMMENT_MULTILINE", 
    "COMMENT_SINGLELINE", "SINGLE_QUOTE_LITERAL", "DOUBLE_QUOTE_LITERAL", 
    "REGULAR_EXPR_FIRST_CHAR", "REGULAR_EXPR_CHAR", "REGULAR_EXPR_BODY", 
    "BACKSLASH_SEQUENCE", "IDENT_PART", "REGULAR_EXPR_FLAG", "HEX_NUMBER_LITERAL", 
    "DEC_NUMBER", "EXPONENT", "DEC_NUMBER_LITERAL", "IDENT_NAME_ASCII_START", 
    "IDENTIFIER", "IDENT_ASCII_START"
]




class AS3_exParser(Parser):
    grammarFileName = "AS3_ex.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 18, 2009 10:09:25")
    antlr_version_str = "3.1.3 Mar 18, 2009 10:09:25"
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(AS3_exParser, self).__init__(input, state, *args, **kwargs)

        self._state.ruleMemo = {}





        self._adaptor = None
        self.adaptor = CommonTreeAdaptor()
                


        
    def getTreeAdaptor(self):
        return self._adaptor

    def setTreeAdaptor(self, adaptor):
        self._adaptor = adaptor

    adaptor = property(getTreeAdaptor, setTreeAdaptor)

     
    def converT(self,t):
        global madict
        r=madict.get(t)
        if r!=None:
            return r
        else:
            return t


    class numericLiteral_return(ParserRuleReturnScope):
        def __init__(self):
            super(AS3_exParser.numericLiteral_return, self).__init__()

            self.tree = None




    # $ANTLR start "numericLiteral"
    # AS3_ex.g:236:1: numericLiteral : (D= DEC_NUMBER_LITERAL | H= HEX_NUMBER_LITERAL );
    def numericLiteral(self, ):

        retval = self.numericLiteral_return()
        retval.start = self.input.LT(1)
        numericLiteral_StartIndex = self.input.index()
        root_0 = None

        D = None
        H = None

        D_tree = None
        H_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 1):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # AS3_ex.g:237:5: (D= DEC_NUMBER_LITERAL | H= HEX_NUMBER_LITERAL )
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if (LA1_0 == DEC_NUMBER_LITERAL) :
                    alt1 = 1
                elif (LA1_0 == HEX_NUMBER_LITERAL) :
                    alt1 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 1, 0, self.input)

                    raise nvae

                if alt1 == 1:
                    # AS3_ex.g:238:5: D= DEC_NUMBER_LITERAL
                    pass 
                    root_0 = self._adaptor.nil()

                    D=self.match(self.input, DEC_NUMBER_LITERAL, self.FOLLOW_DEC_NUMBER_LITERAL_in_numericLiteral2187)
                    if self._state.backtracking == 0:

                        D_tree = self._adaptor.createWithPayload(D)
                        self._adaptor.addChild(root_0, D_tree)

                    if self._state.backtracking == 0:
                                 
                        pass#self.pass#Emit(D);
                                



                elif alt1 == 2:
                    # AS3_ex.g:242:7: H= HEX_NUMBER_LITERAL
                    pass 
                    root_0 = self._adaptor.nil()

                    H=self.match(self.input, HEX_NUMBER_LITERAL, self.FOLLOW_HEX_NUMBER_LITERAL_in_numericLiteral2209)
                    if self._state.backtracking == 0:

                        H_tree = self._adaptor.createWithPayload(H)
                        self._adaptor.addChild(root_0, H_tree)

                    if self._state.backtracking == 0:
                                 
                        pass#self.pass#Emit(H);
                                



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 1, numericLiteral_StartIndex, success)

            pass
        return retval

    # $ANTLR end "numericLiteral"

    class stringLiteral_return(ParserRuleReturnScope):
        def __init__(self):
            super(AS3_exParser.stringLiteral_return, self).__init__()

            self.tree = None




    # $ANTLR start "stringLiteral"
    # AS3_ex.g:248:1: stringLiteral : (S= SINGLE_QUOTE_LITERAL | D= DOUBLE_QUOTE_LITERAL );
    def stringLiteral(self, ):

        retval = self.stringLiteral_return()
        retval.start = self.input.LT(1)
        stringLiteral_StartIndex = self.input.index()
        root_0 = None

        S = None
        D = None

        S_tree = None
        D_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 2):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # AS3_ex.g:249:5: (S= SINGLE_QUOTE_LITERAL | D= DOUBLE_QUOTE_LITERAL )
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if (LA2_0 == SINGLE_QUOTE_LITERAL) :
                    alt2 = 1
                elif (LA2_0 == DOUBLE_QUOTE_LITERAL) :
                    alt2 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 2, 0, self.input)

                    raise nvae

                if alt2 == 1:
                    # AS3_ex.g:250:5: S= SINGLE_QUOTE_LITERAL
                    pass 
                    root_0 = self._adaptor.nil()

                    S=self.match(self.input, SINGLE_QUOTE_LITERAL, self.FOLLOW_SINGLE_QUOTE_LITERAL_in_stringLiteral2256)
                    if self._state.backtracking == 0:

                        S_tree = self._adaptor.createWithPayload(S)
                        self._adaptor.addChild(root_0, S_tree)

                    if self._state.backtracking == 0:
                             
                        pass#self.pass#Emit(S);
                            



                elif alt2 == 2:
                    # AS3_ex.g:254:7: D= DOUBLE_QUOTE_LITERAL
                    pass 
                    root_0 = self._adaptor.nil()

                    D=self.match(self.input, DOUBLE_QUOTE_LITERAL, self.FOLLOW_DOUBLE_QUOTE_LITERAL_in_stringLiteral2273)
                    if self._state.backtracking == 0:

                        D_tree = self._adaptor.createWithPayload(D)
                        self._adaptor.addChild(root_0, D_tree)

                    if self._state.backtracking == 0:
                             
                        pass#self.pass#Emit(D);
                            



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 2, stringLiteral_StartIndex, success)

            pass
        return retval

    # $ANTLR end "stringLiteral"

    class identifierLiteral_return(ParserRuleReturnScope):
        def __init__(self):
            super(AS3_exParser.identifierLiteral_return, self).__init__()

            self.value = None
            self.tree = None




    # $ANTLR start "identifierLiteral"
    # AS3_ex.g:261:1: identifierLiteral returns [value] : I= IDENTIFIER ;
    def identifierLiteral(self, ):

        retval = self.identifierLiteral_return()
        retval.start = self.input.LT(1)
        identifierLiteral_StartIndex = self.input.index()
        root_0 = None

        I = None

        I_tree = None

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 3):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # AS3_ex.g:262:5: (I= IDENTIFIER )
                # AS3_ex.g:263:5: I= IDENTIFIER
                pass 
                root_0 = self._adaptor.nil()

                I=self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_identifierLiteral2321)
                if self._state.backtracking == 0:

                    I_tree = self._adaptor.createWithPayload(I)
                    self._adaptor.addChild(root_0, I_tree)

                if self._state.backtracking == 0:
                             
                    retval.value = self.converT(I.text)
                            




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 3, identifierLiteral_StartIndex, success)

            pass
        return retval

    # $ANTLR end "identifierLiteral"

    class literal_return(ParserRuleReturnScope):
        def __init__(self):
            super(AS3_exParser.literal_return, self).__init__()

            self.value = None
            self.tree = None




    # $ANTLR start "literal"
    # AS3_ex.g:270:1: literal returns [value] : ( numericLiteral | stringLiteral );
    def literal(self, ):

        retval = self.literal_return()
        retval.start = self.input.LT(1)
        literal_StartIndex = self.input.index()
        root_0 = None

        numericLiteral1 = None

        stringLiteral2 = None



        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 4):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # AS3_ex.g:271:5: ( numericLiteral | stringLiteral )
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if (LA3_0 == HEX_NUMBER_LITERAL or LA3_0 == DEC_NUMBER_LITERAL) :
                    alt3 = 1
                elif ((SINGLE_QUOTE_LITERAL <= LA3_0 <= DOUBLE_QUOTE_LITERAL)) :
                    alt3 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 3, 0, self.input)

                    raise nvae

                if alt3 == 1:
                    # AS3_ex.g:272:6: numericLiteral
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_numericLiteral_in_literal2375)
                    numericLiteral1 = self.numericLiteral()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, numericLiteral1.tree)
                    if self._state.backtracking == 0:
                                 
                        retval.value=((numericLiteral1 is not None) and [self.input.toString(numericLiteral1.start,numericLiteral1.stop)] or [None])[0]
                                



                elif alt3 == 2:
                    # AS3_ex.g:276:7: stringLiteral
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_stringLiteral_in_literal2394)
                    stringLiteral2 = self.stringLiteral()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, stringLiteral2.tree)
                    if self._state.backtracking == 0:
                                 
                        retval.value=((stringLiteral2 is not None) and [self.input.toString(stringLiteral2.start,stringLiteral2.stop)] or [None])[0]
                                



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 4, literal_StartIndex, success)

            pass
        return retval

    # $ANTLR end "literal"

    class fileContents_return(ParserRuleReturnScope):
        def __init__(self):
            super(AS3_exParser.fileContents_return, self).__init__()

            self.value = None
            self.tree = None




    # $ANTLR start "fileContents"
    # AS3_ex.g:282:1: fileContents returns [value] : ( stringLiteral | numericLiteral | identifierLiteral | EOL | xx= ( LCURLY | RCURLY | WHITESPACE | DOT | STAR | SEMI | COLON | ASSIGN | JING | COMMA | LPAREN | RPAREN | ZHI | DIV ) )* EOF ;
    def fileContents(self, ):

        retval = self.fileContents_return()
        retval.start = self.input.LT(1)
        fileContents_StartIndex = self.input.index()
        root_0 = None

        xx = None
        EOL6 = None
        EOF7 = None
        stringLiteral3 = None

        numericLiteral4 = None

        identifierLiteral5 = None


        xx_tree = None
        EOL6_tree = None
        EOF7_tree = None

              
        retval.value=unicode("")

        success = False
        try:
            try:
                if self._state.backtracking > 0 and self.alreadyParsedRule(self.input, 5):
                    # for cached failed rules, alreadyParsedRule will raise an exception
                    success = True
                    return retval

                # AS3_ex.g:286:5: ( ( stringLiteral | numericLiteral | identifierLiteral | EOL | xx= ( LCURLY | RCURLY | WHITESPACE | DOT | STAR | SEMI | COLON | ASSIGN | JING | COMMA | LPAREN | RPAREN | ZHI | DIV ) )* EOF )
                # AS3_ex.g:287:5: ( stringLiteral | numericLiteral | identifierLiteral | EOL | xx= ( LCURLY | RCURLY | WHITESPACE | DOT | STAR | SEMI | COLON | ASSIGN | JING | COMMA | LPAREN | RPAREN | ZHI | DIV ) )* EOF
                pass 
                root_0 = self._adaptor.nil()

                # AS3_ex.g:287:5: ( stringLiteral | numericLiteral | identifierLiteral | EOL | xx= ( LCURLY | RCURLY | WHITESPACE | DOT | STAR | SEMI | COLON | ASSIGN | JING | COMMA | LPAREN | RPAREN | ZHI | DIV ) )*
                while True: #loop4
                    alt4 = 6
                    LA4 = self.input.LA(1)
                    if LA4 == SINGLE_QUOTE_LITERAL or LA4 == DOUBLE_QUOTE_LITERAL:
                        alt4 = 1
                    elif LA4 == HEX_NUMBER_LITERAL or LA4 == DEC_NUMBER_LITERAL:
                        alt4 = 2
                    elif LA4 == IDENTIFIER:
                        alt4 = 3
                    elif LA4 == EOL:
                        alt4 = 4
                    elif LA4 == SEMI or LA4 == LCURLY or LA4 == RCURLY or LA4 == LPAREN or LA4 == RPAREN or LA4 == DOT or LA4 == COMMA or LA4 == STAR or LA4 == DIV or LA4 == COLON or LA4 == ASSIGN or LA4 == JING or LA4 == ZHI or LA4 == WHITESPACE:
                        alt4 = 5

                    if alt4 == 1:
                        # AS3_ex.g:288:9: stringLiteral
                        pass 
                        self._state.following.append(self.FOLLOW_stringLiteral_in_fileContents2445)
                        stringLiteral3 = self.stringLiteral()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, stringLiteral3.tree)
                        if self._state.backtracking == 0:
                                     
                            retval.value+=((stringLiteral3 is not None) and [self.input.toString(stringLiteral3.start,stringLiteral3.stop)] or [None])[0]
                                    



                    elif alt4 == 2:
                        # AS3_ex.g:293:10: numericLiteral
                        pass 
                        self._state.following.append(self.FOLLOW_numericLiteral_in_fileContents2468)
                        numericLiteral4 = self.numericLiteral()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, numericLiteral4.tree)
                        if self._state.backtracking == 0:
                                     
                            retval.value+=((numericLiteral4 is not None) and [self.input.toString(numericLiteral4.start,numericLiteral4.stop)] or [None])[0]
                                    



                    elif alt4 == 3:
                        # AS3_ex.g:297:10: identifierLiteral
                        pass 
                        self._state.following.append(self.FOLLOW_identifierLiteral_in_fileContents2489)
                        identifierLiteral5 = self.identifierLiteral()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, identifierLiteral5.tree)
                        if self._state.backtracking == 0:
                                     
                            retval.value+=((identifierLiteral5 is not None) and [self.input.toString(identifierLiteral5.start,identifierLiteral5.stop)] or [None])[0]
                                    



                    elif alt4 == 4:
                        # AS3_ex.g:301:10: EOL
                        pass 
                        EOL6=self.match(self.input, EOL, self.FOLLOW_EOL_in_fileContents2510)
                        if self._state.backtracking == 0:

                            EOL6_tree = self._adaptor.createWithPayload(EOL6)
                            self._adaptor.addChild(root_0, EOL6_tree)

                        if self._state.backtracking == 0:
                                     
                            retval.value+=EOL6.text
                                    



                    elif alt4 == 5:
                        # AS3_ex.g:306:9: xx= ( LCURLY | RCURLY | WHITESPACE | DOT | STAR | SEMI | COLON | ASSIGN | JING | COMMA | LPAREN | RPAREN | ZHI | DIV )
                        pass 
                        xx = self.input.LT(1)
                        if (SEMI <= self.input.LA(1) <= RPAREN) or (DOT <= self.input.LA(1) <= COMMA) or (STAR <= self.input.LA(1) <= DIV) or (COLON <= self.input.LA(1) <= ASSIGN) or (JING <= self.input.LA(1) <= ZHI) or self.input.LA(1) == WHITESPACE:
                            self.input.consume()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, self._adaptor.createWithPayload(xx))
                            self._state.errorRecovery = False

                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            mse = MismatchedSetException(None, self.input)
                            raise mse


                        if self._state.backtracking == 0:
                                     
                            retval.value+=xx.text
                                    



                    else:
                        break #loop4
                EOF7=self.match(self.input, EOF, self.FOLLOW_EOF_in_fileContents2771)
                if self._state.backtracking == 0:

                    EOF7_tree = self._adaptor.createWithPayload(EOF7)
                    self._adaptor.addChild(root_0, EOF7_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                success = True
            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:
            if self._state.backtracking > 0:
                self.memoize(self.input, 5, fileContents_StartIndex, success)

            pass
        return retval

    # $ANTLR end "fileContents"


    # Delegated rules


 

    FOLLOW_DEC_NUMBER_LITERAL_in_numericLiteral2187 = frozenset([1])
    FOLLOW_HEX_NUMBER_LITERAL_in_numericLiteral2209 = frozenset([1])
    FOLLOW_SINGLE_QUOTE_LITERAL_in_stringLiteral2256 = frozenset([1])
    FOLLOW_DOUBLE_QUOTE_LITERAL_in_stringLiteral2273 = frozenset([1])
    FOLLOW_IDENTIFIER_in_identifierLiteral2321 = frozenset([1])
    FOLLOW_numericLiteral_in_literal2375 = frozenset([1])
    FOLLOW_stringLiteral_in_literal2394 = frozenset([1])
    FOLLOW_stringLiteral_in_fileContents2445 = frozenset([4, 5, 6, 7, 8, 11, 12, 23, 24, 39, 40, 48, 49, 57, 58, 61, 62, 69, 72, 74])
    FOLLOW_numericLiteral_in_fileContents2468 = frozenset([4, 5, 6, 7, 8, 11, 12, 23, 24, 39, 40, 48, 49, 57, 58, 61, 62, 69, 72, 74])
    FOLLOW_identifierLiteral_in_fileContents2489 = frozenset([4, 5, 6, 7, 8, 11, 12, 23, 24, 39, 40, 48, 49, 57, 58, 61, 62, 69, 72, 74])
    FOLLOW_EOL_in_fileContents2510 = frozenset([4, 5, 6, 7, 8, 11, 12, 23, 24, 39, 40, 48, 49, 57, 58, 61, 62, 69, 72, 74])
    FOLLOW_set_in_fileContents2542 = frozenset([4, 5, 6, 7, 8, 11, 12, 23, 24, 39, 40, 48, 49, 57, 58, 61, 62, 69, 72, 74])
    FOLLOW_EOF_in_fileContents2771 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("AS3_exLexer", AS3_exParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
