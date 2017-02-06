import csv

def transpose(l):
    return list(map(list, zip(*l)))

class Table():
    def __init__(self, filename, base="data"):
        self.header = []
        self.rows = []
        self.filename = filename
        self.base = base
        self.done = False
    def read(self):
        if not self.done:
            header_read = False
            filename = self.filename.replace(".csv", ".tsv")
            with open(self.base + "/" + filename, "r", encoding='utf-8') as table:
                has_header = csv.Sniffer().has_header(table.readline())
                table.seek(0)

                for line in csv.reader(table, delimiter="\t"):
                    if has_header and not header_read:
                        self.header = line
                        header_read = True
                    else:
                        self.rows.append(line)
            self.done = True
        return {"header": self.header, "rows": self.rows}


if __name__ == "__main__":
    t = Table("test.tsv")
    print(t.read())