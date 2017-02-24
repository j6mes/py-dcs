class EntityContainer():
    entities = set()

    def add(x):
        EntityContainer.entities.add(x)

    add = staticmethod(add)