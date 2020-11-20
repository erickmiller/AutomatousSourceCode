# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 23:50:11 EDT 2015
@author: aaditya prakash
"""

import re
from time import clock

problem_number = '206'
problem_statement = """
Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit.
"""

def concealed_square():
    """ solves problem 206"""
    pat = re.compile(r'1\d2\d3\d4\d5\d6\d7\d8\d9\d0')
    
    #smallest_integer possible given the requirement = 1020304050403020100 
    start = 1010101010 # square root of smallest integer 
    while True:
        if len(pat.findall(str(start**2))): return start
        start += 10


timeStart = clock()
print(concealed_square())
print('Time (sec):' + str(clock() - timeStart))
answer = '1389019170'



