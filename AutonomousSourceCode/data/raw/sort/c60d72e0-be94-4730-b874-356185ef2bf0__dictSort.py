def sortedDictValues1(adict): 
    items = adict.items() 
    items.sort() 
    return items
    #return [value  for key, value  in items]

def sortedDictValues2(adict): 
    keys = adict.keys() 
    keys.sort() 
    
    return [adict[key] for key in keys]

def sortedDictValues3(adict): 
    keys = adict.keys() 
    keys.sort() 
    return map(adict.get,keys )


student = {'name':'Tom','age':25,'score':88}
result = sortedDictValues3(student)
print result
