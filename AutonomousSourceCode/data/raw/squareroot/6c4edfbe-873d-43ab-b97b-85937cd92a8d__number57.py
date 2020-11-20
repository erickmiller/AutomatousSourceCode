"""
David Schonberger
Project Euler - problem 57
Square root convergents
"""

def addn(l, n):
    return [l[0] + n * l[1], l[1]]
    
def flip(l):
    return [l[1], l[0]]

upper = 1000
curr_lst = [1,2]
bigger_numerator_count = 0
for i in range(2 , upper + 1):
    curr_lst = flip(addn(curr_lst,2))
    curr_conv = addn(curr_lst,1)
    if(len(str(curr_conv[0])) > len(str(curr_conv[1]))):
        bigger_numerator_count += 1
        
print "in first ", upper, "convergents", bigger_numerator_count, "have bigger numerator"
