def cardSort(values):
    sortedList=[]
    for i in range(min(values),max(values)+1):
        if i in values:
            for card in values:
                if card==i:
                    sortedList.append(card)
                    del card
                    
    return sortedList
