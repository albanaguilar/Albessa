from tablaDeVariables import tablaVar
import sys

# function table
class tablaFunc():
    def __init__(self): #create dictionary
        self.functions = { }


    def agregarFuncion(self, type, functionName, numberParams, paramType, vars, numberVars):
        if functionName not in self.functions.keys(): #params to save in the table
            self.functions[functionName] = {
                'type' : type, 'numberParams' : numberParams,
                'paramType' : paramType, 'vars' : vars, 
                'variables' : tablaVar(), #it is done separatly, too many vars
                'numberVars' : numberVars }
            print('Funcion añadida:',functionName, ' ', type)
        else:
            print(id , 'ya existe')

    def buscarFun(self, id):
        return id in self.functions 

    # function to add variable to table function
    # to associate certain variables to certain functions
    def agregarVariable(self, functionName, tipo, id):
        if (self.functions[functionName]['variables'].buscarVar(id)):
            print(id, 'ya existe')
        else:
            self.functions[functionName]['variables'].agregar(tipo, id)
            print(id, 'fue añadida exitosamente')
            

    def printFun(self, functionName):
        if id in self.functions:
            self.functions[functionName]['variables'].printVar()


        


#test

#funcion = tablaFunc()
#funcion.agregarFuncion("void", "factores", 2, ["int", "float"], ["a", "b"], 2)
#print(funcion.buscarFun("factores"))
#funcion.printFun("factores")













