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
def outputCpp(self):
    nm=self.mapackage+"_"+self.maclass
    f=open("output/"+nm+".cpp","w")
    f.write("#include "+nm+".h\n")
    for d in self.mastaticP:
        (d1,v)=d[0]
        f.write(d1[1]+" "+self.maclass+"::"+d1[0]+"="+v+";\n")
    for f1 in self.mafunction:
        if(len(f1[2])==0):#no para
            f.write(str(f1[1])+" "+self.maclass+"::"+str(f1[0])+"()"+"\n")
        else:
            ps=[]            
            for p1 in f1[2]:
                d=p1[0]
                ps.append(d[1]+" "+d[0])
                f.write(str(f1[1])+" "+self.maclass+"::"+str(f1[0])+"("+",".join(ps)+")"+"\n")        
        
        f.write(f1[3])
        f.write("\n")

    f.close()
    #f=open("output/"+nm+".cpp","r").read()
    #print f
def outputInclude(self):
    #print self.maproperty
    #print self.mastaticP
    #print self.mafunction
    nm=self.mapackage+"_"+self.maclass
    f=open("output/"+nm+".h","w")
    f.write("#ifndef _"+nm+"_\n#define _"+nm+"_\n")
    f.write("#include <cocos2d.h>\n")
    f.write("using namespace cocos2d;\n");
    if self.mabase=="":
        f.write("class "+self.maclass+"\n")
    else:
        f.write("class "+self.maclass+" :public "+self.mabase+"\n")
    f.write("{\npublic:\n")
    #static prop
    for d in self.mastaticP:
        #print d
        (d1,v)=d[0]
        f.write("static "+d1[1]+" "+d1[0]+";\n")
    for d in self.maproperty:
        #print d
        (d1,v)=d[0]
        f.write(d1[1]+" "+d1[0]+";\n")
    for f1 in self.mafunction:
        if(len(f1[2])==0):#no para
            if 'static' in f1[4]:
                f.write("static "+str(f1[1])+" "+str(f1[0])+"();"+"\n")
            else:
                f.write(str(f1[1])+" "+str(f1[0])+"();"+"\n")
        else:
            ps=[]            
            for p1 in f1[2]:
                d=p1[0]
                ps.append(d[1]+" "+d[0])
            if 'static' in f1[4]:
                f.write("static "+str(f1[1])+" "+str(f1[0])+"("+",".join(ps)+");"+"\n")
            else:
                f.write(str(f1[1])+" "+str(f1[0])+"("+",".join(ps)+");"+"\n")        
    f.write("};\n")
    f.write("#endif")
    f.close()
    #f=open("output/"+nm+".h","r").read()
    #print f
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

fileContents
    : 
    packageDeclaration? packageElement* 
    EOF
    ;

translation_unit:  
    packageDeclaration  
    EOF
    ;
packageDeclaration
        @init{
            self.mapackage=""
        }
    :   
    p=PACKAGE 
    (type
        {
            self.mapackage=$type.start.text
        }
    )? 
    l=LCURLY 
    packageElement* 
    r=RCURLY 
        {
            self.outputInclude()
            self.outputCpp()
        }
    ;

packageElement
    :classOrInterfaceDecl 
        {
            print "class or interfacedecl"
        }
    | propertyDeclaration 
        {
            print "propery decl"
        }
    | functionDeclaration 
        {
            print "function decl"
        }
    | interfaceFunctionDeclaration
        {
            print "interface decl"
        } 
    | statement 
        {
            print "statement"
        }
    | directive
        {
            print "directive"
        }
    ;

importDeclaration
    :   
        {
            pass#pass#InsertCR(False);
        } 
    i=IMPORT 
        {
            pass#self.pass#Emit($i);
        } 
    type 
    (
    D=DOT  {
                pass#self.pass#Emit($D);
            } 
    S=STAR {
                pass#self.pass#Emit($S);
            } 
    )? semic 
    ;

classOrInterfaceDecl
    :   
    (
    conditionalDirAndBindingDecls
    )?
    ( 
    memberModifiers
    )
    ? 
    (
    interfaceDeclaration 
    | 
    classDeclaration
    )
    ;
    
directive returns [value]
@init{
    $value=""
}
    : 
    (bindingDecl 
    | includeDirective 
    | useNamespaceDirective 
    | importDeclaration 
    )
    ;
    
conditionalDirAndBindingDecls
    : 
    conditionalCompilerOption 
    (
    bindingDecl
    )*
    ;
    
   
conditionalCompilerOption returns [value]
    :
    i1=identifierLiteral 
        {
            $value=$i1.value
        }
    x=XML_NS_OP 
        {
            $value+="::"
        } 
    i2=identifierLiteral
        {
            $value+=$i2.value
        }
    ;
    

    
bindingDecl
    : 
    L=LBRACK  
    I=IDENTIFIER 
    (
        L=LPAREN 
            (bindingDeclArg 
                (
                C=COMMA 
                bindingDeclArg
                )*
            )? 
        R=RPAREN
    )? 
    R=RBRACK
    (
        s=SEMI 
    )?
    ;
    
includeDirective
    : 
    I=INCLUDE
    stringLiteral 
    semic  
    ;
    
bindingDeclArg
    :
    (I=IDENTIFIER 
     E=ASSIGN 
    )? 
    (
        stringLiteral 
        | numericLiteral 
        | eitherIdentifier  
    );


interfaceDeclaration
    :  
    INTERFACE 
    type 
    (
        e=EXTENDS 
        typeList
    )? 
    interfaceBody
    ;    

interfaceBody
    :   
    l=LCURLY 
    interfaceElement* 
    r=RCURLY 
    ;    

