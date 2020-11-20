from itertools import combinations

def is_square(n):
    root = int(n ** 0.5)
    return n == root*root

# returns dict of letter -> digit if n is a valid digital substitution of w,
#   otherwise returns None
def get_pandigital_mapping(w, n):
    str_n = str(n)

    if len(str_n) != len(w):
        return None

    mapping = {}
    used_digits = set()

    for i in xrange(len(w)):
        digit = int(str_n[i])
        if w[i] in mapping and mapping[w[i]] != digit:
            # one letter cannot have multiple mappings
            return None
        elif digit in used_digits:
            # multiple letters cannot map to the same digit
            return None
        else:
            used_digits.add(digit)
            mapping[w[i]] = digit

    return mapping

def apply_mapping(mapping, w):
    used = set()

    n = 0
    for c in w:
        if c not in mapping:
            return ValueError('Mapping does not contain a character in the word')
        n = n*10 + mapping[c]
        used.add(c)

    if len(used) != len(mapping):
        print "Not all the characters in the mapping were used -- did not use an anagram pair"

    return n

# returns largest square formed by pair if the pair is a square anagram word
#   pair. Otherwise returns 0
def pandigital_square_pair(w1, w2):
    if len(w1) != len(w2):
        return False

    max_square = 0

    i = int((10 ** (len(w1)-1)) ** 0.5 + 1)

    while i*i < 10 ** len(w1):
        mapping = get_pandigital_mapping(w1, i*i)
        if mapping:
            mapped = apply_mapping(mapping, w2)
            if len(str(mapped)) == len(str(i*i)) and is_square(mapped):
                # mapped is square and has no leading zeroes
                max_square = max(mapped, i*i, max_square)

        i += 1

    return max_square

with open('words.txt', 'r') as f:
    words = f.readlines()

assert(len(words) == 1)

words = words[0].split(',')
words = map(lambda w: w[1:-1], words) # strip quotation marks

anagrams = {}

for w in words:
    anagram_hash = ''.join(sorted(w))
    if anagram_hash not in anagrams:
        anagrams[anagram_hash] = [w]
    else:
        anagrams[anagram_hash].append(w)

max_square = 0

for k in anagrams:
    if len(anagrams[k]) > 1:
        for combo in (combinations(anagrams[k], 2)):
            max_square = max(pandigital_square_pair(combo[0], combo[1]), max_square)

print max_square
