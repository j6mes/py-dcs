class Entity():
    def __init__(self,tokens):
        self.tokens = tokens

    def __str__(self):
        return str("[ENTITY " + str(self.tokens) + "]")