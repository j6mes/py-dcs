class Node():
    def __init__(self,name):
        self.name = name
        self.edges = dict()

    def add_edge(self,name,edge):
        self.edges[name] = edge

    def __str__(self):
        return "NODE['" + str(self.name) + "']"