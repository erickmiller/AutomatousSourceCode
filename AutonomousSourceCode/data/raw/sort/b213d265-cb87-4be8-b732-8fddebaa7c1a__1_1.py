# Solution to Exercise 1.1 from Cracking the Coding Interview, 5th Edition
# Nitin Punjabi
# nptoronto@yahoo.com
# https://github.com/nitinpunjabi
#
# Assumptions:
# - whitespace is insignificant.
# - case-sensitive

# Solution using dict.
def unique_chars_dict(s):
  chars = {}
  for c in s:
    if c != ' ':
      if c in chars:
        return False
      else:
        chars[c] = 1

  return True

# Solution using sorting.
def unique_chars_sort(s):
  sorted_s = sorted(s)
  for i in range(1, len(sorted_s)):
    if sorted_s[i] != ' ':
      if sorted_s[i] == sorted_s[i - 1]:
        return False

  return True

