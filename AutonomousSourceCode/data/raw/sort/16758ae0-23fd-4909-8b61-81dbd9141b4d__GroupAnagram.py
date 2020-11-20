'''
group the anagrams together

cat tea tac  eat rat act tar ball
'''
'''
return the lexicalgraphical order sorted string
'''
def lexicalSort(string):
    return ''.join(sorted(string))


def groupAnagram(arr):
    groups = {}
    for string in arr:
        try: groups[lexicalSort(string)]+=[string]
        except: groups[lexicalSort(string)] = [string]

    return groups

print groupAnagram(['cat', 'tea', 'tac',  'eat', 'rat', 'act', 'tar' ,'ball'])



