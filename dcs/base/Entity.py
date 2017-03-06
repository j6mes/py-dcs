from dcs.TypeInfo import TypeInfo
from dcs.extra.EntityContainer import EntityContainer


class Entity(TypeInfo):
    def __init__(self, value):
        self.value = value
        EntityContainer.add(self)

    def vals(self):
        return {self}

    def compile(self):
        return lambda x: x == self or x == self.value

    def __str__(self):
        return "[ENTITY:" + self.value + "]"

    def __hash__(self):
        return self.value.__hash__()

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return other.value == self.value
        return False

