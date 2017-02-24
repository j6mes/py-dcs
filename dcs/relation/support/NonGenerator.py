class NonGenerator():
    def __eq__(self, other):
        return isinstance(other, NonGenerator)

    def __hash__(self):
        return "$$NG$$".__hash__()