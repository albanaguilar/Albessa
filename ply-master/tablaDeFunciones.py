class tablaVar:
    def __init__(self): #whith self we can access the atributes of the class in python
        self.listaVariables = { }
        
    def agregar(self, type, id):
        self. listaVariables[id ] = {
            'type': type
        }
    def buscarVar(self, id):
        return id in self.listaVariables
    
    def print(self): #para ver si esta guardada la variable en la tabla
        for i in self.listaVariables:
            print('Variable', i, 'se encuentra en la tabla de variables')