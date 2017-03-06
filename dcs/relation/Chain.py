from dcs.TypeInfo import TypeInfo, ChainableType
from dcs.base.Pair import Pair


class Chain(ChainableType):
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def compile(self):
        a = self.a.compile()
        v = self.a.vals()

        b = self.b.compile()
        return lambda x,z: True in [a(x,y.v) and b(y.v,z) for y in v]

    def vals(self):
        avals = self.a.vals()
        bvals = self.b.vals()
        c = self.compile()

        ret = set()
        for a in avals:
            for b in bvals:
                if c(a.k,b.v):
                    ret.add(Pair(a.k,b.v))
        return ret

    def __str__(self):
        return "[CHAIN: "+str(self.a) +" x "+str(self.b)+"]"

    def __hash__(self):
        return "$CHAIN$".__hash__() + self.a.__hash__() + self.b.__hash__()

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return other.a == self.a and other.b == self.b
        return False