classDeclaration
    :   
        {
            tbase=""
            self.mabase=""
        }
    c=CLASS 
    t1=type
        {
            v=t1.start.text
            self.maclass=v[0].upper()+v[1:]
        }
    ( 
    E=EXTENDS 
    t2=type
        {
            self.mabase=t2.start.text
        }
    )? 
    ( 
    I=IMPLEMENTS 
    typeList
    )? 
    classBody 
    ;  
    
  

classBody
        @init
        {
            self.mafunction=[]
            self.maproperty=[]
            self.mastaticP=[]
        }
    : 
    L=LCURLY 
    classBodyElement* 
    R=RCURLY
    ;


classBodyElement
    :
    propertyDeclaration
        {
            pass
        }
    | functionDeclaration
        {
            self.mafunction.append($functionDeclaration.value)
        } 
    | statement 
    | directive //| emptyStatement
    ;

interfaceElement
    :   propertyDeclaration 
    | interfaceFunctionDeclaration 
    | statement
    | directive //| emptyStatement
    ;


interfaceFunctionDeclaration
    :    
    (conditionalDirAndBindingDecls
    )? 
    memberModifiers? 
    F=FUNCTION 
    (
    S=SET
    | 
    G=GET
    )? 
    (I=IDENTIFIER 
    | notQuiteReservedWord
    ) 
    formalParameterList 
    (C=COLON 
    type
    )? 
    semic
    ;


propertyDeclaration
        @init
        {
            mamodi=[]
        }
    :    
    (conditionalDirAndBindingDecls
    )? 
    (memberModifiers
        {
            mamodi.append($memberModifiers.text)
        }
    )?
    (
    variableStatement
        {
            if ("static" in mamodi):
                self.mastaticP.append($variableStatement.value)
            else:
        
                self.maproperty.append($variableStatement.value);
        } 
    | constantVarStatement 
        {
            if ("static" in mamodi):
                self.mastaticP.append($constantVarStatement.value)
            else:

                self.maproperty.append($constantVarStatement.value);

        }
    | namespaceDirective
    ) 
    ;


functionDeclaration returns [value]
        @init
        {
            mamodi=[]
        }
    :
        {
            rettype=""
            funcname=""
        }
    (
    conditionalDirAndBindingDecls
    )? 
        {
            pass#InsertCR(False);
        } 
    (memberModifiers
        {
            mamodi=$memberModifiers.value
        }
    )? 
    F=FUNCTION 
    (
    funcType=(SET|GET) 
    )?
    (
    I=IDENTIFIER 
        {
            funcname=I.text
        } 
    | 
    notQuiteReservedWord
    ) 
    formalParameterList
    (
    C=COLON 
        {
            pass#self.InsertWS(pass#mPrinter.GetAdvancedSpacesBeforeColons());
        } 
    type
        {
            rettype=self.converT($type.start.text)
        }
    )?
    functionBody 
        {
                $value=[funcname,rettype,$formalParameterList.value,$functionBody.value,mamodi]
        }
    ;

functionExpression
    :   F=FUNCTION 
        {
            pass#self.pass#Emit($F);
        } 
    (I=IDENTIFIER
        {
            pass#self.pass#Emit($I);
        }
    )? 
    formalParameterList 
    (C=COLON 
        {
            #self.InsertWS(pass#mPrinter.GetAdvancedSpacesBeforeColons());
            pass#self.pass#Emit($C);
            #self.InsertWS(pass#mPrinter.GetAdvancedSpacesAfterColons());
        } 
    type
    )? 
        {
            pass#PopIndent();
        } 
    functionBody
        {
            pass#self.PushExpressionIndent();
        }
    ;

formalParameterList returns [value]
        @init
        {
            $value=[]
        }
    :   
    L=LPAREN 
    ( 
        ( 
            v1=variableDeclaration 
                {
                     $value.append(v1.value)
                }
            ( 
            C=COMMA
            v2=variableDeclaration 
                {
                    $value.append(v2.value)
                }
            )* 
            ( 
                C=COMMA  
                  formalEllipsisParameter
                {
                    $value.append(formalEllipsisParameter.value)
                }
            )?
        )
        | 
        formalEllipsisParameter
        {
            $value.append(formalEllipsisParameter.value)
        }
    )? 
    R=RPAREN 
        {
            #print $formalParameterList.text
            pass#print $value
        }
    ;
    
formalEllipsisParameter returns [value]
    :   
    E=ELLIPSIS  
        {
            $value="..."
        } 
    variableIdentifierDecl
        {
            $value+=$variableIdentifierDecl.value
        }
    ;   

functionBody returns [value]
@init{
    pass
    #print "in func body ==========="
}
    :   
    L=LCURLY
        {
            $value=chr(123)
        } 
    (
        statement
            {
                $value+=$statement.value+"\n"
            }
        |
        functionDeclaration
            {
                (funcname,rettype,para,fb,mamodi)=$functionDeclaration.value
                $value+=rettype+funcname+str(para)+"\n"
            }
    )* 
    R=RCURLY   
        {
            $value+=chr(125)
        }
    ;


memberModifiers returns [value]
    :   
        {$value=[]}
    (memberModifier
        {
            $value.append($memberModifier.text)
        }
    )+
    ;

    
memberModifier
    :   x=(
        DYNAMIC
    |   FINAL
    |   INTERNAL
    |   NATIVE
    |   OVERRIDE
    |   PRIVATE
    |   PROTECTED
    |   PUBLIC
    |   STATIC
    |   IDENTIFIER 
    ) 
        {
            pass#Emit($x);
        }
    ;


