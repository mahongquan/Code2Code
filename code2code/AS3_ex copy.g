grammar AS3_ex;
options
{
    backtrack=true;
    memoize=true;
    output=AST;
    language=Python;
}

tokens{
    AS          =   'as';
    BREAK       =   'break';
    CASE        =   'case';
    CATCH       =   'catch';
    CLASS       =   'class';
    CONST       =   'const';
    CONTINUE    =   'continue';
    DEFAULT     =   'default';
    DELETE      =   'delete';
    DO          =   'do';
    ELSE        =   'else';
    EXTENDS     =   'extends';
    FALSE       =   'false';
    FINALLY     =   'finally';
    FOR         =   'for';
    FUNCTION    =   'function';
    IF          =   'if';
    IMPLEMENTS  =   'implements';
    IMPORT      =   'import';
    IN          =   'in';
    INSTANCEOF  =   'instanceof';
    INTERFACE   =   'interface';
    INTERNAL    =   'internal';
    IS          =   'is';
    NATIVE      =   'native';
    NEW         =   'new';
    NULL        =   'null';
    PACKAGE     =   'package';  
    PRIVATE     =   'private';
    PROTECTED   =   'protected';
    PUBLIC      =   'public';
    RETURN      =   'return';
    SUPER       =   'super';
    SWITCH      =   'switch';
    THIS        =   'this';
    THROW       =   'throw';
    TO          =   'to';
    TRUE        =   'true';
    TRY         =   'try';
    TYPEOF      =   'typeof';
    USE         =   'use';
    VAR         =   'var';
    VOID        =   'void';
    WHILE       =   'while';
    WITH        =   'with';
    
    EACH        =   'each';
    GET         =   'get';
    SET         =   'set';
    NAMESPACE   =   'namespace';
    INCLUDE     =   'include';
    DYNAMIC     =   'dynamic';
    FINAL       =   'final';
    OVERRIDE    =   'override';
    STATIC      =   'static';
    
    
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
    SHR_ASSIGN;
    SHU_ASSIGN;
    LAND_ASSIGN = '&&=';
    LOR_ASSIGN  = '||=';
    AND_ASSIGN  = '&=' ;
    XOR_ASSIGN  = '^=' ;
    OR_ASSIGN   = '|=' ;
    ELLIPSIS    = '...';
    XML_ELLIPSIS='..';
    XML_TEND    = '/>';
    XML_E_TEND  = '</';
    XML_NS_OP   = '::';
    XML_AT      = '@';
    XML_LS_STD  = '<>';
    XML_LS_END  = '</>';
    JING='#';
}
@lexer::header
{
    import AS3_exParser
    AS3_exParser.CHANNEL_SLCOMMENT=43;
    AS3_exParser.CHANNEL_MLCOMMENT=42;
    AS3_exParser.CHANNEL_WHITESPACE=41;
    AS3_exParser.CHANNEL_EOL=40;
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
    { 
        $channel = AS3_exParser.EOL; 
    }
    ;

WHITESPACE
    :   
    (
    ('\u0020'|'\u0009'|'\u000B'|'\u000C')
    |('\u001C'..'\u001F')
    )+              
        { 
            $channel = AS3_exParser.WHITESPACE; 
        }
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

booleanLiteral
@init{
    pass#print $booleanLiteral.text
}
    :
    T=TRUE 
        {
            pass#self.pass#Emit($T);
            #print $booleanLiteral.text
        } 
    | F=FALSE
        {
            pass#self.pass#Emit($F);
            #print $booleanLiteral.text
        } 
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
    | notQuiteReservedWord
        {
            $value=$notQuiteReservedWord.text
        }
 ; 


literal   returns [value]             
    :   
    N=NULL 
        {
            $value="NULL";
        } 
    | booleanLiteral 
        {
            $value=$booleanLiteral.text
        }
    | numericLiteral 
        {
            $value=$numericLiteral.text
        }
    | stringLiteral 
        {
            $value=$stringLiteral.text
        }
    ;

semic
        @init
        {
            pass
        }
    :
    S=SEMI
    |   E=EOF
    |   R=RCURLY
    ;
notQuiteReservedWord
    : 
    word=(
        TO | NATIVE | EACH | GET | SET | NAMESPACE | DYNAMIC | FINAL | OVERRIDE | STATIC 
    ) 
        {
            pass
        }
    ;