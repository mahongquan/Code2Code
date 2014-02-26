grammar AS3_ex;
options
{
    backtrack=true;
    memoize=true;
    output=AST;
    language=Python;
}

tokens{
    SEMI        = ';' ;
    LCURLY      = '{' ;
    RCURLY      = '}' ;
    LPAREN      = '(' ;
    RPAREN      = ')' ;
    LBRACK      = '[' ;
    RBRACK      = ']' ;
    DOT         = '.' ;
    COMMA       = ',' ;
    LT          = '<' ;
    GT          = '>' ;
    LTE         = '<=' ;
    GTE; 
    EQ          = '==' ;
    NEQ         = '!=' ;
    SAME        = '===' ;
    NSAME       = '!==' ;
    PLUS        = '+' ;
    SUB         = '-' ;
    STAR        = '*' ;
    DIV         = '/' ; 
    MOD         = '%' ;
    INC         = '++' ;
    DEC         = '--' ;
    SHL         = '<<' ;
    SHR;
    SHU;
    AND         = '&' ;
    OR          = '|' ;
    XOR         = '^' ;
    NOT         = '!' ;
    INV         = '~' ;
    LAND        = '&&' ;
    LOR         = '||' ;
    QUE         = '?' ;
    COLON       = ':' ;
    ASSIGN      = '=' ;
    UNDERSCORE  = '_';
    DOLLAR      = '$';
    DIV_ASSIGN  = '/=' ;
    MOD_ASSIGN  = '%=' ;
    ADD_ASSIGN  = '+=' ;
    SUB_ASSIGN  = '-=' ;
    SHL_ASSIGN  = '<<=';
    JING='#';
    ZHI  = '->';
}
@lexer::header
{
    import AS3_exParser
    AS3_exParser.CHANNEL_SLCOMMENT=43;
    AS3_exParser.CHANNEL_MLCOMMENT=42;
    AS3_exParser.CHANNEL_WHITESPACE=41;
    AS3_exParser.CHANNEL_EOL=40;
}
@lexer::members
{
def converT(self,t):
    if t=="Number":
        return "float"
    else:
        return t
}
@parser::header
{
    madict={}
    madict["Number"]="float"
    madict["Array"]= "CCArray * "
    madict["MovieClip"]="CCSprite * "
    madict["Boolean"]="bool"
    madict["Point"]="CCPoint"
}
@parser::members
{
def converT(self,t):
    global madict
    r=madict.get(t)
    if r!=None:
        return r
    else:
        return t
}
fragment UNDERSCORE  : '_';

fragment DOLLAR      : '$';

fragment ALPHABET            :    'a'..'z'|'A'..'Z';

fragment NUMBER              :    '0' .. '9';   

fragment HEX_DIGIT           :    ('0' .. '9'|'a'..'f'|'A'..'F') ;

fragment CR                  :    '\r';

fragment LF                  :    '\n';

fragment UNICODE_ESCAPE      :    '\\' 'u' HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT;

fragment ESCAPE_SEQUENCE     :   '\\' ('b'|'t'|'n'|'f'|'r'|'\"'|'\''|'\\')
                                 |   UNICODE_ESCAPE
                                 ;
EOL  
    :    
    (CR LF | CR | LF)        

    ;

WHITESPACE
    :   
    (
    ('\u0020'|'\u0009'|'\u000B'|'\u000C')
    |('\u001C'..'\u001F')
    )+              
    ;
    
COMMENT_MULTILINE           
    :   
    '/*' 
    ( options 
        {
            greedy=False;
        } : . 
    )* 
    '*/'         
        { 
        $channel = AS3_exParser.CHANNEL_MLCOMMENT; 
        }
    ;

COMMENT_SINGLELINE
    :   
    '//' ~( CR | LF )* (CR LF | CR | LF)                          
    { 
        $channel = AS3_exParser.CHANNEL_SLCOMMENT; 
    }
    ;



SINGLE_QUOTE_LITERAL
    :   '\'' ( ESCAPE_SEQUENCE | ~('\\'|'\'') )* '\''
    ;
DOUBLE_QUOTE_LITERAL         
    :   '"'  ( ESCAPE_SEQUENCE | ~('\\'|'"') )* '"'
    ;


fragment REGULAR_EXPR_BODY
    :   
    REGULAR_EXPR_FIRST_CHAR REGULAR_EXPR_CHAR*
    ;   

fragment REGULAR_EXPR_FIRST_CHAR
    :   
    ~(CR | LF |'*'|'\\'|'/'|'>')
    |   BACKSLASH_SEQUENCE
    ;

fragment REGULAR_EXPR_CHAR
    :   ~(CR | LF |'\\'|'/')
    |   BACKSLASH_SEQUENCE
    ;

fragment BACKSLASH_SEQUENCE:    
    '\\' ~(CR | LF)
    ;    
    
fragment REGULAR_EXPR_FLAG :    
    IDENT_PART 
    ;


HEX_NUMBER_LITERAL           
    : '0' 
    ('X'|'x') 
    HEX_DIGIT+ 
    ;

fragment DEC_NUMBER          :  
    NUMBER+ '.' NUMBER* 
    | '.' NUMBER+ 
    | NUMBER+ 
    ;

DEC_NUMBER_LITERAL
    :  DEC_NUMBER EXPONENT? 
    ;

fragment EXPONENT            : 
    ('e'|'E') 
    ('+'|'-')? 
    NUMBER+ 
    ;


IDENTIFIER
    :   
    IDENT_NAME_ASCII_START
    |
    (UNICODE_ESCAPE
    )+
    ;
       
fragment IDENT_NAME_ASCII_START   
    : 
    IDENT_ASCII_START 
    IDENT_PART*
    ;

fragment IDENT_ASCII_START        
    : 
    ALPHABET 
    | DOLLAR 
    | UNDERSCORE
    ;
    
fragment     IDENT_PART 
    :   
    (
    IDENT_ASCII_START
    ) => IDENT_ASCII_START
    |   
    NUMBER
    ;

numericLiteral 
    :   
    D=DEC_NUMBER_LITERAL 
        {
            pass#self.pass#Emit($D);
        } 
    | H=HEX_NUMBER_LITERAL 
        {
            pass#self.pass#Emit($H);
        }
    ;

stringLiteral          
    :   
    S=SINGLE_QUOTE_LITERAL
    {
        pass#self.pass#Emit($S);
    } 
    | D=DOUBLE_QUOTE_LITERAL 
    {
        pass#self.pass#Emit($D);
    }
    ;


identifierLiteral      returns [value]    
    :    
    I=IDENTIFIER
        {
            $value=self.converT($I.text);
        } 
 ; 


literal   returns [value]             
    :   
     numericLiteral 
        {
            $value=$numericLiteral.text
        }
    | stringLiteral 
        {
            $value=$stringLiteral.text
        }
    ;

fileContents returns [value]
@init{
    $value=unicode("")
}
    : 
    (
        stringLiteral
        {
            $value+=$stringLiteral.text
        }
 
        |numericLiteral
        {
            $value+=$numericLiteral.text
        }
        |identifierLiteral
        {
            $value+=$identifierLiteral.text
        }
        |EOL
        {
            $value+=$EOL.text
        }
        |
        xx=(
            LCURLY
            |RCURLY
            |WHITESPACE
            |DOT|STAR
            |SEMI
            |COLON
            |ASSIGN
            |JING
            |COMMA
            |LPAREN
            |RPAREN
            |ZHI
            |DIV
            |NOT
            |EQ
            |INV
        )
        {
            $value+=$xx.text
        }
    )*
    EOF
    ;