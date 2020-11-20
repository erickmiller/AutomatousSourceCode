import collections


############################################################
# Problem 3a

def computeMaxWordLength(text):
    """
    Given a string |text|, return the longest word in |text|.  If there are
    ties, choose the word that comes latest in the alphabet.
    A word is defined by a maximal sequence of characters without whitespaces.
    You might find max() and list comprehensions handy here.
    """
    alphaWords = sorted(text.split())
    sortedWords = collections.OrderedDict()
    for word in alphaWords:
        sortedWords[word] = len(word)
    sortedWords = collections.OrderedDict(sorted(sortedWords.items(), key=lambda t: t[1]))
    return sortedWords.keys()[-1]


############################################################
# Problem 3b

def manhattanDistance(loc1, loc2):
    """
    Return the Manhattan distance between two locations, where the locations
    are pairs of numbers (e.g., (3, 5)).
    """
    return sum(abs(x - y) for x, y in zip(loc1, loc2))


############################################################
# Problem 3c

def mutateSentences(sentence):
    """
    High-level idea: generate sentences similar to a given sentence.
    Given a sentence (sequence of words), return a list of all possible
    alternative sentences of the same length, where each pair of adjacent words
    also occurs in the original sentence.  Notes:
    - The order of the sentences you output doesn't matter.
    - You must not output duplicates.
    - Your generated sentence can use a word in the original sentence more than
      once.
    """
    words = sentence.split()
    bigrams = zip(*[words[i:] for i in range(2)])
    mutatedSentences = dict()
    for i in range(0, len(bigrams)):
        (mutation1, mutation2) = list(bigrams[i]), list(bigrams[i])
        (j, k) = 0, 0
        while (j < len(bigrams)):
            if (mutation1[-1] == bigrams[j][0]):
                mutation1.append(bigrams[j][1])
                j = 0
            if len(mutation1) == len(words): mutatedSentences[" ".join(mutation1)] = len(mutation1)
            if (mutation2[0] == bigrams[len(bigrams) - 1 - j][1]):
                mutation2.insert(0, bigrams[len(bigrams) - 1 - j][0])
                j = 0
            if len(mutation2) == len(words): mutatedSentences[" ".join(mutation2)] = len(mutation2)
            k += 1
            if k > (len(bigrams) * len(bigrams)): break
            j += 1
        i += 1
    return sorted(mutatedSentences.keys())


############################################################
# Problem 3d

def sparseVectorDotProduct(v1, v2):
    """
    Given two sparse vectors |v1| and |v2|, each represented as Counters, return
    their dot product.
    You might find it useful to use sum() and a list comprehension.
    This function will be useful later for linear classifiers.
    """
    return (sum(a * b for a, b in zip(v1.values(), v2.values())))


############################################################
# Problem 3e

def incrementSparseVector(v1, scale, v2):
    """
    Given two sparse vectors |v1| and |v2|, perform v1 += scale * v2.
    This function will be useful later for linear classifiers.
    """
    for v in v2.keys(): v1[v] = v1[v] + ( scale * v2[v] )
    return (v1) #and also return it b/c not sure if you want that...



############################################################
# Problem 3f

def computeMostFrequentWord(text):
    """
    Splits the string |text| by whitespace and returns two things as a pair: 
        the set of words that occur the maximum number of times, and
	their count, i.e.
	(set of words that occur the most number of times, that maximum number/count)
    You might find it useful to use collections.Counter().
    """
    topwords = collections.Counter(text.split()).most_common()
    (toplist, lasttop) = [], 0
    for top in topwords:
        if (top[1] >= lasttop): toplist = [top[0]] + toplist
        elif (top[1] < lasttop): break
        lasttop = top[1]
    return (set(toplist), lasttop)



############################################################
# Problem 3g

def computeLongestPalindrome(text):
    """
    A palindrome is a string that is equal to its reverse (e.g., 'ana').
    Compute the length of the longest palindrome that can be obtained by deleting
    letters from |text|.
    For example: the longest palindrome in 'animal' is 'ama'.
    Your algorithm should run in O(len(text)^2) time.
    You should first define a recurrence before you start coding.
    """
    cache = {}
    def recurse(text, b, e):
        # recurrence finds length of longest palindrome dynamically & w/ memoization:
        if(b, e) in cache: return cache[(b, e)]
        if b == e: ans = 1
        elif b > e: ans = 0
        elif text[b] == text[e]: ans = 2 + recurse(text, b+1, e-1)
        else: ans = max( recurse(text, b+1, e), recurse(text, b, e-1) )
        cache[(b, e)] = ans
        return ans

    return recurse(text, 0, len(text)-1)
