#Radix Sort
#O(n), need to know the number of digits

def radix_sort(list_1d,num_digits): #num_digits is the largest number of digits
    for digit in range(num_digits):
        current_digits=[(x/(10**digit))%10 for x in list_1d] #extract digits of interest
        (sorted_list_digits,sorted_list_index)=counting_sort(current_digits,9)
        sorted_list=[list_1d[sorted_list_index[i]] for i in range(len(sorted_list_index))]
        list_1d=sorted_list
    return list_1d

#test
print radix_sort([345,999,765,764,444,789,300],3)
print radix_sort([3,100,2],3)
print radix_sort([3,2],1)
print radix_sort([2,3],1)
print radix_sort([1,3,2,3,4,5,6,7,0,2,3,99,50,10],2)
