#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import math

from benchmark import timethese

SAMPLE_SIZE             = 40 * 1000
BENCHMARK_ITERATIONS    = 100


def main():
    print "Generating sample data..."    
    points = generatate_points(SAMPLE_SIZE)
    
    timethese(BENCHMARK_ITERATIONS,
        (
            ("classic",     lambda : sort_classic(points)),
            ("key",         lambda : sort_key(points)),
            ("OM",          lambda : sort_om(points)),
            ("ST",          lambda : sort_st(points)),
        )
    )


def generatate_points(N):
    DISTANCE = 10
    a = []

    for x in xrange(N):
        a.append(
            (random.uniform(-DISTANCE, DISTANCE), random.uniform(-DISTANCE, DISTANCE))
        )
    return a


def veclen(point):
    return math.sqrt( point[0] ** 2 + point[1] ** 2)


def sort_classic(data):
    
    def cmp_distances(a, b):
        return int(veclen(a) - veclen(b))
    
    return sorted(data, cmp=cmp_distances)


def sort_key(data):
    return sorted(data, key=veclen)


def sort_om(data):
    cache = dict()
    
    def cmp_cached(a, b):
        if a not in cache:
            cache[a] = veclen(a)
        if b not in cache:
            cache[b] = veclen(b)

        return int(cache[a] - cache[b])
    
    return sorted(data, cmp=cmp_cached)


def sort_st(data):
    return [ p for vl, p in sorted([(veclen(p), p) for p in data]) ]


if __name__ == '__main__':
    main()
