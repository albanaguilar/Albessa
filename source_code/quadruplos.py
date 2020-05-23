import sys
from nombreTipo import nombreTipo
from stack import Stack
from cuboSemantico import CuboS

#variables globales
# avail es un contador para los cuadruplos
global avail 
avail = 0
#variable que va a guardar las t
global tvar 
tvar = 'T'

class Quadruplo:

	# quadruplo es una lista porque almacenar las instrucciones que 
	# se ejecutan en cada linea del archivo
	def __init__(self):
		self.quadruplo = []
		self.contador = 0

	# añade cuadruplos a un objeto
	def addQ(self, left, right, op, result):
		q = { op, right, left, result}
		self.quad.append(q)
		self.contador += 1
	


	def add_logic(self, goto, result, place, other):
		q = { goto, result, place, other }
		self.quad.append(q)

 #    def getQ(self):
 #        l = self.quad[-1]
 #        return l
        
 #    def fill_Quad(self, index):
 #        temp = self.quad[index]
 #        temp[3]= len(self.quad)
 #        self.quad[index] = tuple(temp)
 #        print ("cuadruplo", self.quad[index])



# se generan los cuadruplos
class Operaciones:
    def __init__(self):
        self.cuboSemantico = CuboS()
        
    def getTipo(self, opIzq, opDer, operator):
    	return self.compat[opIzq][opDer][operator]

    def operations(self, operators: Stack, opNombreTipo: Stack, quadruplo: Quadruplo):
        operador = operators.pop()
        operandoDerecho = opNombreTipo.pop()
        operandoIzquierdo = opNombreTipo.pop()
        # verifica que los tipos concuerden accediendo al atributo de los operandos
        
        res_type = self.getTipo(operandoIzquierdo.tipo, operandoDerecho.tipo, operador)
        
        if (res_type != 'ERROR'):
        	avail += 1
        	ntvar = tvar + str(avail)
        	result = ntvar
        	quadruplo.addQ(operandoDerecho.id,operandoIzquierdo,operador.id, result)
        	opNombreTipo.push(result)
        else:
            print("type mismatch")
            SystemExit()

    def operations_min(self, operators: Stack, opNombreTipo: Stack, quadruplo: Quadruplo):
        operator = operators.pop()
        operand = opNombreTipo.pop()
        quadruplo.addQ(None, None, operator, operand)
        opNombreTipo.push(operand)
        

    def logic(self, operadores: Stack, opNombreTipo: Stack, saltos: Stack, quadruplo: Quadruplo, goto):
        tipx = operadores.pop().tipo
        if tipx =='bool':
            result = opNombreTipo.pop()
            quadruplo.add_logic(goto, result, None, -1)
            saltos.push(len(quadruplo)-1)
            print("tipo cuad " , result.id)
        else:
            print("type mismatch")
            SystemExit()



print("hi welcome to test")

s = Stack()
z = Stack()

uno = 1
dos = 2
cubo = CuboS()
a = nombreTipo('float', uno)
b = nombreTipo('float', dos)


s.push(a)
s.push(b)
z.push('+')

print('HOLAAAAAAAA', s.pop().type, s.pop().type, z.pop())

o = Operaciones()
q = Quadruplo()


