import sys

class Memoria:
    def __init__(self):

        # se hacen diccionarios para asociar simbolos a numeros
        self.const = {}
        self.var ={}
        self.temp = {}
        self.loc = {}

        # a cada type de variable se le asigna un espacio de memoria
        # de 1000 en el que puede almacenar la cantidad necesaria
        self.intsGlobales = 500 #500 a 1499
        self.floatsGlobales = 1500 # 1500 a 2499
        self.charsGlobales = 2500 #2500 a 3499
        self.boolsGlobales = 3500 # 3500 a 4499
        ######################
        self.intsTemporales = 5000 # 5000 a 5999
        self.floatsTemporales = 6000 #6000 a 6999
        self.charsTemporales = 7000 #7000 a 7999
        self.boolsTemporales = 8000 #8000 a 8999
        ######################
        self.intLocal = 10000 #10000 a 19999
        self.floatsLocal = 20000 #20000 a 29999
        self.charLocal = 30000 # 30000 a 39999
        self.boolLocal = 40000 # 40000 a 44999
        ######################
        self.intsConstantes = 45000 #45000 a 45999
        self.floatsConstantes = 46000 #46000 a 46999
        self.charsConstantes = 47000 #47000 a 47999
        self.stringConstantes = 48000 #48000 a 49000

        #cada simbolo se represnta mediante un numero
        self.operadores = {
            '+':1, '-':2, '/':3, '*':4, '=':5, '<':6, '>':7
            , '<>':8, '<=':9 , '=>':10, '&':11, '|':12, '==':13, 'for': 14,
            'while': 15, 'read': 16, 'print': 17, 'GOTO' : 18, 'GOTOV' : 19,
            'GOTOF' : 20, 'return': 21, 'GOSUB' : 22, 'ENDPROC' : 23, 'END': 24
            }


    def guardarValorDatoMemoria(self, direccion, val):
        if direccion < 3500: 
            if direccion < 1500: #500 a 1499
                self.globales[direccion] = val
                print(val, " global entera")
            elif direccion < 2500: # 1500 a 2499
                self.globales[direccion] = val
                print( val ,"global flotante")
            elif direccion < 3500: #2500 a 3499
                self.globales[direccion] = val
                print(val,  " global char")
            else: 
                self.globales[direccion] = val
                print( val, " global bool")

        elif direccion >= 5000 and direccion < 9000: 
            if direccion <= 5999: # 5000 a 5999
                self.temporal[direccion] = val
                print(val, " temporal entera")

            elif direccion < 6999: #6000 a 6999
                self.temporal[direccion] = val
                print(val, " temporal flotante")

            elif direccion < 7999: #7000 a 7999
                self.temporal[direccion] = val
                print(val, " temporal char")

            elif direccion < 8999: #8000 a 8999
                self.temporal[direccion] = val
                print(val, " temporal bool")
        else:
            if direccion >= 10000 and direccion <= 44999:
                if direccion <= 19999: #10000 a 19999
                    self.locales[direccion] = val
                    print( val," local entera")
           
                elif direccion <= 29999: #20000 a 29999
                    self.locales[direccion] = val
                    print(val," local flotante")
            
                elif direccion <= 39999: # 30000 a 39999
                    self.locales[direccion] = val
                    print(val, " local char")
            
                elif direccion <= 44999: # 40000 a 44999
                    self.locales[direccion] = val
                    print(val, " local bool")
                # else:
                #     print("fuera de rango")  
                    

    ########################################################################
    ######### GLOBALES #############################################
        
    def establecerDirVariables(self, functionName, type, id): #set
    #se checa si la funcion es la global, la principal
        if functionName == 'program':
            if type == 'int':
                if self.intsGlobales > 500 and self.intsGlobales < 1500:
                    # se le asigna una direccion y luego se incrementa para no asignar
                    # la misma direccion a dos datos
                    direccion = self.intsGlobales
                    self.intsGlobales += 1
                    print(id," su direccion: ", direccion)
                    return direccion
                    
            elif type == 'float': 
                if self.floatsGlobales > 1500 and self.floatsGlobales < 2499: # 1500 a 2499
                    direccion = self.floatsGlobales
                    self.floatsGlobales += 1
                    print(id, " su direccion: ", direccion)
                    return direccion

            elif type == 'char': 
                if self.charsGlobales >= 2500 and self.charsGlobales < 3499: #2500 a 3499
                    direccion = self.charsGlobales
                    self.charsGlobales += 1
                    print(id, " su direccion: ", direccion)
                    return direccion

            else:
                if self.boolsGlobales >= 3500 and self.boolsGlobales < 4499: # 3500 a 4499
                    direccion = self.boolsGlobales
                    self.boolsGlobales += 1
                    print(id, " su direccion: ", direccion)
                    return direccion

    ########################################################################
    ######### LOCALES #############################################
        else:
            if type == 'int':
                if self.intLocal >= 10000 and self.intLocal < 19999:
                    direccion = self.intLocal
                    self.intLocal += 1
                    print(id, " su direccion: ", direccion)
                    return direccion

            elif type == 'float':
                if self.floatsLocal >= 20000 and self.floatsLocal < 29999: #20000 a 29999
                    direccion = self.floatsLocal
                    self.floatsLocal += 1
                    print(id, " su direccion: ", direccion)
                    return direccion

            elif type == 'char':
                if self.charLocal>= 30000 and self.charLocal < 39999:  # 30000 a 39999
                    direccion = self.charLocal
                    self.charLocal += 1
                    print(id, " su direccion: ", direccion)
                    return direccion

            elif self.boolLocal >= 40000 and self.boolLocal < 44999: # 40000 a 44999
                direccion = self.boolLocal
                self.boolLocal += 1
                print(id, " su direccion: ", direccion)
                return direccion    
    
    ########################################################################
    ######### TEMPORALES #############################################
    
    def establecerDirTemporales(self, functionName, type, id):
        if type == 'int':
            if self.intsTemporales >= 5000 and self.intsTemporales < 5999: # 5000 a 5999
                direccion = self.intsTemporales
                #print("direccion es ", direccion)
                self.intsTemporales += 1
                print(id, " su direccion: ", direccion)
                return direccion

        elif type == 'float':
           if self.floatsTemporales >= 6000 and self.floatsTemporales < 6999: #6000 a 6999      
               direccion = self.floatsTemporales
               self.floatsTemporales += 1
               print(id, " su direccion: ", direccion)
               return direccion
                    
        elif type == 'char':
            if self.charsTemporales > 7000 and self.charsTemporales < 7999:  #7000 a 7999
                direccion = self.charsTemporales
                self.charsTemporales += 1
                print(id, " su direccion: ", direccion)
                return direccion
            
        elif self.boolsTemporales > 8000 and self.boolsTemporales < 8999:    #8000 a 8999             
            direccion = self.boolsTemporales
            self.boolsTemporales += 1
            print(id, " su direccion: ", direccion)
            return direccion


    ########################################################################
    ######### CONSTANTES ############################################

    # Funcion para asignar valores a constantes
    def establecerConstantes(self, val): #Set
        if isinstance(val, int):
            if self.intsConstantes > 45000 and self.intsConstantes < 45999:  #45000 a 45999
                direccion = self.intsConstantes
                self.intsConstantes += 1
                print(id, " su direccion: ", direccion)
                return direccion
        
        elif isinstance(val, float):
            if self.floatsConstantes > 46000 and self.floatsConstantes < 46999:  #46000 a 46999
                direccion = self.floatsConstantes
                self.floatsConstantes += 1
                print(id, " su direccion: ", direccion)
                return direccion
        
        elif isinstance(val, str):
            if len(val)<2:
                if self.charsConstantes > 47000 and self.charsConstantes < 47999:  #47000 a 47999
                    direccion = self.stringConstantes
                    self.charsConstantes += 1
                    print(id," su direccion: ", direccion)
                    return direccion
            else: 
                self.stringConstantes > 48000   #48000 a 49000
                direccion = self.stringConstantes
                self.stringConstantes += 1
                print(id, " su direccion: ", direccion)
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
            return self.temp[temp]['direccion']
        else:
            return -1
