import sys
import ply.lex as lex
import ply.yacc as yacc
from tablaDeFunciones import tablaFunc
from tablaDeVariables import tablaVar
from nombreTipo import nombreTipo
from cuboSemantico import CuboS
from stack import Stack

# Objetos
tablaFunc = tablaFunc()
tablaVar = tablaVar()

#pilaOperadores = Stack()
nombresVariables_y_tipoDatos = Stack()


#Variables globales
variableActualTipo = ''
variableActualID = ''

funcionActualTipo = ''
funcionActualID = ''
listaOperadores = []
lista_NombresVariables_y_tipoDatos = []

#reserved words from the language
reserved = {
    'funcion' : 'FUNCION',
    'var': 'VAR',
    'program': 'PROGRAM',
    'main' :'MAIN',
    'void' : 'VOID',
    'int' : 'INT',
    'float': 'FLOAT',
    'char' : 'CHAR',
    'if' : 'IF',
    'then' : 'THEN',
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
    'ID', 'CTEI', 'CTEF', 'CTEC', 'CTESTRING', 'EQUALS', 
    'PLUS', 'MINUS', 'MUL', 'DIV', 'LT', 'GT', 'LTE', 'GTE', 
    'AND', 'OR', 'LPAREN', 'RPAREN', 'COMMA','COMILLA', 
    'SEMICOLON', 'NE', 'LBRACKET', 'RBRACKET', 'LCURLY', 'RCURLY', 'EE'
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
t_EE = r'\=='
t_ignore = ' \t\n'


#id tokens
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

#int tokens
def t_CTEI(t):
    r'0|[-+]?[1-9][0-9]*'
    t.value = int(t.value)
    return t

#char tokens
def t_CTEC(t):
    r"\'[^']\'"
    t.value = t.value[1]
    return t

#float tokens
def t_CTEF(t):
    r'[-+]?\d*\.\d+'
    t.value = float(t.value)
    return t

#tokens de strings
def t_CTESTRING(t):
    r'\'[\w\d\s\,. ]*\'|\"[\w\d\s\,. ]*\"'
    return t

#if errors are detected it prints error message
def t_error(t):
    print("ERROR at '%s'" % t.value)
    t.lexer.skip(1) 

lexer = lex.lex()

lexer.input("ab3 = 'a'")

# parser
#reglas en minuscula
# palabrs resevadas en mayuscula

#estructura basica del programa
def p_prog(p):
    '''
    prog : PROGRAM ID inicializarProg SEMICOLON prog_1 END 
    '''
    p[0] = 'PROGRAMA COMPILADO'

#considera -1 al ID, inicializarProg es el indice 0
def p_inicializarProg(p):
    '''
    inicializarProg : 
    '''

    #PUNTOS NEURALGICOS: puntos que van a hacer una funcion, dentro del parser
    global funcionActualID, funcionActualTipo
    #print(p[-2])
    funcionActualID = p[-1]
    funcionActualTipo = 'programa'

    tablaFunc.agregarFuncion(funcionActualTipo, funcionActualID, 0, '', '', 0)
    tablaFunc.printFun(funcionActualID)

# aux del prog para evitar ambiguedades
def p_prog_1(p):
    '''
    prog_1 : var methods main_1
    '''

#main del programa
def p_main_1(p):
    '''
    main_1 : MAIN agregarMain LPAREN RPAREN LCURLY estatutos RCURLY
    '''

def p_agregarMain(p):
    '''
    agregarMain : 
    '''
    global funcionActualID, funcionActualTipo
    funcionActualID = p[-1]
    funcionActualTipo = 'main'

    #type, fid, numberParams, paramType, paramsID, numberVars
    tablaFunc.agregarFuncion(funcionActualTipo, funcionActualID, 0, '', '', 0)
    tablaFunc.printFun(funcionActualID)

def p_estatutos(p):
    '''
    estatutos : asignacion SEMICOLON estatutos
        | llamadaFun estatutos
        | lectura estatutos
        | escritura estatutos
        | for estatutos
        | while estatutos
        | if estatutos
        | empty
    '''

def p_for(p):
    '''
    for : FOR asignacion TO CTEI LCURLY estatutos RCURLY
    '''

def p_while(p):
    '''
    while : WHILE LPAREN expresion RPAREN LCURLY estatutos RCURLY
    '''

def p_if(p):
    '''
    if : IF LPAREN expresion RPAREN THEN LCURLY estatutos RCURLY else
    '''

def p_else(p):
    '''
    else : ELSE LCURLY estatutos RCURLY
        | empty
    '''

def p_return(p):
    '''
    return : RETURN expresion SEMICOLON
    '''


#Regla para guardar en una pila los operadores usados
def p_guardarOp(p):
    '''
    guardarOp : 
    '''

    global operador

    operador = p[-1]
    listaOperadores.append(operador)
    print(listaOperadores[-1])


def p_expresion(p):
    '''
    expresion : expAux
        | expAux OR guardarOp expAux
    ''' 


def p_expAux(p):
    '''
    expAux : eAux
         | eAux AND guardarOp eAux
    ''' 

def p_eAux(p):
    '''
    eAux : masMen 
        | eAux2 masMen
    ''' 

def p_eAux2(p):
    '''
    eAux2 : masMen GT guardarOp masMen
        | masMen LT guardarOp masMen
        | masMen GTE guardarOp masMen
        | masMen LTE guardarOp masMen
        | masMen NE guardarOp masMen 
    ''' 

def p_masMen(p):
    '''
    masMen : mulDiv
           | mulDiv PLUS guardarOp mulDiv
           | mulDiv MINUS guardarOp mulDiv
    '''
def p_mulDiv(p):
    '''
    mulDiv : expNum
           | expNum MUL guardarOp expNum
           | expNum DIV guardarOp expNum
    '''
def p_expNum(p):
    '''
    expNum : CTEI
         | CTEF
         | CTEC
         | llamadaFun
         | ID
         | LPAREN expresion RPAREN
    '''


def p_arreglos(p):
    '''
    arreglos : type ID LBRACKET CTEI RBRACKET arrAux SEMICOLON 
    '''

def p_arrAux(p):
    '''
    arrAux : COMMA ID LBRACKET CTEI RBRACKET
        | empty
    '''


def p_escritura(p):
    '''
    escritura : PRINT LPAREN escrituraAux RPAREN SEMICOLON
    '''

def p_escrituraAux(p):
    '''
    escrituraAux : ID
        | COMILLA CTESTRING COMILLA
        | COMILLA CTESTRING COMILLA COMMA ID
    '''


def p_lectura(p):
    '''
    lectura : READ LPAREN lecturaAux RPAREN SEMICOLON
    ''' 

def p_lecturaAux(p):
    '''
    lecturaAux : ID lecturaAux2
    '''

def p_lecturaAux2(p):
    '''
    lecturaAux2 : COMMA lecturaAux
        | empty
    '''

def p_asignacion(p):
    '''
    asignacion : ID EQUALS expresion
    '''

def p_llamadaFun(p): 
    '''
    llamadaFun : ID LPAREN expresion RPAREN SEMICOLON
    ''' 


def p_var(p):
    '''
    var : VAR var1
        | empty
    '''

#aux de var para agregar variables de otros tipos
def p_var1(p):
    '''
    var1 : type ID addVariable varMulti SEMICOLON var2
        | arreglos
    '''

def p_varMulti(p):
    '''
    varMulti : COMMA ID addVariable varMulti
        | empty
    '''

#se agregan las variables, sus nombres y tipos a la tabla de funciones 
def p_addVariable(p):
    '''
    addVariable : 
    '''

    global funcionActualID, variableActualTipo,funcionActualTipo

    variableActualID = p[-1]

    tablaFunc.agregarVariable(funcionActualID , variableActualTipo, variableActualID)
    #tablaFunc.printFun(funcionActualID)
    nom_y_tipo = nombreTipo(variableActualTipo, variableActualID)
    nombresVariables_y_tipoDatos.push(nom_y_tipo)
    #print( nombresVariables_y_tipoDatos.peek().identificador )
    #print( nombresVariables_y_tipoDatos.peek().type )


# para agregar mas de un tipo de variablea; solo puede ser empty la segunda que entra
def p_var2(p):
    '''
    var2 : var1
        | empty
    '''

def p_type(p):
    '''
    type : INT returnTipo regresaTipoVar
        | FLOAT returnTipo regresaTipoVar
        | CHAR returnTipo regresaTipoVar
    '''

def p_regresaTipoVar(p):
    '''
    regresaTipoVar :
    '''

    global variableActualTipo
    variableActualTipo = p[-2]

def p_returnTipo(p):
    '''
    returnTipo : 
    '''

    global variableActualTipo, funcionActualTipo
    funcionActualTipo = p[-1]


def p_methods(p):
    '''
    methods : FUNCION VOID ID agregarFuncion LPAREN argumentos RPAREN var LCURLY estatutos RCURLY methods
        | FUNCION type ID agregarFuncion LPAREN argumentos RPAREN var LCURLY estatutos return RCURLY methods
        | empty
    '''


#puntos neuralgicos
def p_agregarFuncion(p):
    '''
    agregarFuncion : 
    '''

    global funcionActualID, funcionActualTipo
    funcionActualID = p[-1]

    if p[-2] == 'void':
        funcionActualTipo = 'void'
    

    #type, fid, numberParams, paramType, paramsID, numberVars
    tablaFunc.agregarFuncion(funcionActualTipo, funcionActualID, 0, '', '', 0)



def p_argumentos(p):
    '''
    argumentos : type ID multiArg
        | empty
    '''

def p_multiArg(p):
    '''
    multiArg : COMMA argumentos
        | empty
    '''


def p_error(p):
    print("Syntax Error in input!", p)

def p_empty(p):
    '''
    empty : 
    '''

parser = yacc.yacc()


def main():
    try:
        nombreArchivo = 'test.txt'
        arch = open(nombreArchivo, 'r')
        print("El archivo a leer es: " + nombreArchivo)
        informacion = arch.read()
        arch.close()
        lexer.input(informacion)
        while True:
            tok = lexer.token()
            if not tok:
                break
            print(tok)
        if (parser.parse(informacion, tracking = True) == 'PROGRAMA COMPILADO'):
            print ("Correct Syntax")
        else: 
            print("Syntax error")
    except EOFError:
        print(EOFError)
main()