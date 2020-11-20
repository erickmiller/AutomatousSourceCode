# Sorting list of dictionary

def sort(dictList):
  # x is the basis of sorting
  # -x for ascending order, x for descending order
  return sorted(dictList, key = lambda x: -x['count'])