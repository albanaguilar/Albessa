import lexer
import parser

def main():

	#red the content of test.lang and store it to start lexing it
	content = ""
	with open("test.lang", "r") as file:
		content = file.read()


	#LEXER
	#
	# we create an instance of the lexer class and pass the content var
	# we initialize the lexer class with the source code
	lex = lexer.Lexer(content)
	tokens = lex.tokenize()


	#PARSER
	#
	#
	parse = parser.Parser(tokens)
	parse.parse()

main()