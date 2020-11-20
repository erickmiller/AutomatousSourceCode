'''
Created on 24.08.2014

Problem 21 of Euler Problems

"Evaluate the sum of all the amicable numbers under 10000."
https://projecteuler.net/problem=21

@author: vls
'''

import numpy

def return_all_factors(n):
    """faster way to get all factors"""
    #primes=Problem_003.primesfrom2to(n)
    square_root = int(numpy.sqrt(n))
    if square_root*square_root!=n:
        return reduce(list.__add__, 
                ([i, n//i] for i in range(1,int(square_root)+1) if n % i == 0))
    else:
        factor_list = reduce(list.__add__,([i, n//i] for i in range(1,int(square_root)) if n % i == 0))
        factor_list.append(square_root)
    return factor_list

def is_amicable_pair(n):
    """tests if it is amicable pair, and returns the pair"""
    list_factors=return_all_factors(n)
    pair = sum(list_factors)-n
    if pair==1:
        return False
    
    list_factors_pair = return_all_factors(pair)
    
    if sum(list_factors_pair)-pair!= n:
        return False
    return pair


def find_all_amicable_numbers(n):
    """finds all amicable numbers until n"""
    list_pairs=[]
    for i in range(2,n+1):
        if i not in list_pairs:
            pair = is_amicable_pair(i)
            if pair==i: #perfect number
                continue
            if pair:
                list_pairs.append(i)
                list_pairs.append(pair)
    for item in list_pairs:
        if item>n:
            list_pairs.remove(item)
    return list_pairs
            


if __name__=='__main__':
    print sum(find_all_amicable_numbers(10000))
    #print is_amicable_pair(2)
    # return_all_factors(2)
    #print numpy.sqrt(9)
    '''for i in range(8,9):
        pair = is_amicable_pair(i)
        if pair:
            print str(pair)+', '+str(i)''' 