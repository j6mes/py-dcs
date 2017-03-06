from dcs.TypeInfo import TypeInfo, ChainableType
from dcs.base.Pair import Pair


class Reverse(ChainableType):
    def __init__(self, b):
        self.b = b

    def __str__(self):
        return "R[" + str(self.b) + "]"

    def vals(self):
        ret = set()

        for p in self.b.vals():
            ret.add(Pair(p.v, p.k))

        return ret

    def compile(self):
        c = self.b.compile()
        return lambda x, y: c(y, x)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return other.b == self.b
        return False

    def __hash__(self):
        return -self.b.__hash__()
