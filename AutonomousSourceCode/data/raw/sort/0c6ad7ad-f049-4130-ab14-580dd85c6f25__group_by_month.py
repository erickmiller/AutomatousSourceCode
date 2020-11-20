from datetime import datetime
from itertools import groupby

def monthly(changeset):
    date = datetime.fromtimestamp(changeset.date()[0])
    return '%4d-%02d' % (date.year, date.month)

def group_by_month(changesets):
    sort = sorted(changesets, key=monthly)
    return groupby(sort, monthly)
