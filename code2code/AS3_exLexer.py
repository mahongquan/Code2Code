# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 AS3_ex.g 2014-02-25 23:33:48

import sys
from antlr3 import *
from antlr3.compat import set, frozenset
          
import AS3_exParser
AS3_exParser.CHANNEL_SLCOMMENT=43;
AS3_exParser.CHANNEL_MLCOMMENT=42;
AS3_exParser.CHANNEL_WHITESPACE=41;
AS3_exParser.CHANNEL_EOL=40;



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
SHR=29
LOR=37
DOLLAR=42
DEC=27
LT=13
EXPONENT=71
STAR=23
LBRACK=9
BACKSLASH_SEQUENCE=66
SHL=28
MOD=25
REGULAR_EXPR_BODY=65
GTE=16
MOD_ASSIGN=44
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
DOUBLE_QUOTE_LITERAL=62
REGULAR_EXPR_FLAG=68
HEX_DIGIT=52
WHITESPACE=58
UNDERSCORE=41
LCURLY=5
ZHI=49
SEMI=4
SAME=19
COLON=39
REGULAR_EXPR_CHAR=64
NEQ=18
SINGLE_QUOTE_LITERAL=61
QUE=38
OR=32
RCURLY=6
ASSIGN=40
IDENT_PART=67
GT=14
DIV=24
DEC_NUMBER=70
CR=53
LAND=36
SUB_ASSIGN=46
COMMENT_MULTILINE=59
LF=54
COMMENT_SINGLELINE=60


