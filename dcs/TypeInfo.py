class TypeInfo():
    def get_types(self):
        types = set()
        for v in self.vals():
            types.add(type(v))
        return types

    def vals(self):
        return {}

    def compatible(self,test):
        return True

class ChainableType(TypeInfo):
    def chain(self,test):
        avals = self.vals()
        bvals = test.vals()

        atypes = set()
        btypes = set()

        for a in avals:
            atypes.add(type(a.v))

        for b in bvals:
            btypes.add(type(b.k))

        return atypes == btypes