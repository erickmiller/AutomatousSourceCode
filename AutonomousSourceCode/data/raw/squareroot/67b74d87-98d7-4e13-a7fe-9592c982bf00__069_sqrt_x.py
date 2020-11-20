# Implement int sqrt(int x).

# Compute and return the square root of x.


class Solution:
    # @param {integer} x
    # @return {integer}
    def mySqrt(self, x):
        
        # Just an initial guess
        n = max(1, 10*(len(str(x))/2))

        # Newton iteration
        while not (pow(int(n), 2) <= x and x < pow(int(n)+1, 2)):
            n = (n + x/n)/2

        return int(n)