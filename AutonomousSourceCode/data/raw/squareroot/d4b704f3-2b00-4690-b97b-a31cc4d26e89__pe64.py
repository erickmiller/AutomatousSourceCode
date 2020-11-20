import math
import gmpy

def get_period(root):
    history = []
    current_pair = Fraction(root, 0, 0, 1).disjoin_invert()
    history.append(current_pair)
    while True:
        # print current_pair
        current_pair = current_pair[1].rationalize().disjoin_invert()
        if current_pair in history:
            return len(history) - history.index(current_pair)
        history.append(current_pair)

def count_odd_periods(max_root):
    count = 0
    for root in xrange(2, max_root + 1):
        if gmpy.is_square(root):
            continue
        period = get_period(root)
        if period % 2 == 1:
            count += 1
    return count

class Fraction(object):
    def __init__(self, num_root, num_int, denom_root, denom_int):
        self.num_root = num_root
        self.num_int = num_int
        self.denom_root = denom_root
        self.denom_int = denom_int
    def rationalize(self):
        assert(self.denom_root != 0)
        assert(self.num_root == 0)
        new_denom_root = 0
        new_denom_int = (self.denom_root - self.denom_int ** 2) / self.num_int
        new_num_root = self.denom_root
        new_num_int = -self.denom_int
        return Fraction(new_num_root, new_num_int, new_denom_root, new_denom_int)
    def disjoin(self):
        assert(self.denom_root == 0)
        assert(self.num_root != 0)
        int_part = int((math.sqrt(self.num_root) + self.num_int) / self.denom_int)
        frac_part = Fraction(self.num_root, self.num_int - int_part * self.denom_int, 0, self.denom_int)
        return (int_part, frac_part)
    def invert(self):
        return Fraction(self.denom_root, self.denom_int, self.num_root, self.num_int)
    def disjoin_invert(self):
        int_part, frac_part = self.disjoin()
        return (int_part, frac_part.invert())
    def __eq__(self, other):
        return (
            self.num_root == other.num_root
            and self.num_int == other.num_int
            and self.denom_root == other.denom_root
            and self.denom_int == other.denom_int)
    def __str__(self):
        return "(%d, %d, %d, %d)" % (self.num_root, self.num_int, self.denom_root, self.denom_int)
    def __repr__(self):
        return str(self)

if __name__ == '__main__':
    print count_odd_periods(13)
    print count_odd_periods(10000)
