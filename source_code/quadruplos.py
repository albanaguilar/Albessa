import sys
from nombreTipo import nombreTipo
from stack import Stack
from cuboSemantico import *
from tablaDeFunciones import tablaFunc
from tablaDeVariables import tablaVar

#variables globales
# avail es un contador para los cuadruplos
avail = 0
#variable que va a guardar las t
tvar = 'T'

class Quadruplo:
    # quadruplo es una lista porque almacenar las instrucciones que 
    # se ejecutan en cada linea del archivo
    def __init__(self):
        self.quadruplo = []
        self.contador = 0

    def addQ(self, left, right, op, result):
        q = {left, right, op, result}
        self.quadruplo.append(q)
        self.contador += 1

    def getQ(self): # retorna el cuadruplo
        l = self.quadruplo[-1]
        return l
        

# se generan los cuadruplos
class Operaciones:

    # el cubo semantico te va a decir que resultado va a ser basado en los tipos de datos
    def __init__(self):
        self.type = float
        self.identificador = 0
        
    def getTipo(self, opIzq, opDer, operator):
        return getType(opIzq, opDer, operator)

    # se genera el cuadruplo
    def operations(self, operators, opNombreTipo, quadruplo):
        global avail 
        global tvar 
        global ntvar

        #operadorDeMemoria = tablaFunc.getMemoriaDeOperadores( listaOperadores.top())
        operador = operators.pop()

        operandoDerecho = opNombreTipo.pop()
        operandoIzquierdo = opNombreTipo.pop()
        # verifica que los tipos concuerden accediendo al atributo de los operandos
        

        res_type = self.getTipo(operandoIzquierdo, operandoDerecho, operador)
        
        # si da un resultado coerente segun los estatutos del cuadro semantico hace el proceso, sino error
        if(res_type != 'ERROR'):
            avail += 1
            ntvar = tvar + str(avail)
            result = ntvar
            
            #si no es error agrega el cuadruplo
            quadruplo.addQ(operandoIzquierdo, operandoDerecho ,operador , result)
            
            # tablaFunc.anadirMemoriaVarTemporales(res_type, result, functionName)
            # temp = tablaFunc.getMemoriaVarTemp(result)
            # qua = (operadorDeMemoria, operandoIzquierdo, operandoDerecho, temp)

            # quads.append(qua)
            # pilaNombres.push(temp)
            # pilaTiposDatos.push(res_type)

            #hace push con el nombre de variabel y tipo de dato al stack
            opNombreTipo.push(result)
        else:
            print("errosr")
            SystemExit()


# print("hi welcome to test")

# s = Stack()
# z = Stack()

# uno = 1
# dos = 2
# cubo = CuboS()
# a = nombreTipo('float', uno)
# b = nombreTipo('float', dos)


# s.push(a)
# s.push(b)
# z.push('+')

# print('HOLAAAAAAAA', s.pop().type, s.pop().type, z.pop())
