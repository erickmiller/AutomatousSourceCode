# Find square root of a number
# Apply the concept of a BST

def square_root(n, precision):
    low = 0.0
    high = n
    mid = (low+high)/2.0
    # precision is the +/- error allowed in our answer
    while (abs(mid*mid-n) > precision):
        if (mid*mid) < n:
            low = mid
        elif (mid*mid) > n:
            high = mid
        mid = (low+high)/2.0

    return mid
    
print square_root(1.0, 0.00001)
print square_root(3.0, 0.00001)
print square_root(4.0, 0.00001)
print square_root(49.0, 0.00001)
