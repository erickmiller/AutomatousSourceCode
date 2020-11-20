def insertionSort(ar):
    v = ar[-1]
    pos = len(ar) - 2

    if(-1 == pos):
      print " ".join(map(str, ar))
      return ""

    sorted = False
    while(not sorted):
      if(-1 == pos):
        ar[0] = v
        sorted = True

      elif(v <= ar[pos]):
        ar[pos+1] = ar[pos]
        pos -= 1

      elif(ar[pos] < v):
        ar[pos+1] = v
        sorted = True
      
      print " ".join(map(str, ar))
    
    return ""

#m = input()
#ar = [int(i) for i in raw_input().strip().split()]
#insertionSort(ar)
