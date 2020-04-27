import re #this imports regular expresions library
import ply.lexx as lexx
import ply.yacc as yacc
import sys


class Lexer(object):
	"""docstring for Lexer"""
	def __init__(self, source_code):
		#super(Lexer, self).__init__()
		self.source_code = source_code

	#tokenize turns source code into tokens
	def tokenize(self):

		# where all the tokens created by lexer will be stored
		tokens = []

		# list of all the words in our test.lang file
		source_code = self.source_code.split()

		# this will keep track of the word index were at in the source_code
		source_index = 0

		# loop through each word in source_code to generate tokens
		while source_index < len(source_code):
			word = source_code[source_index]

			# this will recognize a variable and create a token for it 
			if word == "var": 
				tokens.append(["VAR_DECLERATION", word])

			# this will recognize a word and create an identifier token for it
			elif re.match("[a-z]", word) or re.match("[A-Z]", word):
				if word[len(word) - 1] == ";":
					tokens.append(["IDENTIFIER", word[0:len(word) - 1]])
				else:
					tokens.append(["IDENTIFIER", word])

			# this will recognize number and create an integer token for it
			elif re.match("[0-9]", word):
				if word[len(word) - 1] == ";":
					tokens.append(["INTEGER", word[0:len(word) - 1]])
				else:
					tokens.append(["INTEGER", word])

			# this will recognize operators and create a token for it 
			elif word in "=/*=-+":
				tokens.append(["OPERATOR", word])

			# if a ; is found at the last character in a word then add a statement end token
			if word[len(word) - 1] == ";":
				tokens.append(["STATEMENT_END", ";"])


			source_index += 1

		print(tokens)

		return tokens # returns created tokens










