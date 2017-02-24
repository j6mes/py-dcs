from dcs.base.Pair import Pair


class Property():
    def __init__(self,name):
        self.name = name
        self.pairs = set()

    def add(self,k,v):
        self.pairs.add(Pair(k,v))

    def vals(self):
        return self.pairs

    def p(self,x,y):
        return Pair(x,y) in self.pairs

    def compile(self):
        return lambda x,y: self.p(x,y)

    def __str__(self):
        return "[PROPERTY: "+str(self.name)+"]"

    def __hash__(self):
        return "$PROPR$".__hash__() + self.name.__hash__()

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return other.name == self.name
        return False
