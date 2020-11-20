#A method to sort an array of strings so that all the anagrams are next to eachother

def anagram_sort(str_arr):
  anagram_dict = {}
  sorted_arr = []
  for i in str_arr:
    key = ''.join(sorted(i))
    if key in anagram_dict:
      anagram_dict[key].append(i)
    else:
      anagram_dict[key] = [i]
  for key in anagram_dict:
    sorted_arr += anagram_dict[key]
  return sorted_arr

