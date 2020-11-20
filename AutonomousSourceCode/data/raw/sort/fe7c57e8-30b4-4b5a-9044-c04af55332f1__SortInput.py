


def sortOnMedia(data):
    sortedData = sorted(data, key=lambda x: x.getMedia())
    return sortedData

def sortOnCompany(data):
    sortedData = sorted(data, key=lambda x: x.getCompany())
    return sortedData

def sortOnCategory(data):
    sortedData = sorted(data, key=lambda x: x.getCategory())
    return sortedData
    
def sortOnCategorySize(data):
    """
    Assume that the data input is a list sorted by category
    """
    categories = []
    for i in data:
        if len(categories) == 0:
            categories.append([i])
        else:
            if i.getCategory() == categories[-1][-1].getCategory():
                categories[-1].append(i)
            else:
                categories.append([i])
    
    sortedCategories = sorted(categories, key=lambda x: len(x), reverse=True)
    sortedData = []
    for category in sortedCategories:
        for i in category:
            sortedData.append(i)
    return sortedData

def sortInput(data):
    data = sortOnCompany(data)
    data = sortOnMedia(data)
    data = sortOnCategory(data)
    data = sortOnCategorySize(data)
    return data

