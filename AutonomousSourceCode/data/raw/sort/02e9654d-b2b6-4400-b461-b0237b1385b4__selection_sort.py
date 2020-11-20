from ds import arrays
import sys
from profile import profile

@profile
def sort(a):
    selection_sort(a,0,len(a))

def selection_sort(a,start,length):
    for i in xrange(start+1,start+length):
        key = a[i]
        j = i
        while(j>start and a[j-1]>key):
            a[j] = a[j-1]
            j -= 1
        a[j] = key

def main():
    a = arrays.make(sys.argv)
    sort(a)
    return a

if __name__=="__main__":
    main()

########################################tests########################################

def assert_sorted(a,from_index,length):
    selection_sort(a, from_index, length)
    for i in xrange(from_index, from_index + length - 1):
        assert a[i]<=a[i+1]

def should_partially_sort():
    assert_sorted([30,20,10,5,3,2,4,1,-4,-5],3,5)
    assert_sorted(arrays.array(50,False),10,20)


