def SortAnagrams(i):
  return sorted(i, lambda x, y: cmp(sorted(x), sorted(y)))

x = ["abcd", "wxyz", "dcba", "zyxw", "cdba"]
print SortAnagrams(x)
