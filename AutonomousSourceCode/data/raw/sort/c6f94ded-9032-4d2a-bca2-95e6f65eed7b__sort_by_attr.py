from django.utils.datastructures import SortedDict

    ### START SORT BY ATTR ####
def sort_by_attr(sort_object, key_name, direction=1):
    sort_list = []
    if type(sort_object) == dict:
        for key, item in sort_object.items():
            sort_list.append(item)
    else:
        if type(sort_object) == list:
            sort_list = sort_object
        else:
            for key, item in enumerate(sort_object):
                sort_list.append(item)

    sort_dict = sorted(sort_list, key=lambda k: sort_key(k, key_name, direction))

    return sort_dict


def sort_key(k, key_name, direction):
    if type(k) == dict:
        return k[key_name]*direction
    else:
        return getattr(k, key_name)*direction


### STOP SORT BY ATTR ####
