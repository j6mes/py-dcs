from dcs.base.Atom import Atom


class Subtract():
    def __init__(self,u1,u2):
        self.u1 = u1
        self.u2 = u2

    def __str__(self):
        return "[SUBTRACT: " + str(self.u2) + " - " + str(self.u1)+ "]"

    def compile(self):
        return lambda x: x in self.vals()

    def vals(self):
        u1vals = self.u1.vals()
        u2vals = self.u2.vals()

        ret = set()

        if len(u1vals) == 1:
            for u in u1vals:
                for v in u2vals:
                    ret.add(Atom(v.value-u.value))

        return ret