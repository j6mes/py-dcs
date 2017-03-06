from dcs.TypeInfo import TypeInfo


class EntityContainer(TypeInfo):
    entities = set()

    def add(x):
        EntityContainer.entities.add(x)

    add = staticmethod(add)