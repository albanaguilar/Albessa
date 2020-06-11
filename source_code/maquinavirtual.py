# import sys
# from stack import Stack
# from memoria import *


# class MaquinaVirtual:
# 	def __init__(self):
# 		#contador para ver en que linea vamos de codigo o en ciclos a cuadruplos
# 		self.iteratorPointer = 0
# 		# pila para guardar los cuadruplos
# 		self.quads = Stack()
# 		#objeto de la clase memoria para usar sus funciones
# 		#self.memoria = memoria.Memoria()


import sys
from memoria import Memoria
from stack import Stack

class MaquinaVirtual():
    def __init__(self):
    	# pila para guardar los cuadruplos
        self.quads = Stack()

        self.memoria = Memoria()










