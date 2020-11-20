'''
Created on Jun 22, 2013

@author: Yubin Bai

All rights reserved.
'''
from collections import deque


def topoSort(graph):
    def topoVisit(u):
        visited[u] = 1
        for v in graph[u]:
            if (visited[v] == 0):
                topoVisit(v)
        topoSorted.appendleft(u)  # this is the only change
    visited = {}
    for v in graph:
        visited[v] = 0
    topoSorted = deque()
    for v in graph:
        if visited[v] == 0:
            topoVisit(v)
    return topoSorted

if __name__ == '__main__':
    graph = {0: [1], 1: [3], 2: [1], 3: [2, 4], 4: [5], 5: [7], 6: [4], 7: [6]}
    print topoSort(graph)
