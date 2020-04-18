from collections import defaultdict

EPSILON = "epsilon"

from nfa import EPSILON


def simulate(nfa, word):

    return __simulate(nfa, word, nfa.start)

def __simulate(nfa, input, q):
    if len(input) == 0:
        return nfa.isAcceptState(q)

    s = input[0]
    nextstates = nfa.nextState(q, s)

    if nextstates != None:
        for next in nextstates:
            ans = __simulate(nfa, input[1:], next)
            if ans == True:
                return True

    nextstates = nfa.nextState(q, EPSILON)
    if nextstates != None:
        for next in nextstates:
            ans = __simulate(nfa, input, next)
            if ans == True:
                return True

    return False

class NFA():
    def __init__(self):
        self.start = None
        self.accept = None
        ## (state, symbol)->list of states
        self.transitions = defaultdict(list)
        self.states = set([])

    def append(self, nfa_list):
        for nfa in nfa_list:
            self.addSingle(nfa)

        return self
    def addSingle(self, nfa):
        self.transitions.update(nfa.transitions)
        self.states.update(nfa.states)

        return self


    def startState(self, start):


        self.start = start
        self.states.add(start)
        return self

    def acceptState(self, accept):

        self.accept = accept
        self.states.add(accept)

        return self

    ## q1 accepting s , go to q2
    def addTransitions(self, q1, s, q2):
        if isinstance(q1, int):
            q1 = str(q1)
        if isinstance(q2, int):
            q2 = str(q2)

        self.states.add(q1)
        self.states.add(q2)

        self.transitions[(q1, s)].append(q2)

        return self
    def isAcceptState(self, q):
        return  q == self.accept


    def nextState(self, q, s):
        next = self.transitions[(q, s)]

        return next
    def match(self, word, left = 0, right = None):
        if right == None:
            word = word[left:]
        else:
            word = word[left : right]

        return simulate(self, word)


    def find(self):
        pass