statement returns [value]
        @init
        {
            print "==========in statement============="
            $value=""
        }
    :blockStatement
        {
            print "block statement"
            $value=$blockStatement.value
        }
    |directive
        {
            print "directive"
            print $directive.text
            $value+=$directive.value
        }
    |namespaceDirective
        {
            $value+=$namespaceDirective.text
        }
    |expression semic
        {
            print "expression"
            print $expression.text
            $value+=$expression.value+chr(59)
            print $value
        }    
    |   constantVarStatement 
        {
            print "const var state"
            print $constantVarStatement.text
            $value+=$constantVarStatement.text
        }
    |   tryStatement
        {
            print "try st"
            print $tryStatement.text
            $value+=$tryStatement.text
        }
    |   labelledStatement
        {
            print "label st"
            print $labelledStatement.text 
            $value+=$labelledStatement.text
        }
    |   switchStatement
        {
            $value+=$switchStatement.text
        }
    |   withStatement
        {
            $value+=$withStatement.text
        }
    |    returnStatement{
            $value+=$returnStatement.value
        } 
    |breakStatement
        {
            $value+=$breakStatement.value
        } 
    |continueStatement
        {
            $value+=$continueStatement.text
        } 
    |forStatement
        {
            $value+=$forStatement.text
        } 

    |forInStatement
        {
            $value+=$forInStatement.text
        } 

    |forEachInStatement
        {
            $value+=$forEachInStatement.text
        } 

    |doWhileStatement
        {
            $value+=$doWhileStatement.text
        } 

    |whileStatement
        {
            $value+=$whileStatement.text
        } 

    |ifStatement
        {
            $value=$ifStatement.value
        }
    |emptyStatement
        {
            $value+=$emptyStatement.text
        } 

    |variableStatement
        {
            d,v=$variableStatement.value[0]
            if(d[1]!=None):
                $value=str(d[1])+" "+d[0]+"="+v+chr(59)
            else:
                $value=d[0]+"="+v+chr(59)
        } 
    |throwStatement 
        {
            $value+=$throwStatement.text
        } 
     
    ;


blockStatement returns [value]
        @init{
            $value=""
        }
    :   
    (
    c=conditionalCompilerOption
        {
            $value+=$c.text
        }
    )? 
    L=LCURLY 
        {
            $value+=chr(123)
        }
    (
    statement
        {
            $value+=$statement.value
        }
    )* 

    R=RCURLY 
        {
            $value+=chr(125)
        }
    ;


throwStatement
    :  T=THROW 
        {
            pass#pass#Emit($T);
        } 
    expression semic
    ;


constantVarStatement returns [value]
@init{
    $value=None
}
    :   C=CONST  
    variableDeclarationList 
        {
            $value=$variableDeclarationList.value
        }
    (S=SEMI
    )?                                                                              
    ; 


useNamespaceDirective
    : 
    U=USE  
    {
        pass#pass#Emit($U);
    } 
    N=NAMESPACE  
    {
        pass#pass#Emit($N);
    } 
    qualifiedIdentifier 
    (C=COMMA 
    {
        pass#pass#Emit($C);
    } 
    qualifiedIdentifier
    )* 
    semic
    ;    

namespaceDirective
    :   //(memberModifiers)? //namespace
    N=NAMESPACE  
    {
        pass#pass#Emit($N);
    }
    {
        pass#self.PushExpressionIndent();
    } 
    qualifiedIdentifier 
    ( A=ASSIGN  
        {
            pass#self.InsertWS(pass#mPrinter.GetSpacesAroundAssignment());pass#Emit($A);
    } 
    stringLiteral 
    )? 
    semic 
    {
        pass#PopIndent();
    }
    ;


tryStatement
    : 
    {
        pass#InsertStatementCR();
    } 
    T=TRY 
    {
        pass#pass#Emit($T);
    } 
    {
        pass#PushIndent(False);
    } 
    blockStatement 
    {
        pass#PopIndent();
    }
    ( catchClause+ finallyClause
    | catchClause+
    | finallyClause
    )
    ;

catchClause
    : 
    {
        pass#self.InsertWS(1);
    } 
    C=CATCH 
    {
        pass#pass#Emit($C);
        #self.InsertWS(pass#mPrinter.GetSpacesBetweenControlKeywordsAndParens());
    }
    {
        pass#PushIndent(False);
    } 
    L=LPAREN 
    {
        pass#pass#Emit($L);
        #self.InsertWS(pass#mPrinter.GetAdvancedSpacesInsideParens());
    } 
    variableIdentifierDecl 
    R=RPAREN 
    {
        #self.InsertWS(pass#mPrinter.GetAdvancedSpacesInsideParens());
        pass#pass#Emit($R);
    } 
    blockStatement 
    {
        pass#PopIndent();
    }
    ;

finallyClause
    : 
    {
        pass#if (pass#mPrinter.IsCRBeforeCatch()): 
        #    pass#InsertCR(False);
    }
    {
        pass#self.InsertWS(1);
    } 
    F=FINALLY 
    {
        pass#pass#Emit($F);
    }
    {
        pass#PushIndent(False);
    } 
    blockStatement 
    {
        pass#PopIndent();
    }
    ;


labelledStatement
    :  I=IDENTIFIER 
    {
        pass#pass#Emit($I);
    }
    {
        pass#PushLabeledIndent();
    } 
    C=COLON 
    {
        pass#pass#Emit($C);
        #self.InsertWS(pass#mPrinter.GetSpacesAfterLabel());
    } 
    statement 
    {
        pass#PopIndent();
    }
    ;


switchStatement
    :   {
            pass#InsertLines(pass#mPrinter.GetBlankLinesBeforeControlStatement());
        }
        {
            pass#InsertStatementCR();
        } 
        S=SWITCH 
        {
            pass#pass#Emit($S);self.InsertWS(pass#mPrinter.GetSpacesBetweenControlKeywordsAndParens());
        }
        {   
            pass#self.PushExpressionIndent();
        } 
        parExpression 
        {
            pass#PopIndent();
        } 
        L=LCURLY 
        {
            pass#LeftCurlyNewlineHandler(False);
            #pass#Emit($L);PushIndent(true);
        } 
        switchBlockStatementGroup* 
        {
            pass#PopIndent();
        } 
        R=RCURLY
        {
            pass#InsertCR(False);pass#Emit($R);
        } 
    ;
    
