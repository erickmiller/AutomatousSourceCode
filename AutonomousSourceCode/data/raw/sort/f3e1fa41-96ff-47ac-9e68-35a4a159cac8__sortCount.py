#!/usr/bin/env python

""" sort the count of words and display top 3 along with count"""

import sys


def getSortedCounts(wordCountFileName, separator):
    sortedCounts = []
    with open(wordCountFileName, 'r') as wordCountFile:
        for line in wordCountFile:
            #strip white spaces
            line = line.strip()
            word, count = line.split(separator, 1)
            try:
                sortedCounts.append((word, int(count)))
            except ValueError:
                #count was not number so ignore it
                pass
    sortedCounts = sorted(sortedCounts, key = lambda wCount: wCount[1])
    return sortedCounts


            


def main():
    if len(sys.argv) >= 2:
        wordCountFileName = sys.argv[1]
        sortedCounts = getSortedCounts(wordCountFileName, '\t')
        #print top 3 word and counts
        print sortedCounts[0][0], '\t', sortedCounts[0][1]
        print sortedCounts[1][0], '\t', sortedCounts[1][1]
        print sortedCounts[2][0], '\t', sortedCounts[2][1]
    else:
        print 'Err: word count file should be passed'

if __name__ == '__main__':
    main()
