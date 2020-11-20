def return_name (str):
  # length method
  return len(my_name)
  # to lowercase method
  return my_name.lower()
  # capitalize method
  return my_name.upper()

def pi_to_string():
  i_love_pi = 3.14
  return str(i_love_pi)

def hello_world():
  return "Hello World!"

def return_smallest(x, y):
  if x < y: return x
  elif y < x: return y
  else: return "that is the same number!"

def square_root(num):
  while ans * ans < x:
    ans = ans + 1
  return ans

def divisor(num):
  for i in range(1, num):
    if num%i == 0:
      return 'divisor ', i

# tuple is an ordered sequence of elements
test = (1, 2, 3, 4) #immutable
print test[1:3] #from 1 up to index 3

test_2 = [3, 5, 4, 2]
sorted_array = test_2.sort()
print sorted_array
