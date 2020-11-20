def bSearch(Phrase, SortedList):
      Low = 0
      High = len(SortedList) - 1
      while Low <= High :
            Mid = (High + Low) / 2
            if SortedList[Mid] == Phrase:
                  return Mid
            elif SortedList[Mid] > Phrase :
                  High=Mid - 1
            else :
                   Low = Mid + 1
      return "X";

def main():
      my_list = [34,32,34,234,23,42,43,234,234,2,423,41,3,12,123,13,13,12,3,423,42,4]
      my_list = sorted(my_list)
      print my_list
      Sort = bSearch(23, my_list)
      print Sort


if __name__ == "__main__":
      main()