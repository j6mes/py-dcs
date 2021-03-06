from dcs.TypeInfo import TypeInfo
from dcs.base.Atom import Atom


class Max(TypeInfo):
    def __init__(self,u):
        self.u = u

    def __str__(self):
        return "[MAX: " + str(self.u) + "]"

    def compile(self):
        return lambda x: x in self.vals()

    def vals(self):
        current_max = float("-inf")
        for v in self.u.vals():
            if isinstance(v.value,str):
                return None
            if v.value > current_max:
                current_max = v.value

        return {Atom(current_max)}
