from dcs.base.Atom import Atom
from dcs.base.Property import Property
from dateutil.parser import parser, parse

_parser_p = parser()
class DateAtom():
    yearprops = Property("$date$year")
    monthprops = Property("$date$month")
    dayprops = Property("$date$day")

    def __init__(self, value):
        self.value = value
        self.atoms = set()

        res, _ = _parser_p._parse(value)
        if hasattr(res, "day") and res.day is not None:
            self.day = res.day
            a = Atom(res.day)
            self.atoms.add(a)
            self.dayprops.add(self,a)
        if hasattr(res, "month") and res.month is not None:
            self.month = res.month
            a = Atom(res.month)
            self.atoms.add(a)
            self.monthprops.add(self, a)
        if hasattr(res, "year") and res.year is not None:
            self.year = res.year
            a = Atom(res.year)
            self.atoms.add(a)
            self.yearprops.add(self, a)

    def __str__(self):
        return ("[DATE Y: " + (str(self.year) if hasattr(self, "year") else "None")
                + " M: " + (str(self.month) if hasattr(self, "month") else "None")
                + " D:" + (str(self.day) if hasattr(self, "day") else "None") + "] ")

    def allprops():
        return {DateAtom.yearprops, DateAtom.monthprops, DateAtom.dayprops}

    def allatoms(self):
        ret = set()
        ret.update(self.atoms)
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

