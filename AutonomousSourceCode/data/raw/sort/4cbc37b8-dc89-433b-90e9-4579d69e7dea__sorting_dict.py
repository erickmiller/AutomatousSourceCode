"""from operator import itemgetter
def sort_dict(d):
    des_ord=sorted(d.iteritems(), key=itemgetter(1), reverse=True)
    return des_ord
    """

def sort_dict(d):
    return sorted(d.items(), key=lambda x: x[1], reverse=True)

#d.items=list of tuples
#itemgetter is like iterate the items in list

a=sort_dict({1:5,3:10,2:2,6:3,8:8})
print a
