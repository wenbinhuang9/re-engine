from lexer import Lexer

from parser import  RegExParser
from idgen import IDGenerator
from nfa import  simulate, NFA

tokenDefiniton = {"CHAR" : r"\d|[a-zA-Z]|\*|\||\(|\)", "IGNORE" : r"\s"}

class Match():
    def __init__(self):
        self.matchedList = []

    def append(self, matchedobj):
        self.matchedList.append(matchedobj)

        return self

    def __repr__(self):
        return self.matchedList.__repr__()
def compile(re_str):
    lex = Lexer(tokenDefiniton)
    lex.run(re_str)
    tree = RegExParser(lex).regex()
    idg = IDGenerator()

    nfa = tree.get_nfa(idg)
    return  nfa

def matchfull(pattern,  word, left = 0, right = None):
    if right == None:
        word = word[left:]
    else:
        word = word[left : right]
    return Match().append(word) if simulate(pattern, word) >=0 else None

def match(pattern, word):
    if not isinstance(pattern, NFA):
        pattern = compile(pattern)

    idx = simulate(pattern,word, isfullmatch=False)
    if idx == -1:
        return None
    return Match().append(word[:idx])


def search(pattern, word):
    if not isinstance(pattern, NFA):
        pattern = compile(pattern)

    for i in range(len(word)):
        idx = simulate(pattern,word, start=i, isfullmatch=False)
        if idx != -1:
            return Match().append(word[i :idx])

    return None

def findAll(pattern, word):
    if not isinstance(pattern, NFA):
        pattern = compile(pattern)

    i = 0

    matchObj = Match()
    while i < len(word):
        idx = simulate(pattern, word, start = i, isfullmatch=False)
        if idx != -1:
            matchObj.append(word[i:idx])
            i = idx
        else:
            i += 1

    return matchObj


