from tablaDeVariables import tablaVar
import sys

# function table
class tablaFunc():
    def __init__(self): #create dictionary
        self.functions = { }


    def agregarFuncion(self, type, fid, numberParams, paramType, paramsID, numberVars):
        if fid not in self.functions.keys(): #params to save in the table
            self.functions[fid] = {
                'type' : type, 
                'numberParams' : numberParams,
                'paramType' : paramType,
                'paramsID' : paramsID, 
                'variables' : tablaVar(), #it is done separatly, too many vars
                'numberVars' : numberVars }
            print('Funcion añadida:',fid)
        else:
            print(id , 'ya existe')



    def buscarFun(self, id):
        return id in self.functions 



    # function to add variable to table function
    # to associate certain variables to certain functions
    def agregarVariable(self, fid, tipo, id):
        if (self.functions[fid]['variables'].buscarFun(id)):
            print(id, 'ya existe')
        else:
            self.functions[fid]['variables'].agregarFuncion(tipo, id)
            print(id, 'fue añadida exitosamente')
            


    def print(self, fid):
        if id in self.functions:
            self.functions[fid]['variables'].printVar()
        

















