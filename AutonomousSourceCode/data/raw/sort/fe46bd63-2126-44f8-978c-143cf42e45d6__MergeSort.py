import pygame

class MergeSort():
  """docstring for MergeSort"""
  def __init__(self):
    pass
    
  def RecursiveSort(self, l):
    """docstring for sort2"""
    # recursive stopping point
    if len(l) == 1:
      return (l, 0)

    # divide task in smaller subtasks
    half_size = len(l)/2
    l1 = l[:half_size]
    l2 = l[half_size:]
    # and recursively sort them
    l1_sorted, l1_complexity = self.RecursiveSort(l1)
    l2_sorted, l2_complexity = self.RecursiveSort(l2)

    # merge results
    algorithm_complexity = 0
    l_sorted = []
    x = 0
    y = 0
    while True:
      algorithm_complexity += 2
      if l1_sorted[x] < l2_sorted[y]:
        l_sorted.append(l1_sorted[x])
        x += 1
        if x >= len(l1_sorted):
          l_sorted += l2_sorted[y:]
          break
      else:
        l_sorted.append(l2_sorted[y])
        y += 1
        if y >= len(l2_sorted):
          l_sorted += l1_sorted[x:]
          break
    return (l_sorted, algorithm_complexity + l1_complexity + l2_complexity)

class Element():
  """docstring for Animation"""
  def __init__(self, elem, pos):
    self.elem = elem
    self.pos = pos

  def getRect(self):
    self.rect = pygame.Rect(self.pos * 10, 0, 1, self.elem)
  
  def changePos(self, new_pos):
    self.pos = new_pos
  
  def update(self):
     pygame.display.update()

  def Iteration(self):
    self.getRect()
    self.update()

def main():
  animation = MergeSort()

if __name__ == '__main__':
  main()

