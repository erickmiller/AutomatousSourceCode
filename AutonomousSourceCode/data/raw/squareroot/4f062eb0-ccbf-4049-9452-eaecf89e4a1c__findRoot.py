def squareRoot(x,power,eps):
    if x<0 and power %2 ==0:
        return None
    low = min(-1,x)
    high = max(1,x)
    ans=(low+high)/2.0
    while abs(ans**power-x) > eps:
        if ans**power <x:
            low = ans
        else:
            high = ans
        ans = (low+high)/2.0
    return ans
