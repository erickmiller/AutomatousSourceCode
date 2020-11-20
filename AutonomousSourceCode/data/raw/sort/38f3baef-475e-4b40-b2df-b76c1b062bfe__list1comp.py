def match_ends(words):
  count = 0
  for word in words:
    if len(word) >= 2 and word[0] == word[-1]:
      count += 1
  return count

def front_x(words):
  xwords = []
  otherwords = []
  for word in words:
    if word[0] == 'x':
      xwords.append(word)
    else:
      otherwords.append(word)
  return sorted(xwords) + sorted(otherwords)

def sort_last(tuples):
  return sorted(tuples, key=lambda tuple: tuple[-1])
