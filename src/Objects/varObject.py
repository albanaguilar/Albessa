
class variableObject(object):
	"""docstring for variableObject"""
	def __init__(self):

		# this will hold the python exec string for the variable declaracion
		self.exec_string = ""


	# name of the variable
	# assigment type
	# value the variable holds
	def transpile(self, name, operator, value):

		# appends python exec string converted using parser
		# translates to " variable = something " in python
		self.exec_string += name + " "+ operator + " " + value + "\n"
		return self.exec_string