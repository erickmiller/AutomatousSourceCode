__author__ = 'olya'

from random import randint


def quick_sort(s):
    info = {
        'comparisons': 0
    }

    def _quick_sort(sample):
        less = []
        greater = []
        equal = []
        if len(sample) < 2:
            return sample
        pivot = sample[randint(0, len(sample) - 1)]
        for x in sample:
            if x < pivot:
                info['comparisons'] += 1
                less.append(x)
            elif x > pivot:
                info['comparisons'] += 1
                greater.append(x)
            else:
                info['comparisons'] += 1
                equal.append(x)
        return _quick_sort(less) + equal + _quick_sort(greater)

    info['sorted'] = _quick_sort(s)
    return info['comparisons'], info['sorted']


def real_quick_sort(s, first, last):
    info = {
        'comparisons': 0
    }


    def _real_quick_sort(sample, p, r):
        info['comparisons'] += 1
        if p < r:
            q = partition(sample, p, r)
            i, j = get_corners(sample, p, r, q)
            _real_quick_sort(sample, p, i)
            _real_quick_sort(sample, j, r)


    def partition(sample, p, r):
        x = sample[r]
        i = p - 1
        for j in range(p, r):
            info['comparisons'] += 1
            if sample[j] < x:
                i += 1
                sample[i], sample[j] = sample[j], sample[i]
        sample[i + 1], sample[r] = sample[r], sample[i + 1]
        return i + 1


    def get_corners(sample, p, r, q):
        i, j = q - 1, q + 1
        while i > p and sample[i] == sample[q]:
            info['comparisons'] += 1
            i -= 1
        while j < r and sample[j] == sample[q]:
            info['comparisons'] += 1
            j += 1
        return i, j

    _real_quick_sort(s, first, last)
    info['sorted'] = s
    return info['comparisons'], info['sorted']