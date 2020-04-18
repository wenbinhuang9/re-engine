from lexer import Lexer

from parser import  RegExParser
from idgen import IDGenerator

tokenDefiniton = {"CHAR" : r"\d|[a-zA-Z]|\*|\||\(|\)", "IGNORE" : r"\s"}

def compile(re_str):
    lex = Lexer(tokenDefiniton)
    lex.run(re_str)
    tree = RegExParser(lex).regex()
    idg = IDGenerator()

    nfa = tree.get_nfa(idg)

    return  nfa

