fruits = ['banana', 'apple', 'fig', 'raspberry', 'aam','strawberry', 'cherry']

def mycomp(var):
    return ord(var[1])

print(sorted(fruits))

#can pass any function to 'key'. Its bascially a comparator from Java.
#also, sorted seems to do a 'stable sort'.
print(sorted(fruits, key=mycomp))
