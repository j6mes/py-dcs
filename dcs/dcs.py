entities = set()


class Unary():
    def __init__(self,name):
        self.name = name
        self.values = set()

    def add(self,v):
        self.values.add(v)

    def contains(self,e):
        for v in self.values:
            if e == v:
                return True
        return False

    def vals(self):
        return self.values

    def  compile(self):
        return lambda x: self.contains(x) or x in self.values


class Entity():
    def __init__(self, value):
        self.value = value
        entities.add(self)

    def vals(self):
        return {self}

    def compile(self):
        return lambda x: x == self or x == self.value

    def __str__(self):
        return "[ENTITY:" + self.value + "]"

    def __hash__(self):
        return self.value.__hash__()

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return other.value == self.value
        return False


class Record():
    def __init__(self, value):
        self.value = value
        entities.add(self)

    def vals(self):
        return {self}

    def compile(self):
        return lambda x: x == self or x == self.value

    def __str__(self):
        return "[RECORD:" + self.value + "]"

    def __hash__(self):
        return self.value.__hash__()


class Pair():
    def __init__(self,k,v):
        self.k = k
        self.v = v

    def __hash__(self):
        return self.k.__hash__() + "$$$".__hash__() + self.v.__hash__()

    def __str__(self):
        return "[PAIR: " + str(self.k) + " -> " + str(self.v) + "]"

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.k == other.k and self.v == other.v
        return False

class Property():
    def __init__(self,name):
        self.name = name
        self.pairs = set()

    def add(self,k,v):
        self.pairs.add(Pair(k,v))

    def vals(self):
        return self.pairs

    def p(self,x,y):
        return Pair(x,y) in self.pairs

    def compile(self):
        return lambda x,y: self.p(x,y)

    def __str__(self):
        return "[PROPERTY: "+str(self.name)+"]"



class Reverse():
    def __init__(self,b):
        self.b = b

    def __str__(self):
        return "R["+str(self.b)+"]"

    def vals(self):
        ret = set()
        c = self.b.compile()
        for p in self.b.vals():
            if c(p.v,p.k):
                ret.add(Pair(p.v,p.k))

        return ret

    def compile(self):
        c = self.b.compile()
        return lambda x,y: c(y,x)

class Join():
    def __init__(self,b,u):
        self.b = b
        self.u = u

    def compile(self):
        bc = self.b.compile()
        uc = self.u.compile()
        ys = self.u.vals()
        return lambda x: True in [bc(x,y) and uc(y) for y in ys]

    def vals(self):
        c = self.compile()
        ret = set()
        for x in self.b.vals():
            if c(x.k):
                ret.add(x.k)

        return ret

class Chain():
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def compile(self):
        a = self.a.compile()
        v = self.a.vals()

        b = self.b.compile()
        return lambda x,z: True in [a(x,y.v) and b(y.v,z) for y in v]

    def vals(self):
        avals = self.a.vals()
        bvals = self.b.vals()
        c = self.compile()

        ret = set()
        for a in avals:
            for b in bvals:
                if c(a.k,b.v):
                    ret.add(Pair(a.k,b.v))
        return ret

class Intersection():
    def __init__(self,u1,u2):
        self.u1 = u1
        self.u2 = u2

    def __str__(self):
        return "[INTERSECTION: " + str(self.u1) + " ^ " + str(self.u2) + "]"

    def compile(self):
        return lambda x: self.u1.compile()(x) and self.u2.compile()(x)

    def vals(self):
        avals = self.u1.vals()
        bvals = self.u2.vals()


        c = self.compile()
        ret = set()

        for val in avals.union(bvals):
            if c(val):
                ret.add(val)
        return ret


class Union():
    def __init__(self,u1,u2):
        self.u1 = u1
        self.u2 = u2

    def __str__(self):
        return "[UNION: " + str(self.u1) + " ^ " + str(self.u2) + "]"

    def compile(self):
        return lambda x: self.u1.compile()(x) or self.u2.compile()(x)

    def vals(self):
        avals = self.u1.vals()
        bvals = self.u2.vals()
        c = self.compile()
        ret = set()

        for val in avals.union(bvals):
            if c(val):
                ret.add(val)
        return ret

class Negate():
    def __init__(self, u):
        self.u = u

    def compile(self):
        return lambda x: not self.u.compile()(x)

    def vals(self):
        c = self.compile()
        ret = set()

        for v in entities:
            if(c(v)):
                ret.add(v)
        return ret


class Atom():
    def __init__(self, v):
        if isinstance(v,Atom):
            v = v.value
        self.value = v

    def vals(self):
        return {self}

    def compile(self):
        return lambda x: x == self or x == self.value

    def __str__(self):
        return "[ATOM:" + str(self.value) + "]"

    def __hash__(self):
        return self.value.__hash__()

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return other.value == self.value
        return False



class Min():
    def __init__(self,u):
        self.u = u

    def compile(self):
        current_max = float("inf")
        for v in self.u.vals():
            if v.value < current_max:
                current_max = v.value

        return lambda: Atom(current_max)


    def __str__(self):
        return "[MIN: " + str(self.u) + "]"

