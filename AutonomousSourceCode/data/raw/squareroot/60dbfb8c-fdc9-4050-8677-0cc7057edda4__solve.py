# This program solves an n-puzzle

from time import time

# Takes in square size and initial configuration
square_size = int(input("Please input the side length of the square: \n"))
print("Please enter the numbers in the square in the following way (example below): ")
print("If you wanted to enter the following configuration for a side length of 3, ")
print("7 2 4")
print("5   6")
print("8 3 1")
print("then you would type in '7 2 4 5 0 6 8 3 1'")
print("Note that the blank spot is represented by the number 0.")
num_string = input("Now, input the properly formatted string for your configuration: \n")

square = []
for i in num_string.split():
  square.append(int(i))

dest = list(range(square_size**2))

N_HASH = {}
for i in range(square_size**2):
  N_HASH[i] = []

DISTANCE_HASH  = {}
for i in range(square_size**2):
  for j in range(i, square_size**2):
    z = j - i
    dy = z//square_size
    dx = z%square_size
    DISTANCE_HASH[(i, j)] = dx + dy
    DISTANCE_HASH[(j, i)] = dx + dy

    if DISTANCE_HASH[(i, j)] == 1:
      N_HASH[i].append(j)
      N_HASH[j].append(i)

def dist_to_dest(num, square_config):
  return DISTANCE_HASH[(num, square_config.index(num))]

def heuristic(square_config):
  d = 0
  for i in range(len(square_config)):
    d += dist_to_dest(i, square_config)

  return d

def neighbors(square_config):
  open_spot = square_config.index(0)
  n_list = []
  for i in N_HASH[open_spot]:
    new_config = list(square_config)
    new_config[open_spot] = square_config[i]
    new_config[i] = 0
    n_list.append(new_config)

  return n_list

def str_print(config):
  for i in range(square_size):
    x = ''
    for j in range(square_size):
      k = config[i*square_size+j]
      if k == 0:
        x += ' '.ljust(3) + ' '
      else:
        x += str(config[i*square_size+j]).ljust(3) + ' '
    print(x)
  print()

t1 = time()

dist_parent_hash = {tuple(square): [0, None]}

d_root = heuristic(square)
q = {d_root: square}

count = 0

max_q_length = len(q)

while len(q) > 0:
  if len(q) > max_q_length:
    max_q_length = len(q)

  m = min(q)
  x = q.pop(m)

  if x == dest:
    break
  count += 1

  nbors = neighbors(x)
  for config in nbors:
    distance = dist_parent_hash[tuple(x)][0] + 1
    if (tuple(config) in dist_parent_hash) == False:
      dist_parent_hash[tuple(config)] = [distance, tuple(x)]
      q[(dist_parent_hash[tuple(config)][0] + heuristic(config))] = config
    elif dist_parent_hash[tuple(config)][0] > distance:
      dist_parent_hash[tuple(config)] = [distance, tuple(x)]
      q[(dist_parent_hash[tuple(config)][0] + heuristic(config))] = config

t2 = time()

if tuple(dest) in dist_parent_hash:
  connection = []
  d = dist_parent_hash[tuple(dest)][0]
  config_to_add = dest
  while d > -1:
    connection.append(config_to_add)
    d -= 1
    config_to_add = dist_parent_hash[tuple(config_to_add)][1]
  print("The connection between the two configurations is: ")
  i = len(connection) - 1
  while i > -1:
    str_print(connection[i])
    i -= 1

  print("The connection is " + str(len(connection) -1) + " edges long.")
else:
  print('The configuration provided is not valid. It is impossible to reach the desired configuration from the given configuration.')
  