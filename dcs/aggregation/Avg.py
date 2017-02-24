from dcs.base.Atom import Atom


class Avg():
    def __init__(self,u):
        self.u = u

    def __str__(self):
        return "[AVG: " + str(self.u) + "]"

    def compile(self):
        return lambda x: x in self.vals()

    def vals(self):
        sum_val = 0
        count_val = 0
        for value in self.u.vals():
            if isinstance(value.value, str):
                return None
            sum_val += value.value
            count_val += 1

        return {Atom(sum_val/count_val)}