from dateutil.parser import parse as dparse


def is_date(string):
    try:
        dparse(string)
        return True
    except ValueError:
        return False


