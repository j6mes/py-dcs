import unicodedata

from dateutil.parser import parse as dparse
from dcs.dcs import *

from training import *

t = TrainingExample("Greece last held its Summer Olympics in 2005?", None, None)


def is_date(string):
    try:
        dparse(string)
        return True
    except ValueError:
        return False


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


table = Table("test.tsv")

properties = []
for prop in table.read()['header']:
    properties.append(Property(prop))

atoms = set()
entities = set()

row_id = 0
last_row = None
next_row = Property("$next")
properties.append(next_row)
index = Property("$index")
records = Unary("$records")
grr = None
for row in table.read()['rows']:
    r = Record("$" + str(row_id))

    index.add(r, Atom(row_id))

    col_id = 0
    for col in row:

        if len(col.strip()) == 0:
            col_id += 1
            continue

        if is_number(col) or is_date(col):
            a = Atom(float(col))
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

actions = [(ground_entity, t.nes),
           (ground_atom, t.nums),
           ]

u = set()
b = set()

for action, data in actions:
    for datum in data:
        u.update(action(datum))

for p in properties:
    b.add(p)

u.add(records)


def AAtransition(u, b):
    u_actions = [(act_union, cross_product(u, u)),
                 (act_intersection, cross_product(u, u)),
                 (act_agg, u)
                 ]

    bu_actions = [(act_join, cross_product(b, u)),
                  (act_sup, cross_product(u, b))
                  ]

    b_actions = [(act_reverse, b)]

    print("Starting with " + str(len(u)) + " unaries")
    print("Starting with " + str(len(b)) + " binaries")

    u_next = set()
    b_next = set()

    for action, data in u_actions:
        for datum in data:
            for a in action(datum):
                u_next.add((datum, a))

    for action, data in bu_actions:
        for datum in data:
            for a in action(datum):
                u_next.add((datum, a))

    for action, data in b_actions:
        for datum in data:
            b_next.update(action(datum))

    print("Generated " + str(len(u_next)) + " unaries")
    print("Generated " + str(len(b_next)) + " binaries")

    u_ret = set()
    b_ret = set()

    u_ret.update(u)
    b_ret.update(b)

    pruned = 0
    for d, a in u_next:
        v = a.vals()
        if v is None:
            pruned += 1
            continue
        elif len(v) == 0:
            pruned += 1
            continue

        print(a)
        print([str(aa) for aa in v])

        if hasattr(d, "__iter__"):
            if hasattr(v, "__iter__"):
                if set(d) == set(v):
                    pruned += 1
                    continue
        u_ret.add(a)

    print("Pruned " + str(pruned) + " unaries")

    pruned = 0
    for a in b_next:
        v = a.vals()
        if v is None:
            pruned += 1
            continue
        elif len(v) == 0:
            pruned += 1
            continue
        b_ret.add(a)

    print("Pruned " + str(pruned) + " binaries")
    return u_ret, b_ret


u_, b_ = u, b

for i in range(3):
    print("Iteration " + str(i))
    u_, b_ = transition(u_, b_)
    print("")

