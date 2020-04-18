import re

class Token():
    def __init__(self, type, value):
        self.type = type
        self.value = value
        self.lineno = None

    def text(self):
        return  self.value

    def __repr__(self):
        return "type={0},value={1}".format(self.type, self.value)

class Lexer():
    def __init__(self, tokenDefiniton):
        self.tokens = []
        self.tokenDefiniton = tokenDefiniton
        self.patternList = []
        self.__getPatterns()


    def __getPatterns(self):
        for tokentype, restr in self.tokenDefiniton.items():
            pat = re.compile('(' + restr + ')')
            self.patternList.append(pat)

    def hasNext(self):
        return  len(self.tokens) > 0

    def eat(self, c):
        token = self.nextToken()
        assert token.value == c

    def more(self):
        return  len(self.tokens) > 0

    def nextToken(self):

        token = self.tokens[0]
        self.tokens.pop(0)

        return token

    def peak(self, index = 0):
        if index >= len(self.tokens):
            return None
        return self.tokens[index].text()


    def run(self, input):
        begin = 0
        end = len(input)
        try:
            while begin < end:
                for i, pattern in enumerate(self.patternList):
                    matched_obj = pattern.match(input, begin, end)
                    if matched_obj != None:
                        matched_str = matched_obj.group(1)
                        begin += len(matched_str)
                        self.tokens.append(Token(self.tokenDefiniton.keys()[i], matched_str))
                        break


        except Exception as e:
            print(e)
            raise ValueError("invalid input={0}, beginIndex={1}", input, begin)
