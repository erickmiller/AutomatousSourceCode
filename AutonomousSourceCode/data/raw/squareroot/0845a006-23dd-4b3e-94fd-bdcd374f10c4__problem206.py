def matches_template(nr):
  nr_str = str(nr)
  return (len(nr_str) == 19 and
          nr_str[0] == '1' and
          nr_str[2] == '2' and
          nr_str[4] == '3' and
          nr_str[6] == '4' and
          nr_str[8] == '5' and
          nr_str[10] == '6' and
          nr_str[12] == '7' and
          nr_str[14] == '8' and
          nr_str[16] == '9' and
          nr_str[18] == '0')

def solve():
  min_root = 1010101010   # multiple of 10, >= sqrt(1020304050607080900)
  max_root = 1389026620   # multiple of 10, <= sqrt(1929394959697989990)
  for root in range(min_root, max_root+1, 10):
    square = root * root
    if matches_template(square):
      return root
  return None

print(solve())
