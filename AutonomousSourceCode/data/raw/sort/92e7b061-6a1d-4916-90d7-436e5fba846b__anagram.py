def anagram(dict):
  output = []
  map = {}

  for word in dict:
    sorted_word = sortchars(word)
    if sorted_word not in map:
      map[sorted_word] = [word]
    else:
      map[sorted_word].append(word)

  for k in map.keys():
    if (len(map[k])) > 1:
      output.append(map[k])

  return output

def sortchars(word):
  l = list(word)
  l.sort()
  return ''.join(l)

result = anagram(("algorithm", "dog", "cat", "god", "tac", "test"))
print result

