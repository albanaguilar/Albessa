import lex.lex as lex
import yacc.yacc as yacc


#reserved words from the language
reserved = {
    'funcion' : 'FUNCION',
    'var': 'VAR',
    'program': 'PROGRAM',
    'main':'MAIN',
    'void' : 'VOID',
    'int' : 'INT',
    'float': 'FLOAT',
    'char' : 'CHAR',
    'if' : 'IF',
    'else' : 'ELSE',
    'return': 'RETURN',
    'end' : 'END',
    'read': 'READ',
    'print': 'PRINT', 
    'for' : 'FOR',
    'from' : 'FROM',
    'while': 'WHILE',
    'to': 'TO'
}

#tokens are declared
tokens =[
    'ID',
    'CTEI',#int
    'CTEF', #float
    'CTEC', #char
    'EQUALS',
    'PLUS',
    'MINUS',
    'MUL',
    'DIV',
    'LT', #<
    'GT', #>
    'LTE', #<=
    'GTE', #>=
    'AND', 
    'OR', 
    'LPAREN',
    'RPAREN',
    'COMMA',
    'SEMICOLON',
    'NE', #NOT EQUAL
    'LBRACKET',
    'RBRACKET',
    'LCURLY',
    'RCURLY',
] + list(reserved.values())


#equivalents in symbols
t_SEMICOLON = r'\;'
t_COMMA = r'\,'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LCURLY = r'\{'
t_RCURLY = r'\}'
t_EQUALS = r'\='
t_PLUS = r'\+'
t_MINUS = r'\-'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMILLA = r'\"'
t_MUL = r'\*'
t_DIV = r'\/'
t_GT = r'\>'
t_LT = r'\<'
t_GTE = r'\=>'
t_LTE = r'\<='
t_NE = r'\<>' 
t_AND = r'\&&'
t_OR = r'\|'
t_ignore = ' \t\n'


#id tokens
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

#float tokens
def t_CTEF(t):
    r'[-+]?\d*\.\d+'
    t.value = float(t.value)
    return t

#int tokens
def t_CTEI(t):
    r'0|[-+]?[1-9][0-9]*'
    t.value = int(t.value)
    return t

#if errors are detected it prints error message
def t_error(t):
    print("ERROR at '%s'" % t.value)
    t.lexer.skip(1) 

lexer = lex.lex()

def p_prog(p):
    '''
	prog : vars modules aux
	prog : vars modules
	          | aux
	'''

def p_aux(p):
    '''
	aux :  main
	''' 
def p_main(p):
    '''
	main : MAIN LPAREN param RPAREN LCURLY vars statement RCURLY END
	'''

def p_tipo(p):
    '''
    tipo : INT 
         | FLOAT 
         | CHAR 
    '''    

def p_vars(p):
    '''
    vars : var 
         | empty
    '''

def p_var(p): #aux function for vars
    '''
    var : VAR var2
    '''  

def p_var1(p):
    '''
        var1 : ID
            | ID COMMA var1
            | ID arr 
            | ID arr COMMA var1
            | empty
    '''


def p_var2(p):
    # recursivity for many var types
    '''
        var2 : var2 tipo var1 SEMICOLON
             | var2 tipo arr SEMICOLON
             | var2 tipo mat SEMICOLON
             | empty
    ''' 

def p_arr(p):
    '''
    arr : LBRACKET CTEI RBRACKET
        | LBRACKET exp RBRACKET 
    
    '''  

def p_modules(p):
    '''
    modules : function modules
            | empty
    
    '''     

def p_function1(p):
    '''
    function1 : ID LPAREN param RPAREN LCURLY vars statement RCURLY
    '''

def p_function(p):
    '''
    function : FUNCION VOID function1 
             | FUNCION INT function2 
             | FUNCION CHAR function2 
             | FUNCION FLOAT function2
    '''

def p_function2(p):
    '''
    function2 : ID LPAREN param RPAREN SEMICOLON LCURLY vars statement RETURN exp SEMICOLON RCURLY   
    ''' 












