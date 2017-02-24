class Atom():
    def __init__(self, v):
        if isinstance(v,Atom):
            v = v.value
        self.value = v

    def vals(self):
        return {self}

    def compile(self):
        return lambda x: x == self or x == self.value

    def __str__(self):
        return "[ATOM:" + str(self.value) + "]"

    def __hash__(self):
        return self.value.__hash__()

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return other.value == self.value
        return False

