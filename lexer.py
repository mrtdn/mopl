#############
# LEXER
#############

from error import IllegalCharacterError
from tokens import *
from constants import *


class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.currChar = self.text[self.pos]

    def nextChar(self):
        self.pos += 1
        self.currChar = self.text[self.pos] if self.pos < len(
            self.text) else None

    def generateTokens(self):
        tokens = []

        while (self.currChar != None):
            ch = self.currChar
            if ch in " \t":
                self.nextChar()
            elif ch in DIGITS:
                tokens.append(self.makeNumber())
                self.nextChar()
            elif ch == '+':
                tokens.append(Token(TT_PLUS))
                self.nextChar()
            elif ch == '-':
                tokens.append(Token(TT_MINUS))
                self.nextChar()
            elif ch == '/':
                tokens.append(Token(TT_DIV))
                self.nextChar()
            elif ch == '*':
                tokens.append(Token(TT_MUL))
                self.nextChar()
            else:
                # IllegalCharacterError
                return [], IllegalCharacterError(f'\'{self.currChar}\'').toString()

        return tokens, None

    def makeNumber(self):
        isDot = False
        num = ""
        while self.currChar != None and self.currChar in DIGITS + '.':
            if (self.currChar == '.'):
                if isDot:
                    break
                isDot = True
                num += "."
            else:
                num += self.currChar
            self.nextChar()

        if isDot:
            return Token(TT_FLOAT, float(num))
        else:
            return Token(TT_INT, int(num))
