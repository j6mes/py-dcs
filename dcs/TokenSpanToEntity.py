from dcs.TokenSpan import TokenSpan
from dcs.Entity import Entity
from dcs.Rule import Rule


class TokenSpanToEntity(Rule):
    def __init__(self, input):
        super().__init__(TokenSpan, Entity)
        super().check(input)
        self.toks = input.toks()

    def emit(self):
        return Entity(self.toks)


if __name__ == "__main__":
    sentence = "Greece held its last Summer Olympics in which year?"
    tokens = sentence.split(" ")

    t = TokenSpan(tokens,0,1)
    r = TokenSpanToEntity(t)

    print(r.emit())
