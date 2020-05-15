import sys

#cubo semantico sirve para cuando se hacen operaciones aritmeticas, logicas, comparaciones, asignaciones

class cuboSemantico():
	
	def __init__(self, arg):
		super(cuboSemantico, self).__init__()
		self.arg = arg
		