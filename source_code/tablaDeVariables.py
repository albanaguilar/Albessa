import sys

# table of variables, symbols
class tablaVar:
    def __init__(self): #whith self we can access the atributes of the class
        self.listaVariables = { }
        

    # function to add var to var table
    def agregar(self, type, id, direccion): 
        self. listaVariables[id] = {
            'type': type,
            'direccion': direccion
        }


    def buscarVar(self, id):
        return id in self.listaVariables.keys()
    

    def getTipoVar(self, id):
        return self.listaVariables[id]["type"]


    def printVar(self): #para vr si esta guardada la variable en la tabla
        print(self.listaVariables.items())
        # for i in self.listaVariables:
        #     print( i, 'se encuentra en la tabla de variables')


#test

#vari = tablaVar()
#vari.agregar("int", "a")
#vari.agregar("float", "b")
#vari.agregar("char", "c")
#vari.agregar("float", "b")
#print(vari.buscarVar("b"))
#vari.printVar()






