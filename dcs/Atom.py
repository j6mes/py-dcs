class Atom():
    def __init__(self,tokens):
        self.tokens = tokens

    def __str__(self):
        return str("[ATOM " + str(self.tokens) + "]")