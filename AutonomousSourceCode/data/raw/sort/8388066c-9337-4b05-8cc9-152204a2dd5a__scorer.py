'''
Created on Nov 10, 2015

@author: st.becker
'''
import math

class Scorer(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def sort(self, setToSort, board):
        def sortKey(word):
            weight = 0
            for value in range(10):
                weight += board.countOverlapForValue(value, word) * math.pow(10, -value)
            return weight
            
        return sorted(setToSort,key=sortKey,reverse=True)