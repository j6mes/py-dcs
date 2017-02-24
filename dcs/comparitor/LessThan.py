from dcs.relation.support.NonGenerator import NonGenerator


class LessThan():
    def __init__(self, a):
        self.a = a

    def __str__(self):
        return "[LT " + str(self.a) + "]"

    def compile(self):
        return lambda x: x.value < self.a.value

    def vals(self):
        return {NonGenerator()}