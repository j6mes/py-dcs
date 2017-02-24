from dcs.aggregation.Avg import Avg
from dcs.aggregation.Count import Count
from dcs.aggregation.Max import Max
from dcs.aggregation.Min import Min
from dcs.aggregation.Sum import Sum
from dcs.arithmetic.Add import Add
from dcs.base.Atom import Atom
from dcs.base.Entity import Entity
from dcs.base.Property import Property
from dcs.comparitor.GreaterThan import GreaterThan
from dcs.relation.Chain import Chain
from dcs.relation.Intersection import Intersection
from dcs.relation.Join import Join
from dcs.relation.Negate import Negate
from dcs.relation.Reverse import Reverse
from dcs.relation.Union import Union
from dcs.superlative.ArgMax import ArgMax
from dcs.superlative.ArgMin import ArgMin

if __name__ == "__main__":
    seattle = Entity("Seattle")
    nyc = Entity("New York")
    nyc2 = Entity("New York2")

    john = Entity("John")
    mary = Entity("Mary")
    bob = Entity("Bob")
    sue = Entity("Sue")

    population = Property("Population")
    population.add(seattle, Atom(50000))
    population.add(nyc,     Atom(100000))

    population.add(nyc,     Atom(600000))
    population.add(nyc2,     Atom(600000))
    cities = Union(nyc2, Union(nyc,seattle))

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

    print(Max(Union(Atom(10),Atom(20))).vals())
    print(Min(Union(Atom(10),Atom(20))).vals())

    print(Count(Intersection(Negate(Join(prof,doctor)),Negate(Join(pob,seattle)))).vals()) #5

    print([str(a) for a in ArgMax(cities,population).vals()])
    print([str(a) for a in ArgMin(cities,population).vals()])


    print(Avg(Union(Atom(10),Atom(20))).vals())
    print(Sum(Union(Atom(10),Atom(20))).vals())


    print([str(a) for a in Join(population,GreaterThan(Atom(500000))).vals()])

    print([str(a) for a in Join(Reverse(population),nyc).vals()])
    print([str(a) for a in Add(Atom(10),Join(Reverse(population),nyc)).vals()])
