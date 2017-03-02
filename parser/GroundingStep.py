from dcs.base.Atom import Atom
from dcs.base.Entity import Entity
from dcs.base.NormalisationAtom import NormalisationAtom
from dcs.base.Property import Property
from dcs.base.Record import Record
from dcs.base.Unary import Unary
from util.dateutils import is_date
from util.numberutils import is_number

def ground_entity(ts):
    s = " ".join(ts.tokens)
    return [Entity(s)]

def ground_atom(ts):
    s = " ".join(ts.tokens)
    return [Atom(s)]


def get_table_properties(table):
    properties = []
    for prop in table.read()['header']:
        properties.append(Property(prop))

    atoms = set()
    entities = set()

    row_id = 0
    last_row = None

    next_row = Property("$next")
    index = Property("$index")

    records = Unary("$records")

    properties.append(next_row)
    properties.append(index)

    for row in table.read()['rows']:
        r = Record("$" + str(row_id))

        index.add(r, Atom(row_id))

        col_id = 0
        for col in row:

            if len(col.strip()) == 0:
                col_id += 1
                continue

            if is_number(col) or is_date(col):
                a = NormalisationAtom(col)
                properties[col_id].add(r, a)
                atoms.add(a)
            else:
                e = Entity(col.strip())

                properties[col_id].add(r, e)
                entities.add(e)
            col_id += 1

        records.add(r)
        if last_row is not None:
            next_row.add(last_row, r)
        row_id += 1
        last_row = r

    b = set()
    u = set()
    for p in properties:
        b.add(p)
    u.add(records)

    return u, b