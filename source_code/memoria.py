import sys

class Memoria:
    def __init__(self):

        # se hacen diccionarios para asociar simbolos a numeros
        self.const = {}
        self.var ={}
        self.temp = {}

        # a cada type de variable se le asigna un espacio de memoria
        # de 1000 en el que puede almacenar la cantidad necesaria
        self.intsGlobales = 500 # 18 a 500
        self.floatsGlobales = 1500 #501 a 1500
        self.charsGlobales = 2500 # 1501 a 2500
        self.boolsGlobales = 3500 # 2501 a 3500
        self.intsTemporales = 5000 #3501 a 5000
        self.floatsTemporales = 6000 # 5001 a 6000
        self.charsTemporales = 7000 #6001 a 7000
        self.boolsTemporales = 8000 #7001 a 8000
        self.intLocal = 10000 #8001 a 10000
        self.floatsLocal = 20000 # 10001 20000
        self.charLocal = 30000 # 20001 a 30000
        self.boolLocal = 40000 # 30001 a 40000
        self.intsConstantes = 45000 # 40001 a 45000
        self.floatsConstantes = 46000 # 45001 a 46000
        self.charsConstantes = 47000 # 46001 a 47000
        self.stringConstantes = 48000 # 47001 a 48000

        #cada simbolo se represnta mediante un numero
        self.operadores = {
            '+':1, '-':2, '/':3, '*':4, '=':5, '<':6, '>':7
            , '<>':8, '<=':9 , '=>':10, '&':11, '|':12, '==':13, 'for': 14,
            'while': 15, 'read': 16, 'print': 17
            }

    ########################################################################
    ######### GLOBALES #############################################
        
    def establecerDirVariables(self, functionName, type, id): #set
    #se checa si la funcion es la global, la principal
        if functionName == 'program':
            if type == 'int':
                if self.intsGlobales > 18 and self.intsGlobales <= 500:
                    # se le asigna una direccion y luego se incrementa para no asignar
                    # la misma direccion a dos datos
                    direccion = self.intsGlobales
                    self.intsGlobales += 1
                else:
                    print("fuera de rango")
                    
            elif type == 'float': #501 a 1500
                if self.floatsGlobales >= 501 and self.floatsGlobales <= 1500:
                    direccion = self.floatsGlobales
                    self.floatsGlobales += 1
                else:
                    print("fuera de rango")

            elif type == 'char': # 1501 a 2500
                if self.charsGlobales > 1500 and self.charsGlobales <= 2500:
                    direccion = self.charsGlobales
                    self.charsGlobales += 1
                else:
                    print("fuera de rango")

            else:
                if self.boolsGlobales >= 2501 and self.boolsGlobales <= 3500: # 2501 a 3500
                    direccion = self.boolsGlobales
                    self.boolsGlobales += 1

    ########################################################################
    ######### LOCALES #############################################

        else:
            if type == 'int':
                if self.intLocal > 8001 and self.intLocal < 10000:
                    direccion = self.intLocal
                    self.intLocal += 1
                    return direccion
                else:
                    print("fuera de rango")

            elif type == 'float':
                if self.floatsLocal >= 10001 and self.floatsLocal < 20000: # 10001 20000
                    direccion = self.floatsLocal
                    self.floatsLocal += 1
                    return direccion
                else:
                    print("fuera de rango")
            elif type == 'char':
                if self.charLocal >= 20001 and self.charLocal < 30000:  # 20001 a 30000
                    direccion = self.charLocal
                    self.charLocal += 1
                    return direccion

            elif self.boolLocal >= 30001 and self.boolLocal < 40000: # 30001 a 40000
                direccion = self.boolLocal
                self.boolLocal += 1
                return direccion    
    
    ########################################################################
    ######### TEMPORALES #############################################
    
    def establecerDirTemporales(self, functionName, type, id):
        if type == 'int':
            if self.intsTemporales >= 3501 and self.intsTemporales < 5000: #3501 a 5000
                direccion = self.intsTemporales
                #print("direccion es ", direccion)
                self.intsTemporales += 1
                return direccion
            else:
                print("fuera de rango")

        elif type == 'float':
           if self.floatsTemporales >= 5001 and self.floatsTemporales < 6000: # 5001 a 6000       
               direccion = self.floatsTemporales
               self.floatsTemporales += 1
               return direccion
           else:
                print("fuera de rango")
                    
        elif type == 'char':
            if self.charsTemporales >= 6001 and self.charsTemporales < 7000:  #6001 a 7000
                direccion = self.charsTemporales
                self.charsTemporales += 1
                return direccion
            else:
                print("fuera de rango")
            
        elif self.boolsTemporales >= 7001 and self.boolsTemporales < 8000:    #7001 a 8000               
            direccion = self.boolsTemporales
            self.boolsTemporales += 1
            return direccion


    ########################################################################
    ######### CONSTANTES ############################################
    
    # Funcion para asignar valores a constantes
    def establecerConstantes(self, val): #Set
        if isinstance(val, int):
            if(self.intsConstantes >= 45001 and self.intsConstantes < 46000):  # 45001 a 46000
                direccion = self.intsConstantes
                self.intsConstantes += 1
                return direccion
        
        elif isinstance(val, float):
            if self.floatsConstantes >= 45001 and self.floatsConstantes < 46000:  # 45001 a 46000
                direccion = self.floatsConstantes
                self.floatsConstantes += 1
                return direccion
        
        elif isinstance(val, str):
            if len(val)<2:
                if self.charsConstantes >= 46001 and self.charsConstantes < 47000:  # 46001 a 47000
                    direccion = self.stringConstantes
                    self.charsConstantes += 1
                    return direccion
            else: 
                self.stringConstantes >= 47001 and self.stringConstantes < 48000   # 47001 a 48000
                direccion = self.stringConstantes
                self.stringConstantes += 1
                return direccion


    def asignaDirAVariables(self,functionName, type, id): #set
        anadir = self.establecerDirVariables(functionName, type, id)
        self.var[id] = {
            'direccion': anadir
        }
        
    def getDirVariables(self, temp): # get
        if temp in self.var.keys():
            return self.var[temp]['direccion']
    

    def asignaDirAConstantes(self, val): #Set
        #asigna una direccion de memoria para agregar al diccionario de ctes
        if self.getDirConstantes(val) == -1:
            ad = self.establecerConstantes(val)
            print("\tLa CONSTANTE", val, "ahora se ha guardado en ", ad)
            self.const[val] = {
            'direccion': ad
            }
        
    def getDirConstantes (self, val):  #get
        if val in self.const.keys():
            return self.const[val]["direccion"]
        else:
            return -1
    
    def getDirOperadores(self, op): #get
        if op in self.operadores.keys():
            return self.operadores[op]

    # asigna direccion de memoria a variables temporales
    def asignaDirTemporales(self, functionName, type, id):
        if self.getDirTemporales(id) == -1:           
            anadir = self.establecerDirTemporales(functionName, type, id)
            self.temp[id] = {
                'direccion': anadir
            }

    def getDirTemporales(self, temp):
        if temp in self.temp.keys():
            return self.temp[temp]['address']
        else:
            return -1