def sort_it(list_, n):
    lst2 = sorted( [ ( l.strip()[n-1], l ) for l in list_.split(',') ] )
    lst3 = [ x[1] for x in lst2 ]
    return ','.join(lst3)



lst = 'bill, bell, ball, bull'
n = 2
print sort_it(lst,n)
