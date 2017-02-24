class Pair():
    def __init__(self,k,v):
        self.k = k
        self.v = v

    def __hash__(self):
        return self.k.__hash__() + "$$$".__hash__() + self.v.__hash__()

    def __str__(self):
        return "[PAIR: " + str(self.k) + " -> " + str(self.v) + "]"

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.k == other.k and self.v == other.v
        return False