def median(args):
    sorted_args = args
    sorted_args.sort()
    
    args_no = len(sorted_args)
    
    #even number of elements
    if args_no%2 != 0:
        return sorted_args[args_no/2]
    #odd number of elements
    else:
        #mean of 2 middle numbers
        middle_first = float(sorted_args[args_no/2 - 1])
        middle_second =  float(sorted_args[args_no/2])
        return (middle_first+middle_second)/2.0

    
#Testing functions:
def median_test(args):
    print "Input: ", args, "Output: ", median(args)
    
median_test([1,3,6,7,12]) 
median_test([7,3,1,4]) 
    