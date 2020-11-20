'''
Created on 16.08.2014


Problem 12 of Euler Problems

"What is the value of the first triangle number to have over five hundred divisors"
https://projecteuler.net/problem=12

@author: vls
'''
import Problem_001
import Problem_003
import numpy

def return_all_factors(n):
    """faster way to get all factors"""
    #primes=Problem_003.primesfrom2to(n)
    square_root = int(numpy.sqrt(n))
    if square_root*square_root!=n:
        return reduce(list.__add__, 
                ([i, n//i] for i in range(1,int(square_root)) if n % i == 0))
    else:
        factor_list = reduce(list.__add__,([i, n//i] for i in range(1,int(square_root)) if n % i == 0))
        factor_list.append(square_root)
        return factor_list

def do_problem_12():
    """method is too slow! -after several hours no result: up to triangle number: 63850650"""        
    number_of_factors = 0
    n=11300
    
    while number_of_factors<=500:
        n=n+1
        number_of_factors=len(Problem_003.list_factors(Problem_001.sum_of_all_whole_numbers(n)))
        if n%100==0:
            print str(Problem_001.sum_of_all_whole_numbers(n))+':'+str(number_of_factors)
        
    print '*****'
    print str(Problem_001.sum_of_all_whole_numbers(n))+':'+str(number_of_factors)
    
def get_number_of_factors(n):
    square_root = numpy.sqrt(n)
    number_of_factors=0
    if n%square_root==0:
        number_of_factors=-1
   
    for i in range(1,int(square_root)+1):
        if n%i ==0:
            number_of_factors+=2
    return number_of_factors

def do_problem_12_try2(max_factors):
    """method is too slow! -after several hours no result: up to triangle number: 63850650"""        
    number_of_factors = 0
    n=0
    
    while number_of_factors<=max_factors:
        n=n+1
        number_of_factors=get_number_of_factors(Problem_001.sum_of_all_whole_numbers(n))

    dictionary ={}

    dictionary[Problem_001.sum_of_all_whole_numbers(n)] = return_all_factors(Problem_001.sum_of_all_whole_numbers(n))
    
    return dictionary

    
if __name__ == '__main__':
    print do_problem_12_try2(500)