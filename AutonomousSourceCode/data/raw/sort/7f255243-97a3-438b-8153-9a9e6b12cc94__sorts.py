import random as rd

def merge_sort(x):
    '''
    x: unsorted list
    '''
    if len(x) == 1:
        return x

    left = x[:len(x)/2]
    right = x[len(x)/2:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    # merge!
    Y = []
    left_k = 0
    right_k = 0
    for k in range(len(x)):
        if left_sorted[left_k] < right_sorted[right_k]:
            Y.append(left_sorted[left_k])
            left_k += 1
        else:
            Y.append(right_sorted[right_k])
            right_k += 1

        # if either of the list reached the end, simply append the other
        if left_k == len(left_sorted):
            Y.extend(right_sorted[right_k:])
            return Y
        if right_k == len(right_sorted):
            Y.extend(left_sorted[left_k:])
            return Y
    return Y

def partition(Y,p):
    '''
    partitions the list using pivot, p
    '''
    left = []
    right = []
    pivots = []
    for k in range(len(Y)):
        if Y[k] < p:
            left.append(Y[k])
        elif Y[k] > p:
            right.append(Y[k])
        elif Y[k] == p:
            pivots.append(Y[k])
    return left,right,pivots

def quick_sort(X):
    '''
    quick sort
    '''
    
    if len(X) <= 1:
        return X

    pivot = X[0]
    left,right,pivots =  partition(X,pivot)
    left_sorted = quick_sort(left)
    right_sorted = quick_sort(right)
    left_sorted.extend(pivots)
    left_sorted.extend(right_sorted)
    return left_sorted


def quick_select(X,n):
    '''
    smartly finds n_th element in a list
    uses quickselection technique
    '''
    
    # base case
    if len(X) == 1:
        return X[0]

    pivot = X[0]
    left,right,pivots = partition(X,pivot)
   
    # left is out
    # n = 0,...,len(X)-1
    # left:[0,...,len(left)-1] 
    # pivots: [len(left),..,len(left)+len(pivots)-1]
    # right: [len(left)+len(pivots),...,len(X)-1] 
    
    # check if element is in left block 
    if len(left) > n:
        return quick_select(left,n)
    
    # check if element is in pivots block
    elif len(left)+len(pivots) > n:
        return pivot
    
    # if not in left or pivots, must be in right block
    else:
        return quick_select(right,n-len(left)-len(pivots))

    

