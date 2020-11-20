def find_anagrams():

    def create_dict():
        fin = open('words.txt')
        res = {}
        
        for line in fin:
            word = line.strip()
            s = list(word)
            s.sort()

            sorted_char_string = ""
            for char in s:
                sorted_char_string += char

            if sorted_char_string in res:
                res[sorted_char_string] += [word]
            else:
                res[sorted_char_string] = [word]
            
        return res

    def sort_dict(d):
        res = []
        
        for key, value in d.items():
            res += [(len(value), value)]
        return res
                    
    dictionary = create_dict()
    return sort_dict(dictionary)


def print_anagrams(anagram_list, sorted):
    if sorted:
        anagram_list.sort(reverse = True)
    for (count, anagrams) in anagram_list:
        if count >= 2:
            print count, anagrams

      
def scrabble_bingos(anagram_list):
    

    res = []
    for (count, anagrams) in anagram_list:
        if len(anagrams[0]) == 8 and count >= 2:
            res += [(count, anagrams)]
            
    res.sort(reverse = True)
    print res[0]
            
anagram_list = find_anagrams()
scrabble_bingos(anagram_list)
