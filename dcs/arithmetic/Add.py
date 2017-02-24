from dcs.base.Atom import Atom


class Add():
    def __init__(self,u1,u2):
        self.u1 = u1
        self.u2 = u2

    def __str__(self):
        return "[ADD: " + str(self.u1) + "+" + str(self.u2) + "]"

    def compile(self):
        return lambda x: x in self.vals()

    def vals(self):
        u1vals = self.u1.vals()
        u2vals = self.u2.vals()

        ret = set()

        if len(u1vals) == 1:
            for u in u1vals:
                for v in u2vals:
                    ret.add(Atom(u.value+v.value))

        return ret
