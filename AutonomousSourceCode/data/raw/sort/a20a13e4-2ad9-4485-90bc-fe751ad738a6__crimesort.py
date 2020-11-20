#campbell is great and wrote all of the fancy math algorithims

def sortByCrime(atms):
    sortedAtms = sorted(atms, key=lambda atm: atm['crimes'])
    print sortedAtms
    return sortedAtms