def front_x(words):
    a1 = []
    a2 = []
    for item in words:
        if item.startswith('x'):
            a1.append(item)
        else:
            a2.append(item)
    return(sorted(a1) + sorted(a2))


w = ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
print(front_x(w))


"""
a1.sort()
a2.sort()
return a1+a2
"""
