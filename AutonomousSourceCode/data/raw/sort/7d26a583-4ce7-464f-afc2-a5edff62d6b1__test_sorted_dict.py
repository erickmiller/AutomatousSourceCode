import operator

d = {
     "and": 1,
     "the": 3,
     "in": 2,
     "was": 2
}


def sort_dict_by_values(_dict):
     sorted_dict = sorted(_dict.items(), key=operator.itemgetter(1), reverse=True)
     return sorted_dict


result = sort_dict_by_values(d)
print(result)