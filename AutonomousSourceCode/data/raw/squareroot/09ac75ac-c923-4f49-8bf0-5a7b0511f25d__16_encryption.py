# https://www.hackerrank.com/challenges/encryption
# square substitution cypher
def squareCypher(s):
    from math import sqrt
    s = s.replace(' ', '')

    root = sqrt(len(s))
    cols = int(root) + 1 if root % 1 else int(root)

    result = ''
    for i in range(cols):
        for j in range(cols):
            index = j * cols + i
            if index < len(s):
                result += s[index]

        result += ' '

    return result

print squareCypher(raw_input())