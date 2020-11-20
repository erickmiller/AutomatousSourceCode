def square_root_continuous(x, epsilon=.01):
    step = epsilon**2
    num_guesses = 0
    ans = 0.0
    while abs(ans**2 - x) >= epsilon and ans <= x:
        ans += step
        num_guesses += 1
    print('Tried ' + str(num_guesses) + ' times')
    
    return(ans)

def square_root_bisect(x, epsilon=.01):
    num_guesses = 0
    low = 0.0
    high = float(x)
    ans = (low + high) / 2.0 
    while abs(ans**2 - x) >= epsilon and ans <= x:
        num_guesses += 1
        if ans**2 > x:
            high = ans
        else:
            low = ans
        ans = (low + high) / 2.0
    print('Tried ' + str(num_guesses) + ' times')
    
    return(ans)

n = 14234
print(square_root_continuous(n, .01))
print(square_root_bisect(n, .000000001))