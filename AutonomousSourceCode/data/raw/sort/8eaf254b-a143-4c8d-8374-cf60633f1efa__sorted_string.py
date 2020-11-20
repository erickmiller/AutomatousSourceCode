#!/usr/bin/env python
"""
Exercise 5A - Write a function sorted_string that takes one string
  argument and returns a string with the same characters but sorted in
  lexical (alphabetic) order.  You may use the list sort method, but
  you may NOT use the built-in library function 'sorted' in your
  solution.  Write your function in a module also named sorted_string
  that defines at least two test strings.  In your module, call your
  function on each of these strings and print the results.
"""
s = 'supercalifragilisticexpealidocius'
t = 'antidisestablishmentarianism'
def sorted_string(s):
    "sorted_string(s), s a string.  Returns a sorted string."

    # Break string into a list of characters
    s_list=list(s)

    if len(s) > 1:
        s_list.sort()

    return ''.join(s_list)

def test_sorted_string(s=s,t=t):
    print sorted_string(s)
    print sorted_string(t)
    return None

if __name__ == "__main__":
    # commandline execution, for debugging
    import sys
    if len(sys.argv) == 3:
        test_sorted_string(s=sys.argv[1], t=sys.argv[2])
    else:
        test_sorted_string()
else:
    # imported execution as per spec:
    test_sorted_string()
