class Union():
    def __init__(self,u1,u2):
        self.u1 = u1
        self.u2 = u2

    def __str__(self):
        return "[UNION: " + str(self.u1) + " ^ " + str(self.u2) + "]"

    def compile(self):
        return lambda x: self.u1.compile()(x) or self.u2.compile()(x)

    def vals(self):
        avals = self.u1.vals()
        bvals = self.u2.vals()
        c = self.compile()
        ret = set()

        for val in avals.union(bvals):
            if c(val):
                ret.add(val)
        return ret