class AS3_exLexer(Lexer):

    grammarFileName = "AS3_ex.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 18, 2009 10:09:25")
    antlr_version_str = "3.1.3 Mar 18, 2009 10:09:25"

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super(AS3_exLexer, self).__init__(input, state)


        self.dfa17 = self.DFA17(
            self, 17,
            eot = self.DFA17_eot,
            eof = self.DFA17_eof,
            min = self.DFA17_min,
            max = self.DFA17_max,
            accept = self.DFA17_accept,
            special = self.DFA17_special,
            transition = self.DFA17_transition
            )

        self.dfa25 = self.DFA25(
            self, 25,
            eot = self.DFA25_eot,
            eof = self.DFA25_eof,
            min = self.DFA25_min,
            max = self.DFA25_max,
            accept = self.DFA25_accept,
            special = self.DFA25_special,
            transition = self.DFA25_transition
            )




               
    def converT(self,t):
        if t=="Number":
            return "float"
        else:
            return t



    # $ANTLR start "SEMI"
    def mSEMI(self, ):

        try:
            _type = SEMI
            _channel = DEFAULT_CHANNEL

            # AS3_ex.g:22:6: ( ';' )
            # AS3_ex.g:22:8: ';'
            pass 
            self.match(59)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SEMI"



    # $ANTLR start "LCURLY"
    def mLCURLY(self, ):

        try:
            _type = LCURLY
            _channel = DEFAULT_CHANNEL

            # AS3_ex.g:23:8: ( '{' )
            # AS3_ex.g:23:10: '{'
            pass 
            self.match(123)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LCURLY"



    # $ANTLR start "RCURLY"
    def mRCURLY(self, ):

        try:
            _type = RCURLY
            _channel = DEFAULT_CHANNEL

            # AS3_ex.g:24:8: ( '}' )
            # AS3_ex.g:24:10: '}'
            pass 
            self.match(125)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "RCURLY"



    # $ANTLR start "LPAREN"
    def mLPAREN(self, ):

        try:
            _type = LPAREN
            _channel = DEFAULT_CHANNEL

            # AS3_ex.g:25:8: ( '(' )
            # AS3_ex.g:25:10: '('
            pass 
            self.match(40)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LPAREN"



    # $ANTLR start "RPAREN"
    def mRPAREN(self, ):

        try:
            _type = RPAREN
            _channel = DEFAULT_CHANNEL

            # AS3_ex.g:26:8: ( ')' )
            # AS3_ex.g:26:10: ')'
            pass 
            self.match(41)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "RPAREN"



    # $ANTLR start "LBRACK"
    def mLBRACK(self, ):

        try:
            _type = LBRACK
            _channel = DEFAULT_CHANNEL

            # AS3_ex.g:27:8: ( '[' )
            # AS3_ex.g:27:10: '['
            pass 
            self.match(91)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LBRACK"



    # $ANTLR start "RBRACK"
    def mRBRACK(self, ):

        try:
            _type = RBRACK
            _channel = DEFAULT_CHANNEL

            # AS3_ex.g:28:8: ( ']' )
            # AS3_ex.g:28:10: ']'
            pass 
            self.match(93)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "RBRACK"



    # $ANTLR start "DOT"
    def mDOT(self, ):

        try:
            _type = DOT
            _channel = DEFAULT_CHANNEL

            # AS3_ex.g:29:5: ( '.' )
            # AS3_ex.g:29:7: '.'
            pass 
            self.match(46)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DOT"



    # $ANTLR start "COMMA"
    def mCOMMA(self, ):

        try:
            _type = COMMA
            _channel = DEFAULT_CHANNEL

            # AS3_ex.g:30:7: ( ',' )
            # AS3_ex.g:30:9: ','
            pass 
            self.match(44)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "COMMA"



    # $ANTLR start "LT"
    def mLT(self, ):

        try:
            _type = LT
            _channel = DEFAULT_CHANNEL

            # AS3_ex.g:31:4: ( '<' )
            # AS3_ex.g:31:6: '<'
            pass 
            self.match(60)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LT"



    # $ANTLR start "GT"
    def mGT(self, ):

        try:
            _type = GT
            _channel = DEFAULT_CHANNEL

            # AS3_ex.g:32:4: ( '>' )
            # AS3_ex.g:32:6: '>'
            pass 
            self.match(62)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "GT"



    # $ANTLR start "LTE"
    def mLTE(self, ):

        try:
            _type = LTE
            _channel = DEFAULT_CHANNEL

            # AS3_ex.g:33:5: ( '<=' )
            # AS3_ex.g:33:7: '<='
            pass 
            self.match("<=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LTE"



    # $ANTLR start "EQ"
    def mEQ(self, ):

        try:
            _type = EQ
            _channel = DEFAULT_CHANNEL

            # AS3_ex.g:34:4: ( '==' )
            # AS3_ex.g:34:6: '=='
            pass 
            self.match("==")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "EQ"



    # $ANTLR start "NEQ"
    def mNEQ(self, ):

        try:
            _type = NEQ
            _channel = DEFAULT_CHANNEL

            # AS3_ex.g:35:5: ( '!=' )
            # AS3_ex.g:35:7: '!='
            pass 
            self.match("!=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NEQ"



    # $ANTLR start "SAME"
    def mSAME(self, ):

        try:
            _type = SAME
            _channel = DEFAULT_CHANNEL

            # AS3_ex.g:36:6: ( '===' )
            # AS3_ex.g:36:8: '==='
            pass 
            self.match("===")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SAME"



    # $ANTLR start "NSAME"
    def mNSAME(self, ):

        try:
            _type = NSAME
            _channel = DEFAULT_CHANNEL

            # AS3_ex.g:37:7: ( '!==' )
            # AS3_ex.g:37:9: '!=='
            pass 
            self.match("!==")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NSAME"



    # $ANTLR start "PLUS"
    def mPLUS(self, ):

        try:
            _type = PLUS
            _channel = DEFAULT_CHANNEL

            # AS3_ex.g:38:6: ( '+' )
            # AS3_ex.g:38:8: '+'
            pass 
            self.match(43)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PLUS"



    # $ANTLR start "SUB"
    def mSUB(self, ):

        try:
            _type = SUB
            _channel = DEFAULT_CHANNEL

            # AS3_ex.g:39:5: ( '-' )
            # AS3_ex.g:39:7: '-'
            pass 
            self.match(45)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SUB"



    # $ANTLR start "STAR"
    def mSTAR(self, ):

        try:
            _type = STAR
            _channel = DEFAULT_CHANNEL

            # AS3_ex.g:40:6: ( '*' )
            # AS3_ex.g:40:8: '*'
            pass 
            self.match(42)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "STAR"



    # $ANTLR start "DIV"
    def mDIV(self, ):

        try:
            _type = DIV
            _channel = DEFAULT_CHANNEL

            # AS3_ex.g:41:5: ( '/' )
            # AS3_ex.g:41:7: '/'
            pass 
            self.match(47)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DIV"



    # $ANTLR start "MOD"
    def mMOD(self, ):

        try:
            _type = MOD
            _channel = DEFAULT_CHANNEL

            # AS3_ex.g:42:5: ( '%' )
            # AS3_ex.g:42:7: '%'
            pass 
            self.match(37)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "MOD"



    # $ANTLR start "INC"
    def mINC(self, ):

        try:
            _type = INC
            _channel = DEFAULT_CHANNEL

            # AS3_ex.g:43:5: ( '++' )
            # AS3_ex.g:43:7: '++'
            pass 
            self.match("++")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "INC"



    # $ANTLR start "DEC"
    def mDEC(self, ):

        try:
            _type = DEC
            _channel = DEFAULT_CHANNEL

            # AS3_ex.g:44:5: ( '--' )
            # AS3_ex.g:44:7: '--'
            pass 
            self.match("--")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DEC"



    # $ANTLR start "SHL"
    def mSHL(self, ):

        try:
            _type = SHL
            _channel = DEFAULT_CHANNEL

            # AS3_ex.g:45:5: ( '<<' )
            # AS3_ex.g:45:7: '<<'
            pass 
            self.match("<<")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SHL"



    # $ANTLR start "AND"
    def mAND(self, ):

        try:
            _type = AND
            _channel = DEFAULT_CHANNEL

            # AS3_ex.g:46:5: ( '&' )
            # AS3_ex.g:46:7: '&'
            pass 
            self.match(38)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "AND"



    # $ANTLR start "OR"
    def mOR(self, ):

        try:
            _type = OR
            _channel = DEFAULT_CHANNEL

            # AS3_ex.g:47:4: ( '|' )
            # AS3_ex.g:47:6: '|'
            pass 
            self.match(124)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "OR"



    # $ANTLR start "XOR"
    def mXOR(self, ):

        try:
            _type = XOR
            _channel = DEFAULT_CHANNEL

            # AS3_ex.g:48:5: ( '^' )
            # AS3_ex.g:48:7: '^'
            pass 
            self.match(94)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "XOR"



    # $ANTLR start "NOT"
    def mNOT(self, ):

        try:
            _type = NOT
            _channel = DEFAULT_CHANNEL

            # AS3_ex.g:49:5: ( '!' )
            # AS3_ex.g:49:7: '!'
            pass 
            self.match(33)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NOT"



    # $ANTLR start "INV"
    def mINV(self, ):

        try:
            _type = INV
            _channel = DEFAULT_CHANNEL

            # AS3_ex.g:50:5: ( '~' )
            # AS3_ex.g:50:7: '~'
            pass 
            self.match(126)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "INV"



    # $ANTLR start "LAND"
    def mLAND(self, ):

        try:
            _type = LAND
            _channel = DEFAULT_CHANNEL

            # AS3_ex.g:51:6: ( '&&' )
            # AS3_ex.g:51:8: '&&'
            pass 
            self.match("&&")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LAND"



    # $ANTLR start "LOR"
    def mLOR(self, ):

        try:
            _type = LOR
            _channel = DEFAULT_CHANNEL

            # AS3_ex.g:52:5: ( '||' )
            # AS3_ex.g:52:7: '||'
            pass 
            self.match("||")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LOR"



    # $ANTLR start "QUE"
    def mQUE(self, ):

        try:
            _type = QUE
            _channel = DEFAULT_CHANNEL

            # AS3_ex.g:53:5: ( '?' )
            # AS3_ex.g:53:7: '?'
            pass 
            self.match(63)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "QUE"



    # $ANTLR start "COLON"
    def mCOLON(self, ):

        try:
            _type = COLON
            _channel = DEFAULT_CHANNEL

            # AS3_ex.g:54:7: ( ':' )
            # AS3_ex.g:54:9: ':'
            pass 
            self.match(58)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "COLON"



    # $ANTLR start "ASSIGN"
    def mASSIGN(self, ):

        try:
            _type = ASSIGN
            _channel = DEFAULT_CHANNEL

            # AS3_ex.g:55:8: ( '=' )
            # AS3_ex.g:55:10: '='
            pass 
            self.match(61)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ASSIGN"



    # $ANTLR start "DIV_ASSIGN"
    def mDIV_ASSIGN(self, ):

        try:
            _type = DIV_ASSIGN
            _channel = DEFAULT_CHANNEL

            # AS3_ex.g:56:12: ( '/=' )
            # AS3_ex.g:56:14: '/='
            pass 
            self.match("/=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DIV_ASSIGN"



    # $ANTLR start "MOD_ASSIGN"
    def mMOD_ASSIGN(self, ):

        try:
            _type = MOD_ASSIGN
            _channel = DEFAULT_CHANNEL

            # AS3_ex.g:57:12: ( '%=' )
            # AS3_ex.g:57:14: '%='
            pass 
            self.match("%=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "MOD_ASSIGN"



    # $ANTLR start "ADD_ASSIGN"
    def mADD_ASSIGN(self, ):

        try:
            _type = ADD_ASSIGN
            _channel = DEFAULT_CHANNEL

            # AS3_ex.g:58:12: ( '+=' )
            # AS3_ex.g:58:14: '+='
            pass 
            self.match("+=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ADD_ASSIGN"



    # $ANTLR start "SUB_ASSIGN"
    def mSUB_ASSIGN(self, ):

        try:
            _type = SUB_ASSIGN
            _channel = DEFAULT_CHANNEL

            # AS3_ex.g:59:12: ( '-=' )
            # AS3_ex.g:59:14: '-='
            pass 
            self.match("-=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SUB_ASSIGN"



    # $ANTLR start "SHL_ASSIGN"
    def mSHL_ASSIGN(self, ):

        try:
            _type = SHL_ASSIGN
            _channel = DEFAULT_CHANNEL

            # AS3_ex.g:60:12: ( '<<=' )
            # AS3_ex.g:60:14: '<<='
            pass 
            self.match("<<=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SHL_ASSIGN"



    # $ANTLR start "JING"
    def mJING(self, ):

        try:
            _type = JING
            _channel = DEFAULT_CHANNEL

            # AS3_ex.g:61:6: ( '#' )
            # AS3_ex.g:61:8: '#'
            pass 
            self.match(35)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "JING"



    # $ANTLR start "ZHI"
    def mZHI(self, ):

        try:
            _type = ZHI
            _channel = DEFAULT_CHANNEL

            # AS3_ex.g:62:5: ( '->' )
            # AS3_ex.g:62:7: '->'
            pass 
            self.match("->")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ZHI"



    # $ANTLR start "UNDERSCORE"
    def mUNDERSCORE(self, ):

        try:
            # AS3_ex.g:93:22: ( '_' )
            # AS3_ex.g:93:24: '_'
            pass 
            self.match(95)




        finally:

            pass

    # $ANTLR end "UNDERSCORE"



    # $ANTLR start "DOLLAR"
    def mDOLLAR(self, ):

        try:
            # AS3_ex.g:95:22: ( '$' )
            # AS3_ex.g:95:24: '$'
            pass 
            self.match(36)




        finally:

            pass

    # $ANTLR end "DOLLAR"



    # $ANTLR start "ALPHABET"
    def mALPHABET(self, ):

        try:
            # AS3_ex.g:97:30: ( 'a' .. 'z' | 'A' .. 'Z' )
            # AS3_ex.g:
            pass 
            if (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                if self._state.backtracking > 0:
                    raise BacktrackingFailed

                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "ALPHABET"



    # $ANTLR start "NUMBER"
    def mNUMBER(self, ):

        try:
            # AS3_ex.g:99:30: ( '0' .. '9' )
            # AS3_ex.g:99:35: '0' .. '9'
            pass 
            self.matchRange(48, 57)




        finally:

            pass

    # $ANTLR end "NUMBER"



    # $ANTLR start "HEX_DIGIT"
    def mHEX_DIGIT(self, ):

        try:
            # AS3_ex.g:101:30: ( ( '0' .. '9' | 'a' .. 'f' | 'A' .. 'F' ) )
            # AS3_ex.g:101:35: ( '0' .. '9' | 'a' .. 'f' | 'A' .. 'F' )
            pass 
            if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 70) or (97 <= self.input.LA(1) <= 102):
                self.input.consume()
            else:
                if self._state.backtracking > 0:
                    raise BacktrackingFailed

                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "HEX_DIGIT"



    # $ANTLR start "CR"
    def mCR(self, ):

        try:
            # AS3_ex.g:103:30: ( '\\r' )
            # AS3_ex.g:103:35: '\\r'
            pass 
            self.match(13)




        finally:

            pass

    # $ANTLR end "CR"



    # $ANTLR start "LF"
    def mLF(self, ):

        try:
            # AS3_ex.g:105:30: ( '\\n' )
            # AS3_ex.g:105:35: '\\n'
            pass 
            self.match(10)




        finally:

            pass

    # $ANTLR end "LF"



    # $ANTLR start "UNICODE_ESCAPE"
    def mUNICODE_ESCAPE(self, ):

        try:
            # AS3_ex.g:107:30: ( '\\\\' 'u' HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT )
            # AS3_ex.g:107:35: '\\\\' 'u' HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT
            pass 
            self.match(92)
            self.match(117)
            self.mHEX_DIGIT()
            self.mHEX_DIGIT()
            self.mHEX_DIGIT()
            self.mHEX_DIGIT()




        finally:

            pass

    # $ANTLR end "UNICODE_ESCAPE"



    # $ANTLR start "ESCAPE_SEQUENCE"
    def mESCAPE_SEQUENCE(self, ):

        try:
            # AS3_ex.g:109:30: ( '\\\\' ( 'b' | 't' | 'n' | 'f' | 'r' | '\\\"' | '\\'' | '\\\\' ) | UNICODE_ESCAPE )
            alt1 = 2
            LA1_0 = self.input.LA(1)

            if (LA1_0 == 92) :
                LA1_1 = self.input.LA(2)

                if (LA1_1 == 34 or LA1_1 == 39 or LA1_1 == 92 or LA1_1 == 98 or LA1_1 == 102 or LA1_1 == 110 or LA1_1 == 114 or LA1_1 == 116) :
                    alt1 = 1
                elif (LA1_1 == 117) :
                    alt1 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 1, 1, self.input)

                    raise nvae

            else:
                if self._state.backtracking > 0:
                    raise BacktrackingFailed

                nvae = NoViableAltException("", 1, 0, self.input)

                raise nvae

            if alt1 == 1:
                # AS3_ex.g:109:34: '\\\\' ( 'b' | 't' | 'n' | 'f' | 'r' | '\\\"' | '\\'' | '\\\\' )
                pass 
                self.match(92)
                if self.input.LA(1) == 34 or self.input.LA(1) == 39 or self.input.LA(1) == 92 or self.input.LA(1) == 98 or self.input.LA(1) == 102 or self.input.LA(1) == 110 or self.input.LA(1) == 114 or self.input.LA(1) == 116:
                    self.input.consume()
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse



            elif alt1 == 2:
                # AS3_ex.g:110:38: UNICODE_ESCAPE
                pass 
                self.mUNICODE_ESCAPE()



        finally:

            pass

    # $ANTLR end "ESCAPE_SEQUENCE"



    # $ANTLR start "EOL"
    def mEOL(self, ):

        try:
            _type = EOL
            _channel = DEFAULT_CHANNEL

            # AS3_ex.g:113:5: ( ( CR LF | CR | LF ) )
            # AS3_ex.g:114:5: ( CR LF | CR | LF )
            pass 
            # AS3_ex.g:114:5: ( CR LF | CR | LF )
            alt2 = 3
            LA2_0 = self.input.LA(1)

            if (LA2_0 == 13) :
                LA2_1 = self.input.LA(2)

                if (LA2_1 == 10) :
                    alt2 = 1
                else:
                    alt2 = 2
            elif (LA2_0 == 10) :
                alt2 = 3
            else:
                if self._state.backtracking > 0:
                    raise BacktrackingFailed

                nvae = NoViableAltException("", 2, 0, self.input)

                raise nvae

            if alt2 == 1:
                # AS3_ex.g:114:6: CR LF
                pass 
                self.mCR()
                self.mLF()


            elif alt2 == 2:
                # AS3_ex.g:114:14: CR
                pass 
                self.mCR()


            elif alt2 == 3:
                # AS3_ex.g:114:19: LF
                pass 
                self.mLF()






            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "EOL"



    # $ANTLR start "WHITESPACE"
    def mWHITESPACE(self, ):

        try:
            _type = WHITESPACE
            _channel = DEFAULT_CHANNEL

            # AS3_ex.g:119:5: ( ( ( '\\u0020' | '\\u0009' | '\\u000B' | '\\u000C' ) | ( '\\u001C' .. '\\u001F' ) )+ )
            # AS3_ex.g:120:5: ( ( '\\u0020' | '\\u0009' | '\\u000B' | '\\u000C' ) | ( '\\u001C' .. '\\u001F' ) )+
            pass 
            # AS3_ex.g:120:5: ( ( '\\u0020' | '\\u0009' | '\\u000B' | '\\u000C' ) | ( '\\u001C' .. '\\u001F' ) )+
            cnt3 = 0
            while True: #loop3
                alt3 = 3
                LA3_0 = self.input.LA(1)

                if (LA3_0 == 9 or (11 <= LA3_0 <= 12) or LA3_0 == 32) :
                    alt3 = 1
                elif ((28 <= LA3_0 <= 31)) :
                    alt3 = 2


                if alt3 == 1:
                    # AS3_ex.g:121:5: ( '\\u0020' | '\\u0009' | '\\u000B' | '\\u000C' )
                    pass 
                    if self.input.LA(1) == 9 or (11 <= self.input.LA(1) <= 12) or self.input.LA(1) == 32:
                        self.input.consume()
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                elif alt3 == 2:
                    # AS3_ex.g:122:6: ( '\\u001C' .. '\\u001F' )
                    pass 
                    # AS3_ex.g:122:6: ( '\\u001C' .. '\\u001F' )
                    # AS3_ex.g:122:7: '\\u001C' .. '\\u001F'
                    pass 
                    self.matchRange(28, 31)





                else:
                    if cnt3 >= 1:
                        break #loop3

                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    eee = EarlyExitException(3, self.input)
                    raise eee

                cnt3 += 1



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "WHITESPACE"



    # $ANTLR start "COMMENT_MULTILINE"
    def mCOMMENT_MULTILINE(self, ):

        try:
            _type = COMMENT_MULTILINE
            _channel = DEFAULT_CHANNEL

            # AS3_ex.g:127:5: ( '/*' ( options {greedy=False; } : . )* '*/' )
            # AS3_ex.g:128:5: '/*' ( options {greedy=False; } : . )* '*/'
            pass 
            self.match("/*")
            # AS3_ex.g:129:5: ( options {greedy=False; } : . )*
            while True: #loop4
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == 42) :
                    LA4_1 = self.input.LA(2)

                    if (LA4_1 == 47) :
                        LA4_3 = self.input.LA(3)

                        if ((0 <= LA4_3 <= 65535)) :
                            alt4 = 1


                    elif ((0 <= LA4_1 <= 46) or (48 <= LA4_1 <= 65535)) :
                        alt4 = 1


                elif ((0 <= LA4_0 <= 41) or (43 <= LA4_0 <= 65535)) :
                    alt4 = 1


                if alt4 == 1:
                    # AS3_ex.g:132:13: .
                    pass 
                    self.matchAny()


                else:
                    break #loop4
            self.match("*/")
            if self._state.backtracking == 0:
                          
                _channel = AS3_exParser.CHANNEL_MLCOMMENT; 
                        




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "COMMENT_MULTILINE"



    # $ANTLR start "COMMENT_SINGLELINE"
    def mCOMMENT_SINGLELINE(self, ):

        try:
            _type = COMMENT_SINGLELINE
            _channel = DEFAULT_CHANNEL

            # AS3_ex.g:141:5: ( '//' (~ ( CR | LF ) )* ( CR LF | CR | LF ) )
            # AS3_ex.g:142:5: '//' (~ ( CR | LF ) )* ( CR LF | CR | LF )
            pass 
            self.match("//")
            # AS3_ex.g:142:10: (~ ( CR | LF ) )*
            while True: #loop5
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if ((0 <= LA5_0 <= 9) or (11 <= LA5_0 <= 12) or (14 <= LA5_0 <= 65535)) :
                    alt5 = 1


                if alt5 == 1:
                    # AS3_ex.g:142:10: ~ ( CR | LF )
                    pass 
                    if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop5
            # AS3_ex.g:142:24: ( CR LF | CR | LF )
            alt6 = 3
            LA6_0 = self.input.LA(1)

            if (LA6_0 == 13) :
                LA6_1 = self.input.LA(2)

                if (LA6_1 == 10) :
                    alt6 = 1
                else:
                    alt6 = 2
            elif (LA6_0 == 10) :
                alt6 = 3
            else:
                if self._state.backtracking > 0:
                    raise BacktrackingFailed

                nvae = NoViableAltException("", 6, 0, self.input)

                raise nvae

            if alt6 == 1:
                # AS3_ex.g:142:25: CR LF
                pass 
                self.mCR()
                self.mLF()


            elif alt6 == 2:
                # AS3_ex.g:142:33: CR
                pass 
                self.mCR()


            elif alt6 == 3:
                # AS3_ex.g:142:38: LF
                pass 
                self.mLF()



            if self._state.backtracking == 0:
                      
                _channel = AS3_exParser.CHANNEL_SLCOMMENT; 
                    




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "COMMENT_SINGLELINE"



    # $ANTLR start "SINGLE_QUOTE_LITERAL"
    def mSINGLE_QUOTE_LITERAL(self, ):

        try:
            _type = SINGLE_QUOTE_LITERAL
            _channel = DEFAULT_CHANNEL

            # AS3_ex.g:151:5: ( '\\'' ( ESCAPE_SEQUENCE | ~ ( '\\\\' | '\\'' ) )* '\\'' )
            # AS3_ex.g:151:9: '\\'' ( ESCAPE_SEQUENCE | ~ ( '\\\\' | '\\'' ) )* '\\''
            pass 
            self.match(39)
            # AS3_ex.g:151:14: ( ESCAPE_SEQUENCE | ~ ( '\\\\' | '\\'' ) )*
            while True: #loop7
                alt7 = 3
                LA7_0 = self.input.LA(1)

                if (LA7_0 == 92) :
                    alt7 = 1
                elif ((0 <= LA7_0 <= 38) or (40 <= LA7_0 <= 91) or (93 <= LA7_0 <= 65535)) :
                    alt7 = 2


                if alt7 == 1:
                    # AS3_ex.g:151:16: ESCAPE_SEQUENCE
                    pass 
                    self.mESCAPE_SEQUENCE()


                elif alt7 == 2:
                    # AS3_ex.g:151:34: ~ ( '\\\\' | '\\'' )
                    pass 
                    if (0 <= self.input.LA(1) <= 38) or (40 <= self.input.LA(1) <= 91) or (93 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop7
            self.match(39)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SINGLE_QUOTE_LITERAL"



    # $ANTLR start "DOUBLE_QUOTE_LITERAL"
    def mDOUBLE_QUOTE_LITERAL(self, ):

        try:
            _type = DOUBLE_QUOTE_LITERAL
            _channel = DEFAULT_CHANNEL

            # AS3_ex.g:154:5: ( '\"' ( ESCAPE_SEQUENCE | ~ ( '\\\\' | '\"' ) )* '\"' )
            # AS3_ex.g:154:9: '\"' ( ESCAPE_SEQUENCE | ~ ( '\\\\' | '\"' ) )* '\"'
            pass 
            self.match(34)
            # AS3_ex.g:154:14: ( ESCAPE_SEQUENCE | ~ ( '\\\\' | '\"' ) )*
            while True: #loop8
                alt8 = 3
                LA8_0 = self.input.LA(1)

                if (LA8_0 == 92) :
                    alt8 = 1
                elif ((0 <= LA8_0 <= 33) or (35 <= LA8_0 <= 91) or (93 <= LA8_0 <= 65535)) :
                    alt8 = 2


                if alt8 == 1:
                    # AS3_ex.g:154:16: ESCAPE_SEQUENCE
                    pass 
                    self.mESCAPE_SEQUENCE()


                elif alt8 == 2:
                    # AS3_ex.g:154:34: ~ ( '\\\\' | '\"' )
                    pass 
                    if (0 <= self.input.LA(1) <= 33) or (35 <= self.input.LA(1) <= 91) or (93 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop8
            self.match(34)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DOUBLE_QUOTE_LITERAL"



    # $ANTLR start "REGULAR_EXPR_BODY"
    def mREGULAR_EXPR_BODY(self, ):

        try:
            # AS3_ex.g:159:5: ( REGULAR_EXPR_FIRST_CHAR ( REGULAR_EXPR_CHAR )* )
            # AS3_ex.g:160:5: REGULAR_EXPR_FIRST_CHAR ( REGULAR_EXPR_CHAR )*
            pass 
            self.mREGULAR_EXPR_FIRST_CHAR()
            # AS3_ex.g:160:29: ( REGULAR_EXPR_CHAR )*
            while True: #loop9
                alt9 = 2
                LA9_0 = self.input.LA(1)

                if ((0 <= LA9_0 <= 9) or (11 <= LA9_0 <= 12) or (14 <= LA9_0 <= 46) or (48 <= LA9_0 <= 65535)) :
                    alt9 = 1


                if alt9 == 1:
                    # AS3_ex.g:160:29: REGULAR_EXPR_CHAR
                    pass 
                    self.mREGULAR_EXPR_CHAR()


                else:
                    break #loop9




        finally:

            pass

    # $ANTLR end "REGULAR_EXPR_BODY"



    # $ANTLR start "REGULAR_EXPR_FIRST_CHAR"
    def mREGULAR_EXPR_FIRST_CHAR(self, ):

        try:
            # AS3_ex.g:164:5: (~ ( CR | LF | '*' | '\\\\' | '/' | '>' ) | BACKSLASH_SEQUENCE )
            alt10 = 2
            LA10_0 = self.input.LA(1)

            if ((0 <= LA10_0 <= 9) or (11 <= LA10_0 <= 12) or (14 <= LA10_0 <= 41) or (43 <= LA10_0 <= 46) or (48 <= LA10_0 <= 61) or (63 <= LA10_0 <= 91) or (93 <= LA10_0 <= 65535)) :
                alt10 = 1
            elif (LA10_0 == 92) :
                alt10 = 2
            else:
                if self._state.backtracking > 0:
                    raise BacktrackingFailed

                nvae = NoViableAltException("", 10, 0, self.input)

                raise nvae

            if alt10 == 1:
                # AS3_ex.g:165:5: ~ ( CR | LF | '*' | '\\\\' | '/' | '>' )
                pass 
                if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 41) or (43 <= self.input.LA(1) <= 46) or (48 <= self.input.LA(1) <= 61) or (63 <= self.input.LA(1) <= 91) or (93 <= self.input.LA(1) <= 65535):
                    self.input.consume()
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse



            elif alt10 == 2:
                # AS3_ex.g:166:9: BACKSLASH_SEQUENCE
                pass 
                self.mBACKSLASH_SEQUENCE()



        finally:

            pass

    # $ANTLR end "REGULAR_EXPR_FIRST_CHAR"



    # $ANTLR start "REGULAR_EXPR_CHAR"
    def mREGULAR_EXPR_CHAR(self, ):

        try:
            # AS3_ex.g:170:5: (~ ( CR | LF | '\\\\' | '/' ) | BACKSLASH_SEQUENCE )
            alt11 = 2
            LA11_0 = self.input.LA(1)

            if ((0 <= LA11_0 <= 9) or (11 <= LA11_0 <= 12) or (14 <= LA11_0 <= 46) or (48 <= LA11_0 <= 91) or (93 <= LA11_0 <= 65535)) :
                alt11 = 1
            elif (LA11_0 == 92) :
                alt11 = 2
            else:
                if self._state.backtracking > 0:
                    raise BacktrackingFailed

                nvae = NoViableAltException("", 11, 0, self.input)

                raise nvae

            if alt11 == 1:
                # AS3_ex.g:170:9: ~ ( CR | LF | '\\\\' | '/' )
                pass 
                if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 46) or (48 <= self.input.LA(1) <= 91) or (93 <= self.input.LA(1) <= 65535):
                    self.input.consume()
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse



            elif alt11 == 2:
                # AS3_ex.g:171:9: BACKSLASH_SEQUENCE
                pass 
                self.mBACKSLASH_SEQUENCE()



        finally:

            pass

    # $ANTLR end "REGULAR_EXPR_CHAR"



    # $ANTLR start "BACKSLASH_SEQUENCE"
    def mBACKSLASH_SEQUENCE(self, ):

        try:
            # AS3_ex.g:174:28: ( '\\\\' ~ ( CR | LF ) )
            # AS3_ex.g:175:5: '\\\\' ~ ( CR | LF )
            pass 
            self.match(92)
            if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 65535):
                self.input.consume()
            else:
                if self._state.backtracking > 0:
                    raise BacktrackingFailed

                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "BACKSLASH_SEQUENCE"



    # $ANTLR start "REGULAR_EXPR_FLAG"
    def mREGULAR_EXPR_FLAG(self, ):

        try:
            # AS3_ex.g:178:28: ( IDENT_PART )
            # AS3_ex.g:179:5: IDENT_PART
            pass 
            self.mIDENT_PART()




        finally:

            pass

    # $ANTLR end "REGULAR_EXPR_FLAG"



    # $ANTLR start "HEX_NUMBER_LITERAL"
    def mHEX_NUMBER_LITERAL(self, ):

        try:
            _type = HEX_NUMBER_LITERAL
            _channel = DEFAULT_CHANNEL

            # AS3_ex.g:184:5: ( '0' ( 'X' | 'x' ) ( HEX_DIGIT )+ )
            # AS3_ex.g:184:7: '0' ( 'X' | 'x' ) ( HEX_DIGIT )+
            pass 
            self.match(48)
            if self.input.LA(1) == 88 or self.input.LA(1) == 120:
                self.input.consume()
            else:
                if self._state.backtracking > 0:
                    raise BacktrackingFailed

                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            # AS3_ex.g:186:5: ( HEX_DIGIT )+
            cnt12 = 0
            while True: #loop12
                alt12 = 2
                LA12_0 = self.input.LA(1)

                if ((48 <= LA12_0 <= 57) or (65 <= LA12_0 <= 70) or (97 <= LA12_0 <= 102)) :
                    alt12 = 1


                if alt12 == 1:
                    # AS3_ex.g:186:5: HEX_DIGIT
                    pass 
                    self.mHEX_DIGIT()


                else:
                    if cnt12 >= 1:
                        break #loop12

                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    eee = EarlyExitException(12, self.input)
                    raise eee

                cnt12 += 1



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "HEX_NUMBER_LITERAL"



    # $ANTLR start "DEC_NUMBER"
    def mDEC_NUMBER(self, ):

        try:
            # AS3_ex.g:189:30: ( ( NUMBER )+ '.' ( NUMBER )* | '.' ( NUMBER )+ | ( NUMBER )+ )
            alt17 = 3
            alt17 = self.dfa17.predict(self.input)
            if alt17 == 1:
                # AS3_ex.g:190:5: ( NUMBER )+ '.' ( NUMBER )*
                pass 
                # AS3_ex.g:190:5: ( NUMBER )+
                cnt13 = 0
                while True: #loop13
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if ((48 <= LA13_0 <= 57)) :
                        alt13 = 1


                    if alt13 == 1:
                        # AS3_ex.g:190:5: NUMBER
                        pass 
                        self.mNUMBER()


                    else:
                        if cnt13 >= 1:
                            break #loop13

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        eee = EarlyExitException(13, self.input)
                        raise eee

                    cnt13 += 1
                self.match(46)
                # AS3_ex.g:190:17: ( NUMBER )*
                while True: #loop14
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if ((48 <= LA14_0 <= 57)) :
                        alt14 = 1


                    if alt14 == 1:
                        # AS3_ex.g:190:17: NUMBER
                        pass 
                        self.mNUMBER()


                    else:
                        break #loop14


            elif alt17 == 2:
                # AS3_ex.g:191:7: '.' ( NUMBER )+
                pass 
                self.match(46)
                # AS3_ex.g:191:11: ( NUMBER )+
                cnt15 = 0
                while True: #loop15
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if ((48 <= LA15_0 <= 57)) :
                        alt15 = 1


                    if alt15 == 1:
                        # AS3_ex.g:191:11: NUMBER
                        pass 
                        self.mNUMBER()


                    else:
                        if cnt15 >= 1:
                            break #loop15

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        eee = EarlyExitException(15, self.input)
                        raise eee

                    cnt15 += 1


            elif alt17 == 3:
                # AS3_ex.g:192:7: ( NUMBER )+
                pass 
                # AS3_ex.g:192:7: ( NUMBER )+
                cnt16 = 0
                while True: #loop16
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if ((48 <= LA16_0 <= 57)) :
                        alt16 = 1


                    if alt16 == 1:
                        # AS3_ex.g:192:7: NUMBER
                        pass 
                        self.mNUMBER()


                    else:
                        if cnt16 >= 1:
                            break #loop16

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        eee = EarlyExitException(16, self.input)
                        raise eee

                    cnt16 += 1



        finally:

            pass

    # $ANTLR end "DEC_NUMBER"



    # $ANTLR start "DEC_NUMBER_LITERAL"
    def mDEC_NUMBER_LITERAL(self, ):

        try:
            _type = DEC_NUMBER_LITERAL
            _channel = DEFAULT_CHANNEL

            # AS3_ex.g:196:5: ( DEC_NUMBER ( EXPONENT )? )
            # AS3_ex.g:196:8: DEC_NUMBER ( EXPONENT )?
            pass 
            self.mDEC_NUMBER()
            # AS3_ex.g:196:19: ( EXPONENT )?
            alt18 = 2
            LA18_0 = self.input.LA(1)

            if (LA18_0 == 69 or LA18_0 == 101) :
                alt18 = 1
            if alt18 == 1:
                # AS3_ex.g:196:19: EXPONENT
                pass 
                self.mEXPONENT()






            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DEC_NUMBER_LITERAL"



    # $ANTLR start "EXPONENT"
    def mEXPONENT(self, ):

        try:
            # AS3_ex.g:199:30: ( ( 'e' | 'E' ) ( '+' | '-' )? ( NUMBER )+ )
            # AS3_ex.g:200:5: ( 'e' | 'E' ) ( '+' | '-' )? ( NUMBER )+
            pass 
            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                if self._state.backtracking > 0:
                    raise BacktrackingFailed

                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            # AS3_ex.g:201:5: ( '+' | '-' )?
            alt19 = 2
            LA19_0 = self.input.LA(1)

            if (LA19_0 == 43 or LA19_0 == 45) :
                alt19 = 1
            if alt19 == 1:
                # AS3_ex.g:
                pass 
                if self.input.LA(1) == 43 or self.input.LA(1) == 45:
                    self.input.consume()
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse




            # AS3_ex.g:202:5: ( NUMBER )+
            cnt20 = 0
            while True: #loop20
                alt20 = 2
                LA20_0 = self.input.LA(1)

                if ((48 <= LA20_0 <= 57)) :
                    alt20 = 1


                if alt20 == 1:
                    # AS3_ex.g:202:5: NUMBER
                    pass 
                    self.mNUMBER()


                else:
                    if cnt20 >= 1:
                        break #loop20

                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    eee = EarlyExitException(20, self.input)
                    raise eee

                cnt20 += 1




        finally:

            pass

    # $ANTLR end "EXPONENT"



    # $ANTLR start "IDENTIFIER"
    def mIDENTIFIER(self, ):

        try:
            _type = IDENTIFIER
            _channel = DEFAULT_CHANNEL

            # AS3_ex.g:207:5: ( IDENT_NAME_ASCII_START | ( UNICODE_ESCAPE )+ )
            alt22 = 2
            LA22_0 = self.input.LA(1)

            if (LA22_0 == 36 or (65 <= LA22_0 <= 90) or LA22_0 == 95 or (97 <= LA22_0 <= 122)) :
                alt22 = 1
            elif (LA22_0 == 92) :
                alt22 = 2
            else:
                if self._state.backtracking > 0:
                    raise BacktrackingFailed

                nvae = NoViableAltException("", 22, 0, self.input)

                raise nvae

            if alt22 == 1:
                # AS3_ex.g:208:5: IDENT_NAME_ASCII_START
                pass 
                self.mIDENT_NAME_ASCII_START()


            elif alt22 == 2:
                # AS3_ex.g:210:5: ( UNICODE_ESCAPE )+
                pass 
                # AS3_ex.g:210:5: ( UNICODE_ESCAPE )+
                cnt21 = 0
                while True: #loop21
                    alt21 = 2
                    LA21_0 = self.input.LA(1)

                    if (LA21_0 == 92) :
                        alt21 = 1


                    if alt21 == 1:
                        # AS3_ex.g:210:6: UNICODE_ESCAPE
                        pass 
                        self.mUNICODE_ESCAPE()


                    else:
                        if cnt21 >= 1:
                            break #loop21

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        eee = EarlyExitException(21, self.input)
                        raise eee

                    cnt21 += 1


            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "IDENTIFIER"



    # $ANTLR start "IDENT_NAME_ASCII_START"
    def mIDENT_NAME_ASCII_START(self, ):

        try:
            # AS3_ex.g:215:5: ( IDENT_ASCII_START ( IDENT_PART )* )
            # AS3_ex.g:216:5: IDENT_ASCII_START ( IDENT_PART )*
            pass 
            self.mIDENT_ASCII_START()
            # AS3_ex.g:217:5: ( IDENT_PART )*
            while True: #loop23
                alt23 = 2
                LA23_0 = self.input.LA(1)

                if (LA23_0 == 36 or (48 <= LA23_0 <= 57) or (65 <= LA23_0 <= 90) or LA23_0 == 95 or (97 <= LA23_0 <= 122)) :
                    alt23 = 1


                if alt23 == 1:
                    # AS3_ex.g:217:5: IDENT_PART
                    pass 
                    self.mIDENT_PART()


                else:
                    break #loop23




        finally:

            pass

    # $ANTLR end "IDENT_NAME_ASCII_START"



    # $ANTLR start "IDENT_ASCII_START"
    def mIDENT_ASCII_START(self, ):

        try:
            # AS3_ex.g:221:5: ( ALPHABET | DOLLAR | UNDERSCORE )
            # AS3_ex.g:
            pass 
            if self.input.LA(1) == 36 or (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                if self._state.backtracking > 0:
                    raise BacktrackingFailed

                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "IDENT_ASCII_START"



    # $ANTLR start "IDENT_PART"
    def mIDENT_PART(self, ):

        try:
            # AS3_ex.g:228:5: ( ( IDENT_ASCII_START )=> IDENT_ASCII_START | NUMBER )
            alt24 = 2
            LA24_0 = self.input.LA(1)

            if (LA24_0 == 36 or (65 <= LA24_0 <= 90) or LA24_0 == 95 or (97 <= LA24_0 <= 122)) and (self.synpred1_AS3_ex()):
                alt24 = 1
            elif ((48 <= LA24_0 <= 57)) :
                alt24 = 2
            else:
                if self._state.backtracking > 0:
                    raise BacktrackingFailed

                nvae = NoViableAltException("", 24, 0, self.input)

                raise nvae

            if alt24 == 1:
                # AS3_ex.g:229:5: ( IDENT_ASCII_START )=> IDENT_ASCII_START
                pass 
                self.mIDENT_ASCII_START()


            elif alt24 == 2:
                # AS3_ex.g:233:5: NUMBER
                pass 
                self.mNUMBER()



        finally:

            pass

    # $ANTLR end "IDENT_PART"



    def mTokens(self):
        # AS3_ex.g:1:8: ( SEMI | LCURLY | RCURLY | LPAREN | RPAREN | LBRACK | RBRACK | DOT | COMMA | LT | GT | LTE | EQ | NEQ | SAME | NSAME | PLUS | SUB | STAR | DIV | MOD | INC | DEC | SHL | AND | OR | XOR | NOT | INV | LAND | LOR | QUE | COLON | ASSIGN | DIV_ASSIGN | MOD_ASSIGN | ADD_ASSIGN | SUB_ASSIGN | SHL_ASSIGN | JING | ZHI | EOL | WHITESPACE | COMMENT_MULTILINE | COMMENT_SINGLELINE | SINGLE_QUOTE_LITERAL | DOUBLE_QUOTE_LITERAL | HEX_NUMBER_LITERAL | DEC_NUMBER_LITERAL | IDENTIFIER )
        alt25 = 50
        alt25 = self.dfa25.predict(self.input)
        if alt25 == 1:
            # AS3_ex.g:1:10: SEMI
            pass 
            self.mSEMI()


        elif alt25 == 2:
            # AS3_ex.g:1:15: LCURLY
            pass 
            self.mLCURLY()


        elif alt25 == 3:
            # AS3_ex.g:1:22: RCURLY
            pass 
            self.mRCURLY()


        elif alt25 == 4:
            # AS3_ex.g:1:29: LPAREN
            pass 
            self.mLPAREN()


        elif alt25 == 5:
            # AS3_ex.g:1:36: RPAREN
            pass 
            self.mRPAREN()


        elif alt25 == 6:
            # AS3_ex.g:1:43: LBRACK
            pass 
            self.mLBRACK()


        elif alt25 == 7:
            # AS3_ex.g:1:50: RBRACK
            pass 
            self.mRBRACK()


        elif alt25 == 8:
            # AS3_ex.g:1:57: DOT
            pass 
            self.mDOT()


        elif alt25 == 9:
            # AS3_ex.g:1:61: COMMA
            pass 
            self.mCOMMA()


        elif alt25 == 10:
            # AS3_ex.g:1:67: LT
            pass 
            self.mLT()


        elif alt25 == 11:
            # AS3_ex.g:1:70: GT
            pass 
            self.mGT()


        elif alt25 == 12:
            # AS3_ex.g:1:73: LTE
            pass 
            self.mLTE()


        elif alt25 == 13:
            # AS3_ex.g:1:77: EQ
            pass 
            self.mEQ()


        elif alt25 == 14:
            # AS3_ex.g:1:80: NEQ
            pass 
            self.mNEQ()


        elif alt25 == 15:
            # AS3_ex.g:1:84: SAME
            pass 
            self.mSAME()


        elif alt25 == 16:
            # AS3_ex.g:1:89: NSAME
            pass 
            self.mNSAME()


        elif alt25 == 17:
            # AS3_ex.g:1:95: PLUS
            pass 
            self.mPLUS()


        elif alt25 == 18:
            # AS3_ex.g:1:100: SUB
            pass 
            self.mSUB()


        elif alt25 == 19:
            # AS3_ex.g:1:104: STAR
            pass 
            self.mSTAR()


        elif alt25 == 20:
            # AS3_ex.g:1:109: DIV
            pass 
            self.mDIV()


        elif alt25 == 21:
            # AS3_ex.g:1:113: MOD
            pass 
            self.mMOD()


        elif alt25 == 22:
            # AS3_ex.g:1:117: INC
            pass 
            self.mINC()


        elif alt25 == 23:
            # AS3_ex.g:1:121: DEC
            pass 
            self.mDEC()


        elif alt25 == 24:
            # AS3_ex.g:1:125: SHL
            pass 
            self.mSHL()


        elif alt25 == 25:
            # AS3_ex.g:1:129: AND
            pass 
            self.mAND()


        elif alt25 == 26:
            # AS3_ex.g:1:133: OR
            pass 
            self.mOR()


        elif alt25 == 27:
            # AS3_ex.g:1:136: XOR
            pass 
            self.mXOR()


        elif alt25 == 28:
            # AS3_ex.g:1:140: NOT
            pass 
            self.mNOT()


        elif alt25 == 29:
            # AS3_ex.g:1:144: INV
            pass 
            self.mINV()


        elif alt25 == 30:
            # AS3_ex.g:1:148: LAND
            pass 
            self.mLAND()


        elif alt25 == 31:
            # AS3_ex.g:1:153: LOR
            pass 
            self.mLOR()


        elif alt25 == 32:
            # AS3_ex.g:1:157: QUE
            pass 
            self.mQUE()


        elif alt25 == 33:
            # AS3_ex.g:1:161: COLON
            pass 
            self.mCOLON()


        elif alt25 == 34:
            # AS3_ex.g:1:167: ASSIGN
            pass 
            self.mASSIGN()


        elif alt25 == 35:
            # AS3_ex.g:1:174: DIV_ASSIGN
            pass 
            self.mDIV_ASSIGN()


        elif alt25 == 36:
            # AS3_ex.g:1:185: MOD_ASSIGN
            pass 
            self.mMOD_ASSIGN()


        elif alt25 == 37:
            # AS3_ex.g:1:196: ADD_ASSIGN
            pass 
            self.mADD_ASSIGN()


        elif alt25 == 38:
            # AS3_ex.g:1:207: SUB_ASSIGN
            pass 
            self.mSUB_ASSIGN()


        elif alt25 == 39:
            # AS3_ex.g:1:218: SHL_ASSIGN
            pass 
            self.mSHL_ASSIGN()


        elif alt25 == 40:
            # AS3_ex.g:1:229: JING
            pass 
            self.mJING()


        elif alt25 == 41:
            # AS3_ex.g:1:234: ZHI
            pass 
            self.mZHI()


        elif alt25 == 42:
            # AS3_ex.g:1:238: EOL
            pass 
            self.mEOL()


        elif alt25 == 43:
            # AS3_ex.g:1:242: WHITESPACE
            pass 
            self.mWHITESPACE()


        elif alt25 == 44:
            # AS3_ex.g:1:253: COMMENT_MULTILINE
            pass 
            self.mCOMMENT_MULTILINE()


        elif alt25 == 45:
            # AS3_ex.g:1:271: COMMENT_SINGLELINE
            pass 
            self.mCOMMENT_SINGLELINE()


        elif alt25 == 46:
            # AS3_ex.g:1:290: SINGLE_QUOTE_LITERAL
            pass 
            self.mSINGLE_QUOTE_LITERAL()


        elif alt25 == 47:
            # AS3_ex.g:1:311: DOUBLE_QUOTE_LITERAL
            pass 
            self.mDOUBLE_QUOTE_LITERAL()


        elif alt25 == 48:
            # AS3_ex.g:1:332: HEX_NUMBER_LITERAL
            pass 
            self.mHEX_NUMBER_LITERAL()


        elif alt25 == 49:
            # AS3_ex.g:1:351: DEC_NUMBER_LITERAL
            pass 
            self.mDEC_NUMBER_LITERAL()


        elif alt25 == 50:
            # AS3_ex.g:1:370: IDENTIFIER
            pass 
            self.mIDENTIFIER()






    # $ANTLR start "synpred1_AS3_ex"
    def synpred1_AS3_ex_fragment(self, ):
        # AS3_ex.g:229:5: ( IDENT_ASCII_START )
        # AS3_ex.g:230:5: IDENT_ASCII_START
        pass 
        self.mIDENT_ASCII_START()


    # $ANTLR end "synpred1_AS3_ex"



    def synpred1_AS3_ex(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred1_AS3_ex_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success



    # lookup tables for DFA #17

    DFA17_eot = DFA.unpack(
        u"\1\uffff\1\3\3\uffff"
        )

    DFA17_eof = DFA.unpack(
        u"\5\uffff"
        )

    DFA17_min = DFA.unpack(
        u"\2\56\3\uffff"
        )

    DFA17_max = DFA.unpack(
        u"\2\71\3\uffff"
        )

    DFA17_accept = DFA.unpack(
        u"\2\uffff\1\2\1\3\1\1"
        )

    DFA17_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA17_transition = [
        DFA.unpack(u"\1\2\1\uffff\12\1"),
        DFA.unpack(u"\1\4\1\uffff\12\1"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #17

    class DFA17(DFA):
        pass


    # lookup tables for DFA #25

    DFA25_eot = DFA.unpack(
        u"\10\uffff\1\41\1\uffff\1\44\1\uffff\1\46\1\50\1\53\1\57\1\uffff"
        u"\1\63\1\65\1\67\1\71\11\uffff\1\37\4\uffff\1\74\1\uffff\1\76\1"
        u"\uffff\1\100\31\uffff"
        )

    DFA25_eof = DFA.unpack(
        u"\101\uffff"
        )

    DFA25_min = DFA.unpack(
        u"\1\11\7\uffff\1\60\1\uffff\1\74\1\uffff\2\75\1\53\1\55\1\uffff"
        u"\1\52\1\75\1\46\1\174\11\uffff\1\130\4\uffff\1\75\1\uffff\1\75"
        u"\1\uffff\1\75\31\uffff"
        )

    DFA25_max = DFA.unpack(
        u"\1\176\7\uffff\1\71\1\uffff\1\75\1\uffff\3\75\1\76\1\uffff\2\75"
        u"\1\46\1\174\11\uffff\1\170\4\uffff\1\75\1\uffff\1\75\1\uffff\1"
        u"\75\31\uffff"
        )

    DFA25_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\1\3\1\4\1\5\1\6\1\7\1\uffff\1\11\1\uffff\1\13"
        u"\4\uffff\1\23\4\uffff\1\33\1\35\1\40\1\41\1\50\1\52\1\53\1\56\1"
        u"\57\1\uffff\1\61\1\62\1\10\1\14\1\uffff\1\12\1\uffff\1\42\1\uffff"
        u"\1\34\1\26\1\45\1\21\1\27\1\46\1\51\1\22\1\43\1\54\1\55\1\24\1"
        u"\44\1\25\1\36\1\31\1\37\1\32\1\60\1\47\1\30\1\17\1\15\1\20\1\16"
        )

    DFA25_special = DFA.unpack(
        u"\101\uffff"
        )

            
    DFA25_transition = [
        DFA.unpack(u"\1\33\1\32\2\33\1\32\16\uffff\5\33\1\15\1\35\1\31\1"
        u"\40\1\22\1\23\1\34\1\4\1\5\1\20\1\16\1\11\1\17\1\10\1\21\1\36\11"
        u"\37\1\30\1\1\1\12\1\14\1\13\1\27\1\uffff\32\40\1\6\1\40\1\7\1\25"
        u"\1\40\1\uffff\32\40\1\2\1\24\1\3\1\26"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\37"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\43\1\42"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\45"),
        DFA.unpack(u"\1\47"),
        DFA.unpack(u"\1\51\21\uffff\1\52"),
        DFA.unpack(u"\1\54\17\uffff\1\55\1\56"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\61\4\uffff\1\62\15\uffff\1\60"),
        DFA.unpack(u"\1\64"),
        DFA.unpack(u"\1\66"),
        DFA.unpack(u"\1\70"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\72\37\uffff\1\72"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\73"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\75"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\77"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #25

    class DFA25(DFA):
        pass


 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(AS3_exLexer)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