switchBlockStatementGroup
    :   {
            pass#InsertCR(False);
        } 
        switchLabel 
        {
            pass#PushIndent(False);
        } 
        statement* 
        {
            pass#PopIndent();
        }
        {
            pass#InsertCR(False);
        } 
        breakStatement?
    ;
    
switchLabel
    :   C=CASE 
        {
            pass#pass#Emit($C);
        } 
        expression 
        C=COLON 
        {
            pass#pass#Emit($C);
            #self.InsertWS(pass#mPrinter.GetSpacesAfterLabel());
        } 
    |   D=DEFAULT 
        {
            pass#pass#Emit($D);
        } 
        C=COLON
        {
            pass#pass#Emit($C);
            #self.InsertWS(pass#mPrinter.GetSpacesAfterLabel());
        } 
    ;


withStatement
    :   
    W=WITH  
    {
        pass#pass#Emit($W);
        #self.InsertWS(pass#mPrinter.GetSpacesBetweenControlKeywordsAndParens());
    }
    {
        pass#self.PushExpressionIndent();
    } 
    L=LPAREN  
    {
        pass#pass#Emit($L);self.InsertWS(pass#mPrinter.GetAdvancedSpacesInsideParens());
    } 
    expression  
    R=RPAREN  
    {
        pass#self.InsertWS(pass#mPrinter.GetAdvancedSpacesInsideParens());pass#Emit($R);
    }
    {
        pass#PopIndent();
    } 
    {
        pass#PushIndent(False);
    }
    statement 
    {
        pass#PopIndent();
    }
    ;


returnStatement returns [value]
        @init{
            $value=""
        }
    :R=RETURN
        {
            $value+="return "
        } 
    ( 
    expression
        {
            for e in $expression.value:    
                $value+=e
        }
    )? semic 
        {
            $value+=chr(59)
        }
    ;


breakStatement returns [value]
    :   B=BREAK    
        {
            $value="break ";
        } 
    (I=IDENTIFIER
        {
            $value+=$I.value
        }
    )? 
    semic
        {
            $value+=";"
        }
    ;


continueStatement
    :   
    C=CONTINUE 
        {
            pass#pass#Emit($C);
        } 
    (I=IDENTIFIER
        {
            pass#Emit($I);
        }
    )? 
    semic
    ;


forStatement
    :   
    F=FOR 
        {
            pass#pass#Emit($F);self.InsertWS(pass#mPrinter.GetSpacesBetweenControlKeywordsAndParens());
        } 
        {
            pass#self.PushExpressionIndent();
        } 
    L=LPAREN 
        {
            pass#pass#Emit($L);self.InsertWS(pass#mPrinter.GetAdvancedSpacesInsideParens());
        } 
    forControl 
    R=RPAREN 
        {
            pass#self.InsertWS(pass#mPrinter.GetAdvancedSpacesInsideParens());pass#Emit($R);
        } 
    statement 
    ;
    
forInStatement
    :   
    F=FOR 
        {
            pass#pass#Emit($F);self.InsertWS(pass#mPrinter.GetSpacesBetweenControlKeywordsAndParens());
        } 
        {
            pass#self.PushExpressionIndent();
        } 
    L=LPAREN 
        {
            pass#pass#Emit($L);self.InsertWS(pass#mPrinter.GetAdvancedSpacesInsideParens());
        } 
    forInControl 
    R=RPAREN 
        {
            pass#self.InsertWS(pass#mPrinter.GetAdvancedSpacesInsideParens());pass#Emit($R);
        }  
    statement
    ;  
    
forEachInStatement
    :   
    F=FOR 
        {
            pass#pass#Emit($F);
        } 
        {
            pass#self.PushExpressionIndent();
        }
    E=EACH 
        {
            pass#pass#Emit($E);self.InsertWS(pass#mPrinter.GetSpacesBetweenControlKeywordsAndParens());
        } 
    L=LPAREN 
        {
            pass#pass#Emit($L);self.InsertWS(pass#mPrinter.GetAdvancedSpacesInsideParens());
        } 
    forInControl 
    R=RPAREN 
        {
            pass#self.InsertWS(pass#mPrinter.GetAdvancedSpacesInsideParens());pass#Emit($R);
        }
    statement 
        {
            pass#PopIndent();
        }     
    ;
forControl
options {k=3;} // be efficient for common case: for (ID ID : ID) ...
    :   
    forInit? 
        {
            pass#self.InsertWS(pass#mPrinter.GetSpacesBeforeComma());
        } 
    semic  
        {
            pass#self.InsertWS(pass#mPrinter.GetSpacesAfterComma());
        } 
    expression? 
        {
            pass#self.InsertWS(pass#mPrinter.GetSpacesBeforeComma());
        }
    semic 
        {
            pass#self.InsertWS(pass#mPrinter.GetSpacesAfterComma());
        } 
    forUpdate?
    ;

forInControl
options 
{
    k=3;
} // be efficient for common case: for (ID ID : ID) ...
    :   
    forInDecl 
    I=IN 
        {
            pass#Emit($I);
        } 
    expression
    ;

forInDecl
    :   
    leftHandSideExpression
    |   
    V=VAR 
        {
            pass#Emit($V);
        } 
    variableDeclarationNoIn
    ;

forInit
    :   variableDeclarationNoInList
    |   expressionNoIn
    ;

forUpdate
    :   
    expression
    ;


doWhileStatement
    :   
    D=DO  
    statement 
    W=WHILE  
    parExpression 
    semic 
    (S=SEMI)? 
    ;


