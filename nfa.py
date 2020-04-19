from collections import defaultdict

EPSILON = "epsilon"

from nfa import EPSILON

## simulate the searching word on NFA
def simulate(nfa, word, start = 0, isfullmatch=True):

    return __simulate(nfa, word, nfa.start, start, len(word), isfullmatch)

## return the
def __simulate(nfa, input, q, start,end, isfullmatch):
    if not isfullmatch and nfa.isAcceptState(q):
        return start

    if start == end:
        return end if nfa.isAcceptState(q) else -1

    s = input[start]
    nextstates = nfa.nextState(q, s)

    if nextstates != None:
        for next in nextstates:
            ans = __simulate(nfa, input, next, start + 1, end, isfullmatch)
            if ans != -1:
                return ans

    nextstates = nfa.nextState(q, EPSILON)
    if nextstates != None:
        for next in nextstates:
            ans = __simulate(nfa, input, next,start, end, isfullmatch)
            if ans != -1:
                return ans

    return -1

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





