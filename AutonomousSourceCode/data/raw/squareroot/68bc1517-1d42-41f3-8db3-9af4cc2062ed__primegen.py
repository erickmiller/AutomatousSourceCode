
def primesByMaxValue(MAX):
    
    primes = [2,3,5,7,11,13,17,19,23,29,31,37]
    root_index = 3
    root = 7
    square = 49
    r = range(1,root_index)
    
    for n in range(41,MAX,2):
        
        if square <= n:
            r.append(root_index)
            root_index += 1
            root = primes[root_index]
            square = root * root
        
        for i in r:
            p = primes[i]
            if n % p == 0:
                break
        else:
            primes.append(n)
    
    return primes

