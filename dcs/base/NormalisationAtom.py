from dcs.base.Atom import Atom
from dcs.base.DateAtom import DateAtom
from dcs.base.Property import Property
from util.dateutils import is_date
from util.numberutils import is_number


class NormalisationAtom():
    dateprops = Property("$date")
    numberprops = Property("$number")

    def __init__(self, value):
        self.value = value
        if is_date(value):
            self.da = DateAtom(value)
            self.dateprops.add(self, self.da)

        if is_number(value):
            self.na = Atom(float(value))
            self.numberprops.add(self, self.na)

    def __str__(self):
        return "[NORMALIZE " + str(self.value) + "]"

    def allprops():
        ret = {NormalisationAtom.dateprops, NormalisationAtom.numberprops}
        ret.update(DateAtom.allprops())
        return ret


    def allatoms(self):
        ret = set()
        if hasattr(self,"da"):
            ret.update(self.da.allatoms())
        if hasattr(self,"na"):
            ret.add(self.na)
        ret.add(self)
        return ret

    allprops = staticmethod(allprops)

    def vals(self):
        return {self}


    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return other.value == self.value
        return False

    def __hash__(self):
        return self.value.__hash__()

