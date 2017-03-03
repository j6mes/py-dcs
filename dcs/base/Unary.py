class Unary():
    def __init__(self,name):
        self.name = name
        self.values = set()

    def add(self,v):
        self.values.add(v)

    def contains(self,e):
        for v in self.values:
            if e == v:
                return True
        return False

    def vals(self):
        return self.values

    def __str__(self):
        return "[UNARY: " + str(self.name) + "]"

    def compile(self):
        return lambda x: self.contains(x) or x in self.values

    def __hash__(self):
        return "$UNARY$".__hash__() + self.name.__hash__()

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return other.name == self.name
        return False

    