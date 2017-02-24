from dcs.base.Atom import Atom


class Count():
    def __init__(self,u):
        self.u = u

    def __str__(self):
        return "[COUNT: " + str(self.u) + "]"

    def vals(self):
        return {Atom(len(self.u.vals()))}

    def compile(self):
        return lambda x: x in self.vals()