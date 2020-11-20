import operator, math

class memoize:
    def __init__(self, f):
        self.f = f
        self.memo = {}
    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]

@memoize
def factorial(n):
    return reduce(operator.mul, range(2,n+1), 1)

def choose(n, k):
    return reduce(operator.mul, range(n-k+1, n+1), 1) / factorial(k)

def triangular(p):
    return (p * (p+1)) / 2

def num_divisors(p):
    num = 0
    square_root = int(math.ceil(math.sqrt(p)))
    for x in xrange(1, square_root):
        if p % x == 0:
            num += 2
    if square_root * square_root == p:
        num += 1
    return num

def divisors(p):
    div = set()
    square_root = int(math.ceil(math.sqrt(p)))
    for x in xrange(1, square_root+1):
        if p % x == 0:
            div.add(p/x)
            div.add(x)
    if p > 1: div.remove(p)
    return div

def word_score(word):
    return sum( (ord(x) - ord('A')+1) for x in word)

def get_primes(limit):
    numbers = [True] * limit
    numbers[0] = False
    numbers[1] = False

    for sieve in range(2, limit):
        if not numbers[sieve]:
            # find next prime
            continue

        yield sieve

        for x in range(sieve+sieve, limit, sieve):
            numbers[x] = False

_primes = set()
_non_primes = set()
_prime_limit = 1000000
def is_prime(x):
    if len(_primes) == 0:
        _primes.update(get_primes(_prime_limit))
    if x in _primes:
        return True
    if x in _non_primes or x < _prime_limit:
        return False

    if x % 3 == 0 or x % 2 == 0:
        _non_primes.add(x)
        return False

    for d in range(6, int(math.sqrt(x)), 6):
        if x % (d+1) == 0 or x % (d-1) == 0:
            _non_primes.add(x)
            return False

    _primes.add(x)
    return True

def gcd(a, b):
    if a > b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a

def lcd(a, b):
    return a * b / gcd(a, b)

def permute(seq, pred=cmp):
    """Like C++ std::next_permutation() but implemented as
    generator. Yields copies of seq."""

    def reverse(seq, start, end):
        # seq = seq[:start] + reversed(seq[start:end]) + \
        #       seq[end:]
        end -= 1
        if end <= start:
            return
        while True:
            seq[start], seq[end] = seq[end], seq[start]
            if start == end or start+1 == end:
                return
            start += 1
            end -= 1

    if not seq:
        raise StopIteration

    try:
        seq[0]
    except TypeError:
        raise TypeError("seq must allow random access.")

    first = 0
    last = len(seq)
    seq = seq[:]

    # Yield input sequence as the STL version is often
    # used inside do {} while.
    yield seq

    if last == 1:
        raise StopIteration

    while True:
        next = last - 1

        while True:
            # Step 1.
            next1 = next
            next -= 1

            if pred(seq[next], seq[next1]) < 0:
                # Step 2.
                mid = last - 1
                while not (pred(seq[next], seq[mid]) < 0):
                    mid -= 1
                seq[next], seq[mid] = seq[mid], seq[next]

                # Step 3.
                reverse(seq, next1, last)

                # Change to yield references to get rid of
                # (at worst) |seq|! copy operations.
                yield seq[:]
                break
            if next == first:
                raise StopIteration
    raise StopIteration

def is_square(n):
    sq = int(math.sqrt(n))
    return sq * sq == n

_fprimes = [2]

@memoize
def factors(n, first):
    global _fprimes
    if _fprimes[-1] < n:
        _fprimes = list(get_primes(n*2))

    factors = []
    for p in _fprimes:
        while n % p == 0:
            factors.append(p)
            n /= p
        if n == 1:
            break
    return factors

def zipWith(f, a, b):
    return map(f, zip(a,b))

def compose(f, g):
    def fg(*a, **kw):
        return f(g(*a, **kw))
    return fg

def trace(f):
    def inner(*a, **kw):
        print '> calling', f.func_name, 'with ', a, kw
        r = f(*a, **kw)
        print '> returning', f.func_name, r
        return r
    return inner
