"""Write a method to sort an array of strings so that all the anagrams
are next to each other"""


def anagram_sort(words):
    return sorted(words,  key=lambda x: sorted(x))


def test_anagram_sort():
    words = ['tabu', 'ate',  'beta', 'bade', 'tuba', 'abet',
             'tea', 'abut', 'bead', 'abed', 'beat', 'eat']
    print words
    print anagram_sort(words)


def main():
    test_anagram_sort()


if __name__ == '__main__':
    main()
