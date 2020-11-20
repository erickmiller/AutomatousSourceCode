
# Uppgift 4
[str(i) for i in range(4)]


# Uppgift 5
from math import sqrt # square root
list(filter(lambda x: sqrt(x).is_integer(), range(1000, 1200)))


# Uppgift 6
>>> def make_decrementor(n):
...     return lambda x: n - x
...
>>> f = make_decrementor(42)
>>> f(0)
42
>>> f(1)
41
>>> f(-3)
