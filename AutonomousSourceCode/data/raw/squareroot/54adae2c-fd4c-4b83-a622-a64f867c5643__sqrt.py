def sqrt(x):
    """ Calculate the square root of a perfect square"""
    if x >= 0:
        ans = 0
        while ans * ans < x:
            ans += 1
        if ans * ans == x:
            return ans
        else:
            print(x, "is not a perfect square")
            return None
    else:
        print(x, "is a negative number")
        return None

for i in range (-10, 11):
    x = sqrt(i)
    if x != None:
        print("Square root of", i, "is", x)
