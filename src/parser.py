
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

			print(token_type, token_value)


			# increment so we can loop through all the elements
			self.token_index += 1
		