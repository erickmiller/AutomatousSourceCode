### Compute square root without using the math module. Round down.

# from __future__ import division

# def compute_sqrt(n):
#     return (str(n ** (1/2))).split(".")[0]

# print compute_sqrt(17)



### Better solution:

def compute_sqrt(n):
    
    print int(n**0.5)

print compute_sqrt(17)