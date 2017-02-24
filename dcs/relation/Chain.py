class Chain():
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