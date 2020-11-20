#write a function valuesort to sort values of a dictionary based on the key.
def valuesort(l):
    sort =sorted(l.keys())
    return [l[count] for count in sort]
print valuesort({'x':3,'y':2,'z':1})
