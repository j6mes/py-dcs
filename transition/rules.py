from dcs.dcs import *

def ground_entity(ts):
    s = " ".join(ts.tokens)
    return [Entity(s)]

def ground_atom(ts):
    s = " ".join(ts.tokens)
    return [Atom(s)]

def cross_product(list1, list2):
    return [(a, b) for a in list1 for b in list2]


def act_union(bits):
    return [Union(bits[0], bits[1])]


def act_intersection(bits):
    return [Intersection(bits[0], bits[1])]


def act_join(bits):
    return [Join(bits[0], bits[1])]


def act_agg(u):
    if isinstance(u, Atom):
        return [Min(u), Max(u), Count(u)]
    return [Count(u)]


def act_sup(bits):
    u = bits[0]
    b = bits[1]
    return [ArgMin(u, b), ArgMax(u, b)]


def act_reverse(b):
    if isinstance(b, Reverse):
        return [b.b]
    return [Reverse(b)]