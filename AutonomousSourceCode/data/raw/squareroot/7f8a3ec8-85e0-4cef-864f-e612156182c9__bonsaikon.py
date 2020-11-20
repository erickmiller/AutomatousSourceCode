#!/usr/bin/env python
# Simple Daikon-style invariant checker
# Andreas Zeller, May 2012
# Complete the provided code around lines 28 and 44
# Do not modify the __repr__ functions.
# Modify only the classes Range and Invariants,
# if you need additional functions, make sure
# they are inside the classes.

import sys
import math
import random

#############
### DEBUG ###
#############
# debug #
#########

breakpoints = {118:True}
watchpoints = {'c': True}
stepping = False


def debug(command, my_arg, my_locals):
  global stepping
  global breakpoints
  global watchpoints
  
  if command.find(' ') > 0:
    arg = command.split(' ')[1]
  else:
    arg = None
    
  if command.startswith('s'):
    stepping = True
    return True
  elif command.startswith('c'):
    stepping = False
    return True
  elif command.startswith('p'):    # print 
    if (arg == None):
      print my_locals
    elif(arg in my_locals):
      print arg,' = ', repr(my_locals[arg])
    else:
      print 'No such variable:', arg
  elif command.startswith('b'):    # breakpoint         
    if(arg == None):
      print 'You must supply a line number'
    else:
      breakpoints[int(arg)] = True
  elif command.startswith('w'):    # watch variable
    if arg == None:
      print "You must supply a variable name"
    else:
      watchpoints[arg] = True 
  elif command.startswith('q'):
    sys.exit(0)
  else:
    print "No such command", repr(command)
  return False



############
### main ###
############


def square_root(x, eps = 0.00001):
    assert x >= 0
    y = math.sqrt(x)
    assert abs(square(y) - x) <= eps
    return y
    
def square(x):
    return x * x

# The Range class tracks the types and value ranges for a single variable.
class Range:
    def __init__(self):
        self.min  = None  # Minimum value seen
        self.max  = None  # Maximum value seen
    
    # Invoke this for every value
    def track(self, value):
        # YOUR CODE
        if self.min == None and self.max == None:
            self.min = value
            self.max = value          
        if value <= self.min:
            self.min = value
        elif value > self.max:
            self.max = value
        
            
    def __repr__(self):
        return repr(self.min) + ".." + repr(self.max)




# The Invariants class tracks all Ranges for all variables seen.
class Invariants:
    def __init__(self):
        # Mapping (Function Name) -> (Event type) -> (Variable Name)
        # e.g. self.vars["sqrt"]["call"]["x"] = Range()
        # holds the range for the argument x when calling sqrt(x)
        self.vars = {}
        self.vars["square_root"]={}
        self.vars["square_root"]["call"]={}
        self.vars["square_root"]["call"]["x"]=Range()
        self.vars["square_root"]["call"]["eps"]=Range()
        self.vars["square_root"]["return"]={}
        self.vars["square_root"]["return"]["y"]=Range()
        self.vars["square_root"]["return"]["ret"]=Range()
        
        
    def track(self, frame, event, arg):
           
        # YOUR CODE HERE. 
        # MAKE SURE TO TRACK ALL VARIABLES AND THEIR VALUES
        # If the event is "return", the return value
        # is kept in the 'arg' argument to this function.
        # Use it to keep track of variable "ret" (return)
        if event == "call" and frame.f_code.co_name == "square_root":
            self.vars[frame.f_code.co_name][event]["x"].track(frame.f_locals["x"])
            self.vars[frame.f_code.co_name][event]["eps"].track(frame.f_locals["eps"])
        elif event == "return" and frame.f_code.co_name == "square_root": 
            self.vars[frame.f_code.co_name][event]["y"].track(frame.f_locals["y"])
            self.vars[frame.f_code.co_name][event]["ret"].track(arg)
    
    def __repr__(self):
        # Return the tracked invariants
        s = ""
        for function, events in self.vars.iteritems():
            for event, vars in events.iteritems():
                s += event + " " + function + ":\n"
                # continue
                
                for var, range in vars.iteritems():
                    s += "    assert "
                    if range.min == range.max:
                        s += var + " == " + repr(range.min)
                    else:
                        s += repr(range.min) + " <= " + var + " <= " + repr(range.max)
                    s += "\n"
                
        return s

invariants = Invariants()
    
def traceit(frame, event, arg):
    #print event, frame.f_lineno, frame.f_code.co_name, frame.f_locals
    invariants.track(frame, event, arg)
    return traceit

sys.settrace(traceit)
# Tester. Increase the range for more precise results when running locally
eps = 0.000001
testo = [3, 0, -10]
for i in range(1, 1000):
    r = int(random.random() * 1000) # An integer value between 0 and 999.99
    z = square_root(r, eps)
    z = square(z)
sys.settrace(None)
print invariants