whileStatement
    :   W=WHILE  
    parExpression  
    statement {pass#PopIndent();}
    ;
    

ifStatement returns[value]
        @init 
        {
            $value=""
        }
    :      
    I=IF 
        {
            $value+="if"
        }
    parExpression
        {
            $value+=$parExpression.value+"\n"
        } 
    s1=statement 
        {
            $value+="\n"+$s1.value+"\n"
        }
    (
        options 
        {
            k=1;
        }:
    E=ELSE
        {
            $value+="else\n"
        } 
    s2=statement 
        {
            $value+="\n"+$s2.value+"\n"
        }
    )?
    ;
    

emptyStatement returns [value]
    :     
    S=SEMI  
        {
            $value=chr(59)
        }
    ;


variableStatement returns [value]
@init{
    $value=[]
}
    :
    (
    I=IDENTIFIER 
    )? 
    V=VAR 
    v1=variableDeclaration
        {
            $value.append($v1.value)
        }
    ( 
    C=COMMA 
    v2=variableDeclaration
        {
            $value.append($v2.value)
        }
    )* 
    semic
    ;
    
variableDeclarationList returns [value]
@init{
    $value=[]
}
    :    
     v1=variableDeclaration
         {
             $value.append($v1.value)
         } 
     ( 
     C=COMMA 
     v2=variableDeclaration
         {
             $value.append($v2.value)
         }
     )*
    ;
    
variableDeclarationNoInList
    :    
    (V=VAR
        {
        pass#Emit($V);
        } 
    )? 
    variableDeclarationNoIn 
    ( 
        {
            pass#self.InsertWS(pass#mPrinter.GetSpacesBeforeComma());
        } 
    C=COMMA 
        {
            pass#Emit($C);
        }
        {
            pass#self.InsertWS(pass#mPrinter.GetSpacesAfterComma());
        } 
    variableDeclarationNoIn
    )*
    ;
    
variableDeclaration returns [value]
@init{
    mainit=None
    $value=[]
}
    :   
    variableIdentifierDecl
        {
            $value.append($variableIdentifierDecl.value)
        } 
    ( A=ASSIGN 
        {
            pass#InsertVariableDeclAssignmentWhitespace( $A, true);
        } 
    assignmentExpression 
        {
            mainit=$assignmentExpression.value
    
        }
    )?
        {
            $value.append(mainit)
        }
    ;

variableDeclarationNoIn
    :    
    variableIdentifierDecl 
    ( A=ASSIGN 
         {
          #InsertVariableDeclAssignmentWhitespace( $A, true);
          #self.InsertWS(pass#mPrinter.getSpacesAroundAssignment());
          pass#Emit($A);
          #InsertVariableDeclAssignmentWhitespace( $A, False);
          #self.InsertWS(pass#mPrinter.getSpacesAroundAssignment());
         } 
    assignmentExpressionNoIn 
    )?
    ;
    
variableIdentifierDecl returns [value]
@init
{
    vtype=""
    id1=""
}
    :    
    identifierLiteral 
        {
            id1=$identifierLiteral.value
        }
    ( 
    C=COLON 
    type
        {
            vtype=self.converT($type.start.text)
        } 
    )?
        {
            $value=[id1,vtype]
        }
    ;

type:   
    qualifiedName 
    | S=STAR 
        {
            pass#Emit($S);
        } 
    | V=VOID 
        {
            pass#Emit($V);
        } 
    ;

typeList
    :   
    type 
    (
        {
            pass#self.InsertWS(pass#mPrinter.GetSpacesBeforeComma());
        }
    C=COMMA 
        {
            pass#self.InsertWS(pass#mPrinter.GetSpacesAfterComma());
        } 
    type
    )*
    ; 
     
standardQualifiedName returns [value]
@init{
    $value=""
}
    :
    t1=typeSpecifier 
        {
            $value+=$t1.text
        }
    (
    D=DOT 
        {
            $value+="->"
        } 
    t2=typeSpecifier 
        {
            $value+=$t2.text
        }
    )*
    ;
    
qualifiedName returns [value]

    :   
    standardQualifiedName 
        {
            $value=$standardQualifiedName.value
        }
    (
    typePostfixSyntax
        {
            $value+=$typePostfixSyntax.value
        }
    )? 
    ;
    
typePostfixSyntax returns [value]
@init{
    pass#rint "=============="
    #print "in typePostfixSyntax"
}
    :
    D=DOT 
        {
            $value="."
        } 
    L=LT 
        {
            $value+="<"
        } 
    standardQualifiedName
        {
            $value+=$standardQualifiedName.value
        } 
    (
    t1=typePostfixSyntax
        {
            $value+=$t1.value
        }
    )? 
    G=GT 
        {
            $value+=">"
        }
    ;
    
qualifiedIdentifier returns [value]
    :   
    I=IDENTIFIER 
        {
            $value=self.converT($I.text)
        } 
    ;



parExpression returns [value]
    : L=LPAREN  
    expression  
    R=RPAREN
        {
            $value=chr(40)        
            for e in $expression.value:
                $value+=e
            $value+=chr(41)
        } 
    ;

expression returns [value]
@init{
    $value=""
}
    :   
    a1=assignmentExpression 
        {
            $value+=$a1.value
        }
    ( 
    C=COMMA  
    a2=assignmentExpression
        {
            $value+=","+$a2.value
        }
    )*
    ;

expressionNoIn
    :   
    assignmentExpressionNoIn 
    ( 
        {
            pass#self.InsertWS(pass#mPrinter.GetSpacesBeforeComma());
        } 
    C=COMMA  
        {
            pass#self.InsertWS(pass#mPrinter.GetSpacesAfterComma());
        } 
    assignmentExpressionNoIn
    )*
    ;

assignmentExpression returns [value]
        @init{
            $value=""
        }
    :   
    leftHandSideExpression  assignmentOperator  a1=assignmentExpression
        {
            $value=$leftHandSideExpression.value+ $assignmentOperator.text+  $a1.value
        }
    | 
    conditionalExpression
        {
            $value=$conditionalExpression.value
        }
    ;


assignmentExpressionNoIn
    :   
    conditionalExpressionNoIn
    |   
    leftHandSideExpression  
    assignmentOperator  
    assignmentExpressionNoIn
    ;

assignmentOperator
    : 
    op=assignmentOperator_int 
        {
            pass#self.InsertWS(pass#mPrinter.GetSpacesAroundAssignment());
            pass#Emit($op.start);
            #self.InsertWS(pass#mPrinter.GetSpacesAroundAssignment());
        }
    ;
         
assignmentOperator_int
    : 
    ASSIGN 
    | 
    s=STAR 
    a=ASSIGN! 
        {
            s.Text = "*=";
        }
    | DIV_ASSIGN 
    | MOD_ASSIGN 
    | ADD_ASSIGN 
    | SUB_ASSIGN
    | SHL_ASSIGN
    |   (('>' '>' '=')=> t1='>' t2='>' t3='='
        {
            $t1.Line == $t2.Line and 
            $t1.CharPositionInLine + 1 == $t2.CharPositionInLine and 
            $t2.Line == $t3.Line and 
            $t2.CharPositionInLine + 1 == $t3.CharPositionInLine 
        }?
      -> SHR_ASSIGN) 
      {
          t1.Text = ">>=";
      }

    | (('>' '>' '>' '=')=> t1='>' t2='>' t3='>' t4='='
        { $t1.Line == $t2.Line and 
          $t1.CharPositionInLine + 1 == $t2.CharPositionInLine and
          $t2.Line == $t3.Line and 
          $t2.CharPositionInLine + 1 == $t3.CharPositionInLine and
          $t3.Line == $t4.Line and 
          $t3.CharPositionInLine + 1 == $t4.CharPositionInLine }?
      -> SHU_ASSIGN) {t1.Text = ">>>=";}
    | AND_ASSIGN 
    | XOR_ASSIGN 
    | OR_ASSIGN
    | LOR_ASSIGN
    | LAND_ASSIGN
    ;

conditionalExpression returns [value]
    :   
    logicalORExpression 
        {
            $value=    $logicalORExpression.value
        }
    ( Q=QUE  
        {    $value+=$Q.text#Indent#Emit($Q);
        } 
    a1=assignmentExpression  
        {    
            $value+=$a1.value#PopIndent();
        } 
    C=COLON  
        {
            $value+=$C.text#Indent#Emit($C);
        } 
    a2=assignmentExpression 
        {
            $value+=$a2.value#PopIndent();
        }
    )?
    ;
    
conditionalExpressionNoIn
    :   
    logicalORExpressionNoIn 
    ( Q=QUE 
        {pass#Indent#Emit($Q);} 
    assignmentExpression  
        {pass#PopIndent();} 
    C=COLON  
        {pass#Indent#Emit($C);} 
    assignmentExpression 
        {pass#PopIndent();}
    )?
    ;    
    
logicalORExpression returns [value]
    :   
    l1=logicalANDExpression
        {
            $value=$l1.value
        } 
    ( 
    L=LOR 
        {
            $value+=$L.text
        } 
    l2=logicalANDExpression 
        {
            $value+=$l2.value
        }
    )*
    ; 
    
logicalORExpressionNoIn
    :   
    logicalANDExpressionNoIn 
    ( L=LOR 
        {pass#Indent#Emit($L);} 
    logicalANDExpressionNoIn 
        {pass#PopIndent();}
    )*
    ;     
    
logicalANDExpression returns [value]
    :   
    b1=bitwiseORExpression 
        {
            $value=$b1.value
        }
    ( 
    L=LAND 
        {
            $value+=$L.text
        } 
    b2=bitwiseORExpression 
        {
            $value+=$b2.value
        }
    )*
    ;
    
logicalANDExpressionNoIn
    :   
    bitwiseORExpressionNoIn 
    ( 
    L=LAND 
        {pass#Indent#Emit($L);} 
    bitwiseORExpressionNoIn 
        {pass#PopIndent();}
    )*
    ;    
    
bitwiseORExpression returns [value]
    :   
    b1=bitwiseXORExpression 
        {
            $value=$b1.value
        }
    ( 
    O=OR 
        {
            $value+=$O.text#Indent#Emit($O);
        } 
    b2=bitwiseXORExpression 
        {
            $value+=$b2.value#PopIndent();
        }
    )*
    ;
    
bitwiseORExpressionNoIn
    :   
    bitwiseXORExpressionNoIn 
    ( 
    O=OR 
        {pass#Indent#Emit($O);} 
    bitwiseXORExpressionNoIn 
        {pass#PopIndent();}
    )*
    ;    
    
bitwiseXORExpression returns [value]
    :   
    b1=bitwiseANDExpression 
        {
            $value=$b1.value
        }
    ( 
    x=XOR 
        {
            $value+=$x.value#Indent#Emit($x);
        } 
    b2=bitwiseANDExpression 
        {
            $value+=$b2.value#PopIndent();
        }
    )*
    ;
    
bitwiseXORExpressionNoIn
    :   
    bitwiseANDExpressionNoIn 
    ( 
    x=XOR 
        {pass#Indent#Emit($x);} 
    bitwiseANDExpressionNoIn 
        {pass#PopIndent();}
    )*
    ;    

bitwiseANDExpression returns [value]
    :   
    e1=equalityExpression 
        {
            $value=$e1.value
        }
    ( 
    A=AND 
        {
            $value+=$A.text#Indent#Emit($A);
        } 
    e2=equalityExpression 
        {
            $value+=$e2.value#PopIndent();
        }
    )*
    ;
    
bitwiseANDExpressionNoIn
    :   
    equalityExpressionNoIn 
    ( 
    A=AND 
        {pass#Indent#Emit($A);} 
    equalityExpressionNoIn 
        {pass#PopIndent();}
    )*
    ;    

equalityExpression returns [value]
    :   
    e1=relationalExpression 
        {
            $value=$e1.value
        }
    ( 
    eq=(EQ|NEQ|SAME|NSAME)
        {
            $value+=$eq.text
        }  
    e2=relationalExpression 
        {$value+=$e2.value;
        }
    )*
    ;
    
equalityExpressionNoIn
    :   
    relationalExpressionNoIn 
    ( 
    eq=(EQ|NEQ|SAME|NSAME) 
        {
            pass#Indent#Emit($eq);
        } 
    relationalExpressionNoIn 
        {
            pass#PopIndent();
        }
    )*
    ;    

relationalExpression returns [value]
    :   
    s1=shiftExpression 
        {
            $value=$s1.value
        }
    (
        (     g=GT
                {
                    $value+=$g.text
                } 
            (a=ASSIGN
                {
                    $value+=$a.text
                }
            )? 
            | eq=(IN|LT|LTE|INSTANCEOF|IS|AS)
                {
                    $value+=$eq.text;
                }
        )  
        s2=shiftExpression 
            {
                $value+=$s2.value;
            }
    )*
    ;
    
relationalExpressionNoIn
    :   
    shiftExpression 
    (
        ( 
            g=GT (assign=ASSIGN)? 
                {
                    if (assign!=None):
                        g.Text = ">=";
                        g.Type = GTE;
                } 
            | 
            eq=(LT|LTE|INSTANCEOF|IS|AS) 
                {pass#Indent#Emit($eq);}
        )  
        shiftExpression {pass#PopIndent();}
    )*
    ;

shiftExpression returns [value]
    :   
    a1=additiveExpression 
        {
            $value=$a1.value
        }
    ( 
        o=(
            t1=SHL
        |    (('>' '>')=> t1='>' t2='>'
            { $t1.Line == $t2.Line and 
                  $t1.CharPositionInLine + 1 == $t2.CharPositionInLine }?
              -> SHR) {t1.Text = ">>";}
        |     (('>' '>' '>')=> t1='>' t2='>' t3='>'
            { $t1.Line == $t2.Line and 
                  $t1.CharPositionInLine + 1 == $t2.CharPositionInLine and
                  $t2.Line == $t3.Line and 
                  $t2.CharPositionInLine + 1 == $t3.CharPositionInLine }?
              -> SHU) {t1.Text = ">>>";}
        ) 
            {
                $value+=$o.text
            } 
    a2=additiveExpression 
        {
            $value+=$a2.value;
        }
    )*
    ;

additiveExpression returns [value]
    :   
    m1=multiplicativeExpression 
        {
            $value=$m1.value
        }
    ( 
    op=(PLUS|SUB)
        {
            $value+=$op.text
        }  
    m2=multiplicativeExpression 
        {
            $value+=$m2.value#PopIndent();
        }
    )*
    ;

multiplicativeExpression returns [value]
    :   
    u1=unaryExpression 
        {
            $value=$u1.value
        }
    ( 
    op=(STAR|DIV|MOD)
        {$value+=$op.text#Indent#Emit($op);
        } 
    u2=unaryExpression 
        {$value+=$u2.value#pass#PopIndent();
        }
    )*
    ;

unaryExpression returns [value]
    :   
    p1=postfixExpression
        {
            $value=$p1.value
        }
    |  
    op=(NOT | INV) 
    u1=unaryExpression
        {
            $value=$op.text+$u1.value;
        } 

    |   
    unaryOp 
    p2=postfixExpression
        {
            $value=$unaryOp.text+$p2.value
        }
    ;

unaryOp
    :   
    op=(DELETE | VOID | TYPEOF | INC | DEC | PLUS | SUB | INV | NOT) 
        {pass#Emit($op);}
    ;


postfixExpression returns [value]
@init{
    #print "postfix e"
    pass
}
    :   
    leftHandSideExpression 
        {
            $value=$leftHandSideExpression.value
        }
    (postfixOp
        {
            $value+=$postfixOp.text
        }
    )?
    {
        pass
        #print $value
    }
    ;
    
postfixOp
    :   
    op=(INC | DEC)
    ;

memberExpression returns [value]
    : 
    primaryExpression
        {
            $value=$primaryExpression.value
        }
    | functionExpression
        {
            $value=$functionExpression.text
        }
    | newExpression
        {
            $value=$newExpression.value
        }
    ;

newExpression returns [value]
    : N=NEW  
        {$value="new "} 
    primaryExpression
        {
            $value+=$primaryExpression.value
        }
    ;

leftHandSideExpression returns [value]
        @init
        {
            print "======in left hand"
            $value=""
        }
    :   
    memberExpression
        {
            $value+=$memberExpression.value
        }
    (
        arguments
            {
                $value+=$arguments.value
            }
        | 
        L=LBRACK 
        expression 
        R=RBRACK
            {
                $value+="["+$expression.value+"]"
            }
        | 
        D=DOT 
            {
                $value+="->"
            } 
        (
        e1=eitherIdentifier 
        op=XML_NS_OP 
            {
                $value+=$e1.value+"::"
            } 
        )? 
        e2=eitherIdentifier
            {
                $value+=$e2.value
            }
        | E=XML_ELLIPSIS
            {
                $value+=".."
            } 
        (
        e3=eitherIdentifier 
        op=XML_NS_OP 
            {
                $value+=$e3.value+"::"
            } 
        )? 
        e4=eitherIdentifier
            {
                $value+=$e4.value
            }
        | D=DOT 
            {
                $value+="."
            } 
        parExpression
            {
                $value+=$parExpression.value
            }
        | 
        typePostfixSyntax
            {
                $value+=$typePostfixSyntax.value
            } 
    )*   
    {
        if len($value)>3 and $value[-3:]=="->x":
            $value=$value[:-3]+"->getPositionX()"
        elif len($value)>3 and $value[-3:]=="->y":
            $value=$value[:-3]+"->getPositionY()"
        #rotation
        #
    }
    | x=XML_AT 
        {
            $value+="@"
        }
    ;
    
eitherIdentifier returns [value]
    : I=IDENTIFIER  
        {
            $value=self.converT($I.text);
        } 
     | allKeywords
        {
            $value=$allKeywords.text
        }
    ;
    
typeSpecifier:
    I=IDENTIFIER 
        {
        pass#Emit($I);
        } 
    | notQuiteReservedWord
    | I=INTERNAL 
        {pass#Emit($I);
        } 
    | D=DEFAULT {
        pass#Emit($D);
        }
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

allKeywords
    : 
    (reservedWord 
    | notQuiteReservedWord
    )
    ;
reservedWord
    :
    word=(AS          
    | BREAK           
    | CASE  
    | CATCH           
    | CLASS 
    | CONST
    | CONTINUE
    | DEFAULT
    | DELETE
    | DO
    | ELSE
    | EXTENDS
    | FALSE
    | FINALLY
    | FOR
    | FUNCTION
    | IF
    | IMPLEMENTS
    | IMPORT          
    | IN
    | INSTANCEOF      
    | INTERFACE
    | INTERNAL        
    | IS
    | NEW
    | NULL            
    | PACKAGE  
    | PRIVATE         
    | PROTECTED
    | PUBLIC          
    | RETURN
    | SUPER           
    | SWITCH
    | THIS            
    | THROW
    | TRUE
    | TRY             
    | TYPEOF
    | USE             
    | VAR
    | VOID            
    | WHILE
    | WITH 
    | INCLUDE         
       ) 
    ;
    
arguments returns [value]
    : 
    L=LPAREN 
    {
        $value="("
    }
    (    
        a1=assignmentExpression
        {
            $value+=$a1.value
        } 
        (  
            C=COMMA 
            a2=assignmentExpression 
            {
                $value+=","+$a2.value
            }
        )* 
    )? 
    R=RPAREN
    {
        $value+=")"
    }
    ;

suffix
    :    indexSuffix | propertyReferenceSuffix
    ;
indexSuffix             
    :    
    L=LBRACK  
    expression  
    R=RBRACK
    ;
    
propertyReferenceSuffix
    : D=DOT  
        {
        pass#pass#Emit($D);
        } 
    I=IDENTIFIER
        {
        pass#pass#Emit($I);
        } 
    |    D=DOT  
        {
        pass#pass#Emit($D);
        } 
    ;

primaryExpression returns [value]  
@init{
    pass
    #print "========pe==========="
    #print  $primaryExpression.text
}
    :   T=THIS
        {
            $value="this"#pass#pass#Emit($T);
        } 
    |   S=SUPER
        {
            $value="super"#pass#Emit($S);
        } 
    |   literal  
        {
            $value=$literal.value
        }
    |   arrayLiteral 
        {
            $value=$arrayLiteral.value
        }
    |   objectLiteral  
        {
            $value=$objectLiteral.value
        }
    |   identifierLiteral 
        {
            $value=$identifierLiteral.value
        }
    |   parExpression 
        {
            $value=$parExpression.value
        }
    |   conditionalCompilerOption
        {
            $value=$conditionalCompilerOption.value
        }
    |   l=LT 
        {
            $value="<"#pass#pass#Emit($l);
        } 
    type
        {
            $value+=$type.start.text
        } 
    g=GT 
        {
            $value+=">"#pass#pass#Emit($g);
        } 
    (
    arrayLiteral
        {
            $value+=$arrayLiteral.value+" "
        }
    )? 
    ;

objectLiteral returns [value]
    :   
    L=LCURLY 
        {
            $value=chr(123)
        } 
    (
    propertyNameAndValueList
        {
            $value+=$propertyNameAndValueList.value
        }
    )
    ? 
    R=RCURLY 
        {
            $value+=chr(125)
        } 
    ;

propertyNameAndValueList returns [value]
@init{
    #print "pname and vl"
}
    :   
    p1=propertyNameAndValue 
        {
            $value=$p1.value
        }
    (
    C=COMMA 
        {
            $value+=",";
        }
    p2=propertyNameAndValue
        {
            $value+=$p2.value
            #print $value
        }
    )*
    ;

propertyNameAndValue returns [value]
@init{
    #print "pname and value"
    pass
}
    :   
    propertyName
        {
            $value=$propertyName.value
        } 
    C=COLON 
        {
            $value+=":"
        }
    assignmentExpression
        {
            $value+=$assignmentExpression.text
        }
    ;

propertyName returns [value]
@init{
    pass
    #print "in propertyName"
}
    :   identifierLiteral
        {
            $value=$identifierLiteral.text
        } 
    |   stringLiteral 
        {
            $value=$stringLiteral.text
        }
    |   numericLiteral 
        {
            $value=$numericLiteral.text
        }
    ;

arrayLiteral returns [value]
    :   
    L=LBRACK 
        {
            $value="["
        }
    (elementList
        {
            $value+=$elementList.value
        }
    )
    ? 
    R=RBRACK
        {
            $value+="]"
        }
    ;

elementList returns [value]
    :
    a1=assignmentExpression 
        {
            $value=$a1.value
        }
    (
    C=COMMA 
        {
            $value+=","
        }
    a2=assignmentExpression
        {    
            $value+=$a2.value
        }
    )* 
    (
        C=COMMA 
        {
            $value+=","
        }
    )?         
    ;
