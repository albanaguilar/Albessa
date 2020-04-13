
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

			# if statement_end or ; is found it breaks the for loop
			if token_type == "STATEMENT_END":
				break


			# this will get the variable (var, let, const...)
			if token == 0:
				print("Variable type: " + token_value)

			#this will get the variable name and error validation 
			elif token == 1 and token_type == "IDENTIFIER":
				print("Variable name: " + token_value)

			elif token == 1 and token_type != "IDENTIFIER":
				print("Error: Invalid variable name " + token_value)
				quit()

			# this will get variable Assignment opererator and does error validation
			elif token == 2 and token_type == "OPERATOR":
				print("Asignment opererator: " + token_value)
			elif token == 2 and token_type != "OPERATOR":
				print("Error: Assignment opererator is invalid")
				quit()


			# this will get the variable value assigned
			elif token == 3 and token_type in ["STRING","INTEGER", "IDENTIFIER"]:
				print("Variable value: " + token_value)
			elif token == 3 and token_type not in ["STRING","INTEGER", "IDENTIFIER"]:
				print("Invalid variable assignment value " + token_value)
				quit()


			tokens_checked += 1

		# increment token index by amount of tokens we checked so no need to check again
		self.token_index += tokens_checked













		