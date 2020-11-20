def sort_fractions(fractions):
    fractions = sorted(fractions, key=getKey)
    return(fractions)


def getKey(fractions):
    return(fractions[0]/fractions[1])
