
class Parser(object):
	"""docstring for Parser"""
	def __init__(self, tokens ):
		
		# this will hold all tokens that have created by the lexer
		self.tokens = tokens
		# this will hold the token index were at
		self.token_index = 0

	def parse(self):

		# we loop trough all tokens
		while self.token_index < len(self.tokens):

			# holds type of token (integer, identifier....)
			token_type = self.tokens[self.token_index][0]

			# holds value of token (var, age,....)
			token_value = self.tokens[self.token_index][1]


			# this will triger when a variable declaration token is found
			if token_type == "VAR_DECLERATION" and token_value == "var":
				self.parse_variable_decleration( self.tokens[ self.token_index:len(self.tokens) ])


			# increment so we can loop through all the elements
			self.token_index += 1

	def parse_variable_decleration(self, token_stream):
		tokens_checked = 0

		for token in range(0, len(token_stream)):
			token_type = token_stream[tokens_checked][0]
			token_value = token_stream[tokens_checked][1]

			# this will get the variable (var, let, const...)
			if token == 0:
				print("Variable type: " + token_value)

			#this will get the variable name and error validation 
			elif token == 1 and token_type == "IDENTIFIER":
				print("Variable name: " + token_value)


			elif token == 1 and token_type != "IDENTIFIER":
				print("Error: Invalid variable name " + token_value)
				quit()

			elif token == 2 and token_type == "OPERATOR"







		