import operator

def sort_dict_by_value(thedict):
    return sorted(thedict.items(), key=operator.itemgetter(1),reverse=True)

def get_top_n_from_dict(thedict,n):
    sorteditems = sort_dict_by_value(thedict)
    return sorteditems[0:n]
