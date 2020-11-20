def square_root(x, epsilon=0.0001):
    ans = x/2.0

    while abs(ans**2 - x) > epsilon:
        ans = ans - (((ans**2) - x)/(2*ans))
        
    if abs(ans**2 - x ) > epsilon:
        return None
    else:
        return ans

def cube_root(x, epsilon=0.0001):
    ans = 0

    while ans**3 < abs(x):
        ans += 1

    if ans**3 != abs(x):
        return None
    else:
        return ans;