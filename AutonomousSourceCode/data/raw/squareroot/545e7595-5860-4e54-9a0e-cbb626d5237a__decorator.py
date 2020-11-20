#Archana Bahuguna ---- Decorator fn ----- Jan 6th 2014

def accept_n_gt_zero(fnToCall):
   def wrapper(n, *args, **kwargs):
       if n <= 0:
           print 'From inside Decorator: n <=0 before raising exception'
           raise Exception("Exception raised: n must be > 0")
       else:
           print 'From inside Decorator: n > 0, before calling SquareRoot fn'
           return fnToCall(n, *args, **kwargs)
       return wrapper


# @accept_n_gt_zero
def square_root(n):
    result = n**(1/2)
    return result
# is same as ... SquareRoot = accept_n_gt_zero(SquareRoot)
# square_root(10)
print accept_n_gt_zero(square_root)(10) # <function wrapper>

def wrapper(n, *args, **kwargs):
    if n <= 0:
        print 'From inside Decorator: n <=0 before raising exception'
        raise Exception("Exception raised: n must be > 0")
    else:
        print 'From inside Decorator: n > 0, before calling SquareRoot fn'
        print n, args, kwargs

wrapper(10, 20, a=12)            
#Why do we need a wrapper fn if n is being passed through the fnToCall arg itself?
#Why does the code not work if we dont use the wrapper fn? It should work...
#How is n being passed?
