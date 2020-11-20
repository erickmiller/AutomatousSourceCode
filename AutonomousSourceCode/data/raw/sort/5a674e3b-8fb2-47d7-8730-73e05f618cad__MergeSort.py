def sort(ip):
    if len(ip) == 1:
        return ip
    else:
        seperateat = len(ip)/2
        left =ip[:seperateat]
        right = ip[seperateat:]
        return merge(sort(left), sort(right))
        
def merge(left, right):
    sorted = []
    inversions = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                sorted.append(left[0])
                left.pop(0)
            elif right[0] < left[0]:
                sorted.append(right[0])
                right.pop(0)
        elif len(left) > 0:
            sorted.append(left[0])
            left.pop(0)
        elif len(right) > 0:
            sorted.append(right[0])
            right.pop(0)
    return sorted
    
print sort([6,5,3,1,8,7,2,4,9,1])
