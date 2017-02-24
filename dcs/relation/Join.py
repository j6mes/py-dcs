from dcs.relation.support.NonGenerator import NonGenerator


class Join():
    def __init__(self, b, u):
        self.b = b
        self.u = u

    def compile(self):
        bc = self.b.compile()
        uc = self.u.compile()
        ys = self.u.vals()

        if NonGenerator() in ys:
            ys = [v.v for v in self.b.vals()]

        return lambda x: True in [uc(y) and bc(x, y) for y in ys]

    def vals(self):
        c = self.compile()
        ret = set()
        for x in self.b.vals():
            if c(x.k):
                ret.add(x.k)
        return ret

    def __str__(self):
        return ("[JOIN: " + str(self.b) + " x " + str(self.u) + "]")