class Max():
    def __init__(self,u):
        self.u = u

    def __str__(self):
        return "[MAX: " + str(self.u) + "]"

    def compile(self):
        current_max = float("-inf")
        for v in self.u.vals():
            if v.value > current_max:
                current_max = v.value

        return lambda: Atom(current_max)

class Count():
    def __init__(self,u):
        self.u = u

    def __str__(self):
        return "[COUNT: " + str(self.u) + "]"

    def compile(self):
        return lambda: Atom(len(self.u.vals()))

class Sum():
        def __init__(self, u):
            self.u = u

        def __str__(self):
            return "[SUM: " + str(self.u) + "]"

        def compile(self):
            sum_val = 0
            for value in self.u.vals():
                sum_val += value.value

            return lambda: Atom(sum_val)

class Avg():
    def __init__(self,u):
        self.u = u

    def __str__(self):
        return "[AVG: " + str(self.u) + "]"

    def compile(self):
        sum_val = 0
        count_val = 0
        for value in self.u.vals():
            sum_val += value.value
            count_val += 1

        return lambda: Atom(sum_val/count_val)



class ArgMax():
    def __init__(self,u,b):
        self.u = u
        self.b = b

    def __str__(self):
        return "[ARGMAX: " + str(self.u) + " " + str(self.b) + "]"

    def compile(self):
        bc = self.b.compile()

        current_max = float("-inf")
        best_v = None
        for uv in self.u.vals():
            for bv in self.b.vals():
                m = bc(uv,bv.v)
                if m and bv.v.value > current_max:
                    current_max = bv.v.value
                    best_v = uv
        return lambda: best_v

class ArgMin():
    def __init__(self,u,b):
        self.u = u
        self.b = b

    def __str__(self):
        return "[ARGMIN: " + str(self.u) + " " + str(self.b) + "]"

    def compile(self):
        bc = self.b.compile()

        current_max = float("inf")
        best_v = None
        for uv in self.u.vals():
            for bv in self.b.vals():
                m = bc(uv,bv.v)
                if m and bv.v.value < current_max:
                    current_max = bv.v.value
                    best_v = uv
        return lambda: best_v



if __name__ == "__main__":
    seattle = Entity("Seattle")
    nyc = Entity("New York")

    john = Entity("John")
    mary = Entity("Mary")
    bob = Entity("Bob")
    sue = Entity("Sue")

    population = Property("Population")
    population.add(seattle, Atom(50000))
    population.add(nyc,     Atom(100000))

    cities = Union(nyc,seattle)

    pob = Property("PlaceOfBirth")
    pob.add(john,seattle)
    pob.add(mary,nyc)
    pob.add(bob,nyc)
    pob.add(sue,seattle)

    childrenOf = Property("ChildOf")
    childrenOf.add(mary,john)
    childrenOf.add(john,bob)

    prof = Property("Profession")
    doctor = Entity("Doctor")
    scientist = Entity("Scientist")

    prof.add(john,doctor)
    prof.add(mary,doctor)
    prof.add(bob,scientist)
    prof.add(sue,scientist)

    #is seattle seattle?
    print(seattle.compile()("Seattle"))
    print(seattle.compile()(seattle))

    #was john born in seattle?
    print(pob.compile()(john,seattle))

    #was john born in nyc
    print(pob.compile()(john,nyc))

    #list people born in seattle
    print([str(v) for v in Join(pob,seattle).vals()])

    #Is mary a parent of someone born in seattle?
    print(Chain(childrenOf,pob).compile()(mary,seattle))

    #List of parents who had children born in seattle
    print([str(v) for v in Join(Chain(childrenOf,pob),seattle).vals()])
    print([str(v) for v in Join(Chain(childrenOf,pob),nyc).vals()])

    #Is John a Doctor and born in Seattle?
    print(Intersection(Join(prof,doctor),Join(pob,seattle)).compile()(john))

    #print who is both a doctor and born in seattle
    print([str(v) for v in Intersection(Join(prof,doctor),Join(pob,seattle)).vals()])

    #print who is either a doctor or born in seattle
    print([str(v) for v in Union(Join(prof,doctor),Join(pob,seattle)).vals()])

    #print who is both not a  doctor and born in seattle
    print([str(v) for v in Intersection(Join(prof,doctor),Negate(Join(pob,seattle))).vals()]) #mary
    print([str(v) for v in Intersection(Negate(Join(prof,doctor)),Join(pob,seattle)).vals()]) #sue

    print(Max(Union(Atom(10),Atom(20))).compile()())
    print(Min(Union(Atom(10),Atom(20))).compile()())

    print(Count(Intersection(Negate(Join(prof,doctor)),Negate(Join(pob,seattle)))).compile()()) #5

    print(ArgMax(cities,population).compile()())
    print(ArgMin(cities,population).compile()())


    print(Avg(Union(Atom(10),Atom(20))).compile()())
    print(Sum(Union(Atom(10),Atom(20))).compile()())
