from lexer import *
while True:
    text = input("Project MOPL > ")
    lex = Lexer(text)
    tokens = lex.generateTokens()
    print(tokens)