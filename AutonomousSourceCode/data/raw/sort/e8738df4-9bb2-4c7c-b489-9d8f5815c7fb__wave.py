# function to sort a list in a wave returning the smallest lexicographical list if multiple answers exist

def wave(A):
    sorted_list = sorted(A)
    wave_list = []
    while len(sorted_list)>0:
    	if len(sorted_list)>1:
    		wave_list.append(sorted_list.pop(1))
    		wave_list.append(sorted_list.pop(0))
    	else:
    		wave_list.append(sorted_list.pop(0))
    return wave_list

print wave([1,2,3,4,5])