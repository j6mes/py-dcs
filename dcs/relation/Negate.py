from dcs.TypeInfo import TypeInfo
from dcs.extra.EntityContainer import EntityContainer


class Negate(TypeInfo):
    def __init__(self, u):
        self.u = u

    def compile(self):
        return lambda x: not self.u.compile()(x)

    def vals(self):
        c = self.compile()
        ret = set()

        for v in EntityContainer.entities:
            if(c(v)):
                ret.add(v)
        return ret
