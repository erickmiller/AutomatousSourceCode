"""Lab_LineSorting"""
def linesort(line):
    """return string with line sorted"""
    wordlist = [raw_input() for _ in xrange(line)]
    wordlist.sort(key=len)
    for j in wordlist:
        print j
linesort(input()) 
