"""
Austin Jenchi
Intro to Game Programming - 8th Period
Squaring Things
"""

def square(base, root):
    number = base
    for x in range(1, root):
        number = number + base
    return number;

print(square(4, 4))
