def sort_dict(d):
  'return a sorted list of tuples from the dictionary'
  return sorted(d.items(), key = lambda x : x[1], reverse=True)