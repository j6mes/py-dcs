from dcs.TokenSpan import TokenSpan
from dcs.Atom import Atom
from dcs.Rule import Rule


class TokenSpanToAtom(Rule):
    def __init__(self, input):
        super().__init__(TokenSpan, Atom)
        super().check(input)
        self.toks = input.toks()

    def emit(self):
        return Atom(self.toks)


if __name__ == "__main__":
    sentence = "Greece held its last Summer Olympics in which year?"
    tokens = sentence.split(" ")

    t = TokenSpan(tokens,0,1)
    r = TokenSpanToAtom(t)

    print(r.emit())
