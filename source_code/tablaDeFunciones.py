from tablaDeVariables import tablaVar
import sys
from memoria import Memoria

# function table
class tablaFunc():
    def __init__(self): #create dictionary
        self.functions = {}
        self.memory = Memoria()

    def agregarFuncion(self, type, functionName, numberParams, paramType, vars, numberVars):
        if functionName not in self.functions.keys(): #params to save in the table
            self.functions[functionName] = {
                'type' : type, 'functionName' : functionName, 'numberParams' : numberParams,
                'paramType' : paramType, 'vars' : vars, 
                'variables' : tablaVar(), #it is done separatly, too many vars
                'numberVars' : numberVars }
            print('Funcion añadida:',functionName, ' ', type)
        #else:
            #print(id , 'ya existe')

    def buscarFun(self, id):
        return id in self.functions 

    def printFun(self, functionName):
        if id in self.functions:
            self.functions[functionName]['variables'].printVar()


    # function to add variable to table function
    # to associate certain variables to certain functions

    #si la variable existe en local no se agrega
    def agregarVariable(self, functionName, type, id):
        if (self.functions[functionName]['variables'].buscarVar(id)):
            print(id, 'ya existe')

        # Si la variable fue declarada pero no esta en uso en el codigo de la funcion local no se warda
        elif not self.functions[functionName]['variables'].buscarVar(id):
            # se añade direccion a variable
            anadir = self.memory.asignaDirAVariables(functionName, type, id)
            self.functions[functionName]['variables'].agregar(type, id, anadir) # se agrega a tabla de funciones
            # se suma el cont de varibles
            self.functions[functionName]['numberVars'] = self.functions[functionName]['numberVars'] + 1
            #print("no existe en local aun se va a agregar")


    # añande un espacio de memoria a una variable
    def anadirVarMemoria(self, type, vid, funId): # SET
        self.memory.asignaDirAVariables(type, vid, funId)    
        
    def getDirecionVariables(self, var):  # GET
        return self.memory.getDirVariables(var)


    #obtiene numero de parametrod de una funcion
    def getNumParametros(self, functionName):
        return self.funciones[functionName]['numberParams']

    # añade parametros a la tabla de funciones
    # cuando añades param a la tabla le agregas nombre, tipo y le sumas uno al num de params
    def anadirParamsTablaFunc(self, functionName, nameVar, varTipo):
        self.funciones[functionName]['numberParams'] = self.funciones[functionName]['numberParams'] + 1
        self.funciones[functionName]['idParams'].append(nameVar)
        self.funciones[functionName]['tParams'].append(varTipo)
    
    
    def anadirMemoriaVarTemporales(self, type, vid, funId):
       self.memory.asignaDirTemporales(type, vid, funId)    
        

    def getMemoriaVarTemp(self, temp):
        return self.memory.getDirTemporales(temp)
        

    def anadirMemConstantes(self, val):
        self.memory.asignaDirAConstantes(val)
        

    def getMemoriaConstantes(self, val):
        return self.memory.getDirConstantes(val) 
    

    def getMemoriaDeOperadores(self, op):
        return self.memory.getDirOperadores(op)
            
    def imprimirVariablesDeFuncion(self, functionName):
        if functionName in self.funciones:
            self.funciones[functionName]['vars'].printVar()

        
# else:
#             self.functions[functionName]['variables'].agregar(tipo, id)
#             print(id, 'fue añadida exitosamente')

#test

#funcion = tablaFunc()
#funcion.agregarFuncion("void", "factores", 2, ["int", "float"], ["a", "b"], 2)
#print(funcion.buscarFun("factores"))
#funcion.printFun("factores")