import sys

#clase para guardar en una variable el nombre y tipo de los datos del programa
# y poder meterlos a la lista en el main.py


#esto se pudo poner en el main pero para no rebolverme mas cree otra clase
class nombreTipo():
    def __init__(self, type, identificador):
        self.type = type
        self.identificador = identificador


# oj = nombreTipo("int",'hola')
# lista = []
# lista.append(oj)
# print(lista [-1].type)