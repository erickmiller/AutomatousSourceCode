#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import unittest
import random
import math
from operator import itemgetter

from benchmark import timethese

SAMPLE_SIZE             = 100 * 1000
BENCHMARK_ITERATIONS    = 100


def main():
    print "Generating sample data..."    
    sample = generatate_triplets(SAMPLE_SIZE)
    
    timethese(BENCHMARK_ITERATIONS,
        (
            ("classic",     lambda : sort_classic(sample)),
            ("itemgetter",  lambda : sort_itemgetter(sample)),
            ("GRT-arithm",  lambda : sort_arithmetic(sample)),
            ("GRT-chars",   lambda : sort_chars(sample)),
            ("GRT-bits",    lambda : sort_bits(sample)),
        )
    )


def generatate_triplets(N):
    RANGE = 99
    a = []

    for x in xrange(N):
        a.append(
            (random.randint(0, RANGE), random.randint(0, RANGE), random.randint(0, RANGE))
        )
    return a

def sort_itemgetter(data):
    return sorted(sorted(sorted(data, key=itemgetter(2), reverse=True), key=itemgetter(1)), key=itemgetter(0))


def sort_classic(data):
    def cmp_triplets(a, b):
        return cmp(a[0], b[0]) or cmp(a[1], b[1]) or cmp(b[2], a[2])
    
    return sorted(data, cmp=cmp_triplets)


def sort_arithmetic(data):
    def unpack(a):
        x = int(a / 100**2)
        y = int(a / 100) - x * 100
        z = 99 - a % 100
        return (x, y, z)
    
    def pack(s):
        return s[0] * 100**2 + s[1] * 100 + (99 - s[2])
    
    return map(unpack, sorted(map(pack, data)))


def sort_bits(data):
    def unpack(a):
        return ( (a & 0b111111100000000000000) >> 14, (a & 0b11111110000000) >> 7, ~(a & 0b1111111) )
    
    def pack(s):
        return (s[0] << 14) | (s[1] << 7) | ~s[2]
    
    return map(unpack, sorted(map(pack, data)))


def sort_chars(data):
    def unpack(a):
        return (ord(a[0]), ord(a[1]), 99 - ord(a[2]))
    
    def pack(s):
        return chr(s[0]) + chr(s[1]) + chr(99 - s[2])
    
    return map(unpack, sorted(map(pack, data)))


if __name__ == '__main__':
    main()
