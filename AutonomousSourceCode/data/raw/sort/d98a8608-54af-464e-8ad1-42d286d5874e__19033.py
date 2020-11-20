# conding: UTF-8
import sys

def readWords(argv):
  f = open(argv)
  str = f.read()
  f.close
  return str

def sortDictionary(dictionary):
  sorted_dictionary = [(v,k) for k,v in dictionary.items()]
  sorted_dictionary.sort()
  sorted_dictionary.reverse()
  return sorted_dictionary

def insertWords2Dictionary(str_list):
  dictionary = {}
  for word in str_list:
    dictionary[word] = dictionary.get(word, 0) + 1
  return dictionary

str = readWords(sys.argv[1])
str_list = str.split()
dictionary = insertWords2Dictionary(str_list)
sorted_dictionary = sortDictionary(dictionary)
print "All count is" ,len(str_list)
for count, word in sorted_dictionary[:20]:
    print count, word
