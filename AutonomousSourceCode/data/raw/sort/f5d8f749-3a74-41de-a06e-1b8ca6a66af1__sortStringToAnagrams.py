def sortStringsToAnagram(strings):
  sortedDict = {}
  for strng in strings:
    key = ''.join(sorted(strng)) #forgot to use join here, whoops!!
    print key
    if key in sortedDict:
      sortedDict[key].append(strng)
    else:
      sortedDict[key] = [strng]
  out = []
  for key in sortedDict:
    for strng in sortedDict[key]:
      out.append(strng)
  return out

def main():
  test = ["god", "a","abc","c","bac","dog"]
  out = sortStringsToAnagram(test)
  print out

main()
