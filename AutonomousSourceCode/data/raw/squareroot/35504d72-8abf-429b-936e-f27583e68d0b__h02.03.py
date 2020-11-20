#!/usr/bin/python

import heapq
import sys

LEFT=1
RIGHT=2
UP=3
DOWN=4
DIRS = [LEFT, RIGHT, UP, DOWN]

def display_dir(dir):
  if dir == LEFT:
    return "LEFT"
  elif dir == RIGHT:
    return "RIGHT"
  elif dir == UP:
    return "UP"
  elif dir == DOWN:
    return "DOWN"
  else:
    return "UNKNOWN"

# Coordinates and Squares

class Coord(object):
  @staticmethod
  def fromIndex(index):
    return Coord(index%3, index/3)

  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y

  def __str__(self):
    return "(%d, %d)" % (self.x, self.y)

  def index(self):
    return self.x + self.y * 3

  def dist(self, other):
    return max(
        abs(self.x - other.x),
        abs(self.y - other.y))

  def move(self, dir):
    if dir == LEFT:
      if self.x == 0:
        return None
      return Coord(self.x-1, self.y)
    elif dir == RIGHT:
      if self.x == 2:
        return None
      return Coord(self.x+1, self.y)
    elif dir == UP:
      if self.y == 0:
        return None
      return Coord(self.x, self.y-1)
    elif dir == DOWN:
      if self.y == 2:
        return None
      return Coord(self.x, self.y+1)
    return None

class Square(object):
  @staticmethod
  def fromStr(str):
    data = []
    entries = str.split(" ")
    if len(entries) != 9:
      print "Invalid square format: %s" % str
      sys.exit(2)
    for entry in str.split(" "):
      if entry == '_':
        data.append(None)
      else:
        data.append(int(entry))
    return Square(data)

  def __init__(self, data):
    self.data = data

  def __key(self):
    return self.__str__()

  def __eq__(self, other):
    return self.__key() == other.__key()

  def __hash__(self):
    return hash(self.__key())

  def find(self, num):
    index = None
    for i in xrange(len(self.data)):
      if self.data[i] == num:
        index = i
        break
    if index == None:
      return None
    return Coord.fromIndex(index)

  def lookup(self, coord):
    return self.data[coord.index()]

  def dist(self, other):
    dist = 0
    for i in [None, 1, 2, 3, 4, 5, 6, 7, 8]:
      # find coords of i in self
      self_coords = self.find(i)
      other_coords = other.find(i)
      dist += self_coords.dist(other_coords)
    return dist

  # Return a new square with the given swap applied
  def swap(self, dir):
    blank = self.find(None)
    if blank == None:
      return None
    dest = blank.move(dir)
    if dest == None:
      return None

    # Get the number to swap
    value = self.lookup(dest)

    # Create the new square and set the new values
    data = []
    for i in xrange(len(self.data)):
      if i == blank.index():
        data.append(value)
      elif i == dest.index():
        data.append(None)
      else:
        data.append(self.data[i])
    
    return Square(data)

  def __str__(self):
    out = ""
    for i in xrange(3):
      for j in xrange(3):
        val = self.data[i*3+j]
        if val:
          out += "%d" % val
        else:
          out += "_"
      if i < 2:
        out += " "
    return out

  def display(self):
    out = ""
    for i in xrange(3):
      for j in xrange(3):
        val = self.data[i*3+j]
        if val:
          out += "%d" % val
        else:
          out += " "
      if i < 2:
        out += "\n"
    return out

# States and solving
curr_order = 1
class Node(object):
  def __init__(self, parent, action, square, path_cost, h_cost):
    self.parent = parent
    self.action = action
    self.square = square
    self.path_cost = path_cost
    self.h_cost = h_cost
    self.children = {}
    self.order = None

    if self.parent:
      self.parent.add_child(self)

  def set_order(self):
    global curr_order
    self.order = curr_order
    curr_order += 1

  def cost(self):
    return self.path_cost + self.h_cost

  def add_child(self, node):
    if node.parent != self:
      return
    self.children[node.action] = node

  def show_path(self):
    if self.parent:
      path = self.parent.show_path()
      path.append(self.action)
    else:
      path = []
    return path

  def __str__(self):
    return "Node for [%s]" % self.square

  def display_tree(self):
    display = ""
    display += str(self.square)

  def display(self):
    return "[%s] (c: %d, p:%d, h:%d, order: %s)" % (
        self.square, self.cost(), self.path_cost, self.h_cost, self.order)


def help_display(indent, node):
  # print node data with given indent to acc
  # then display children, indented further
  str =  "%sNode %s\n" % (indent * "  ", node.display())
  for action in node.children.keys():
    child = node.children[action]
    #acc += "%s%s: %s\n" % ((indent+1)*"  ", display_dir(action), child)
    str += help_display(indent+1, child)
  return str

def display_tree(root):
  return help_display(0, root)

class Solver(object):
  def __init__(self, start, goal):
    self.start = start
    self.goal = goal
    self.frontier = []
    self.frontier_seen = {}
    self.explored = {}

  def make_node(self, square, action=None, parent=None):
    if parent:
      path_cost = parent.path_cost + 1
    else:
      path_cost = 0
    h_cost = square.dist(self.goal)
    return Node(parent, action, square, path_cost, h_cost)

  def push(self, node):
    score = node.cost()
    heapq.heappush(self.frontier, (score, node))
    self.frontier_seen[node] = True

  def pop(self):
    (score, node) = heapq.heappop(self.frontier)
    del self.frontier_seen[node]
    return node

  def findGoalNode(self):
    root = self.make_node(self.start)
    self.push(root)

    while self.frontier:
      node = self.pop()
      #print "  Checking %s" % node
      if node.square == self.goal:
        return (root, node)
      self.explored[node.square] = True
      self.expand(node)

    return (root, None)

  def expand(self, node):
    node.set_order()
#    print "    Expanding node"
    for dir in DIRS:
      new_square = node.square.swap(dir)
      if not new_square:
#        print "      Can't expand to the %s" % display_dir(dir)
        continue
      if new_square in self.frontier_seen or new_square in self.explored:
#        print "      Node already in frontier or explored"
        continue
      new_node = self.make_node(new_square, dir, node)
#      print "      Made new node for square to the %s: %s" % (display_dir(dir),
#          new_node)
      self.push(new_node)

if __name__ == '__main__':
  if len(sys.argv) != 3:
    print "Usage: %s start_state goal_state" % sys.argv[0]
    print "  Each state is a string with 9 entries, where each entry"
    print "  is a number 1-8 or the _ to indicate an empty space."
    sys.exit(1)

  start = Square.fromStr(sys.argv[1])
  goal = Square.fromStr(sys.argv[2])

  print "Calculating path from start state:\n%s" % start.display()
  print "to goal state:\n%s" % goal.display()
#  print "Current goal distance is %d" % start.dist(goal)
#  print "Coords of blank in each: %s, %s" % (start.coords(None),
#      goal.coords(None))
#  for i in xrange(1,9):
#    print "Coords of %d in each: %s, %s" % (i, start.coords(i), goal.coords(i))
#  print "start shifted right:\n%s" % start.swap(RIGHT)

  solver = Solver(start, goal)
  (root, node) = solver.findGoalNode()
  if node == None:
    print "No path found from start to goal."
  else:
    print "Path from start to goal: %s" % ", ".join([display_dir(dir) for dir in
      node.show_path()])
    print "%s" % display_tree(root)

