from data.table.Table import Table
from data.table.TableToGraph import ttg

if __name__ == "__main__":
    t = Table("test.tsv")
    g = ttg(t)
    print(g['Year'])