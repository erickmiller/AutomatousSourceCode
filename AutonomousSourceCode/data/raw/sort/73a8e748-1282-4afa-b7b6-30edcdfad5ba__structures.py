'''
Created on 24/11/2012

@author: Pavel
'''
#http://stackoverflow.com/questions/613183/python-sort-a-dictionary-by-value
def sort_dict_value(dicto, decrease = True):
    import operator
    return  sorted(dicto.iteritems(), key=operator.itemgetter(1),reverse=decrease)
    
def sort_dict_key(dicto, decrease = True):
    import operator
    return  sorted(dicto.iteritems(), key=operator.itemgetter(0), reverse = decrease)
    