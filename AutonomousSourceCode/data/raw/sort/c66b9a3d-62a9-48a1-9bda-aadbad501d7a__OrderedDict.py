class OrderedDict(object):
  def __init__(self):
    self.d = {}
    self.L = []
    self.sorted = True
  def __getitem__(self, k):
    return self.d[k]
  def __setitem__(self, k, v):
    if k not in self.d:
      self.L.append(k)
      self.sorted = False
    self.d[k] = v
  def __delitem__(self, k):
    del self.d[k]
    self.L.remove(k)
  def __iter__(self):
    if not self.sorted:
      #self.L.sort()
      self.sorted = True
    return iter(self.L)
