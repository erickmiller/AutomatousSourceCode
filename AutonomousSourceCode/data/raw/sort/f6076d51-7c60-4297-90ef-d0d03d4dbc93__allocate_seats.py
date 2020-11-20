# from collections import OrderedDict
# import operator


from collections import OrderedDict
import operator


def sort_constituencies_by_party_popularity(constituencies, party):
    sorted_constituencies = OrderedDict(sorted(constituencies.iteritems(),
                                               key=lambda x: x[1][party]))
    sorted_constituencies = reversed(sorted_constituencies)
    return sorted_constituencies


def sort_parties_by_seats(party_seats):
    sorted_seats = sorted(party_seats.items(),
                          key=operator.itemgetter(1),
                          reverse=True)
    return sorted_seats


def allocate_seats(constit, party_seats):
    """
    For the given dict of constituencies and the votes per party they have,
    and the given dictionary of seats per party, allocate an MP/seat to each
    constituency on a first-come-first-served basis, ranked by popularity.
    """
    constituencies = dict(constit)
    constituency_seats = {}
    for constituency, _ in constituencies.items():
        constituency_seats[constituency] = ''
    sorted_seats = sort_parties_by_seats(party_seats)
    for party, seats in sorted_seats:
        allocated = 0
        sorted_constituencies = sort_constituencies_by_party_popularity(
            constituencies, party)
        for constituency in sorted_constituencies:
            if allocated == seats:
                break
            constituency_seats[constituency] = party
            constituencies.pop(constituency)
            allocated += 1
    return constituency_seats
