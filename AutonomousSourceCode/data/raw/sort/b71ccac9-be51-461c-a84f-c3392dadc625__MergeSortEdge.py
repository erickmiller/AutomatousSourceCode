'''
Created on 2015年4月3日

@author: Flowerfan
'''


def sort(graph):
    size = len(graph)
    if size == 1:
        return graph
    mid = int(size/2)
    lgraph = graph[:mid]
    rgraph = graph[mid:]
    sorted_graphl = sort(lgraph)
    sorted_graphr = sort(rgraph)
    newgraph =merge(sorted_graphl,sorted_graphr)
    return newgraph

def merge(lg,rg):
    lsize = len(lg)
    rsize = len(rg)
    size = lsize + rsize
    newG = []
    j = 0
    k = 0
    for i in range(size):
        if  k == rsize or (j < lsize and lg[j].weight < rg[k].weight):
            newG.append(lg[j])
            j += 1
        else:
            newG.append(rg[k])
            k += 1
    return newG 





if __name__ == '__main__':
    pass
    
