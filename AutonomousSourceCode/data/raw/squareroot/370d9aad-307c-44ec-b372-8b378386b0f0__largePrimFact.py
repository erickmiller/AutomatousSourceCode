def factor(n):
        if n == 1: return [1]
        i = 2#Next lowest Prime
        limit = n**0.5#Limit is the square root, ie: perfect square
        while i <= limit:
                if n % i == 0:# Is the value divisible by our "prime"
                        ret = factor(n/i)
                        ret.append(i)
                        return ret
                i += 1

        return [n]


print factor(35)
print factor(600851475143)
