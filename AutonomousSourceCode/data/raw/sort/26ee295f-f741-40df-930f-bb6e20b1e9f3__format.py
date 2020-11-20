from datetime import datetime
import calendar
from collections import OrderedDict

def by_date(changes):
    sorted = OrderedDict()
    for repo in changes:
        for commit in changes[repo]:
            _, _, date, _, _ = commit
            epoch = calendar.timegm(datetime.strptime(date, '%Y-%m-%d').utctimetuple())
            if epoch in sorted:
                sorted[epoch] += commit
            else:
                sorted[epoch] = [commit]
    return sorted

def by_author(changes):
    sorted = OrderedDict()
    for repo in changes:
        for commit in changes[repo]:
            _, author, _, _, _ = commit
            if author in sorted:
                sorted[author] += commit
            else:
                sorted[author] = [commit]
    return sorted

def by_directory(changes):
    sorted = OrderedDict()
    for repo in changes:
        if repo in sorted:
            sorted[repo] = changes[repo]
        else:
            sorted[repo] = changes[repo]
    return sorted

SORT = {
    'date': by_date,
    'author': by_author,
    'directory': by_directory
}
