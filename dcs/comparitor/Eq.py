from dcs.relation.support.NonGenerator import NonGenerator


class Eq():
    def __init__(self, a):
        self.a = a

    def __str__(self):
        return "[EQ " + str(self.a) + "]"

    def compile(self):
        return lambda x: x.value == self.a.value

    def vals(self):
        return {NonGenerator()}