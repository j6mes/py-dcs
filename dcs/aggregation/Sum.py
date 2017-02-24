from dcs.base.Atom import Atom


class Sum():
    def __init__(self, u):
        self.u = u

    def __str__(self):
        return "[SUM: " + str(self.u) + "]"

    def compile(self):
        return lambda x: x in self.vals()

    def vals(self):
        sum_val = 0
        for value in self.u.vals():
            if isinstance(value.value, str):
                return None
            sum_val += value.value

        return {Atom(sum_val)}
