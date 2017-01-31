
class TokenSpan():
    def __init__(self,tokens,startpos,endpos):
        self.tokens = tokens
        self.startpos = startpos
        self.endpos = endpos

    def toks(self):
        return self.tokens[self.startpos:self.endpos]


if __name__ == "__main__":
    sentence = "Greece held its last Summer Olympics in which year?"
    tokens = sentence.split(" ")

    t = TokenSpan(tokens,0,1)
    print(t.toks())