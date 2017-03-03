from dateutil.parser import parse as dparse, parser

_parser_p = parser()
def is_date(string):
    try:
        dparse(string)
        components = 0
        res, _ = _parser_p._parse(string)
        if hasattr(res, "day") and res.day is not None:
            components+=1
        if hasattr(res, "month") and res.month is not None:
            components+=1
        if hasattr(res, "year") and res.year is not None:
            return True

        return components>=2
    except ValueError:
        return False


