import csv

from graph.Node import Node
from graph.Property import GProperty
from table.Table import Table


def ttg(table):
    nodes = dict()

    idx = 0
    t = table.read()
    prev = None
    for row in t['rows']:
        node = Node("$"+str(idx))
        nodes[node.name] = node
        node.add_edge("$Index",GProperty(idx))
        if prev is not None:
            prev.add_edge("$Next",prev)

        pos = 0
        for cell in row:
            if len(cell.strip()) > 0:
                prop = GProperty(cell)
                node.add_edge(t['header'][pos],prop)
            pos += 1
        idx += 1
        prev = node

    return nodes['$0']



if __name__ == "__main__":
    t = Table("test.tsv")
    g = ttg(t)
    print(g['Year'])