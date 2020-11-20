'''
Created on Nov 23, 2015

@author: Jonathan
'''

def sort(data):
    alphaSorted = sorted(list(set(data)))
    return sorted(alphaSorted, key = data.count, reverse = True)

if __name__ == '__main__':
    pass