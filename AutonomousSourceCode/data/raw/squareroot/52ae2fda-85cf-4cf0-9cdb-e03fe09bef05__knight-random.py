"""
http://www.johndcook.com/blog/2012/05/08/a-knights-random-walk/
"""

import random
random.seed(12345)

import ROOT

def moves(square):
    N = dict((d for d in zip("abcdefgh", range(1, 9))))
    L = dict((d for d in zip(range(1, 9), "abcdefgh")))
    
    numbers = N[square[0]], int(square[1])
    #print "-", numbers[0], numbers[1]
    m = []
    for two in (-2, +2):
        for one in (-1, +1):
            h = numbers[0] + two
            v = numbers[1] + one

            #print ":", h,v
            if 1 <= h <= 8 and 1 <= v <= 8:
                #print h,v
                m.append((L[h], v))

            h = numbers[0] + one
            v = numbers[1] + two
            #print ":", h,v
            if 1 <= h <= 8 and 1 <= v <= 8:
                #print h,v
                m.append((L[h], v))
    
    return ["%s%i"%(a,n) for a,n in set(m)]

def random_walk(startingsq):
    sq = startingsq
    N = 0
    while True:
        N += 1
        sq = random.choice(moves(sq))

        if sq == startingsq:
            return N

h = ROOT.TH1F("", "", 1000, 0, 1000)
for n in xrange(10000):
    h.Fill(random_walk("a1"))

h.Draw()
raw_input("asf")
