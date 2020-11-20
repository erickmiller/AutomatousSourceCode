#Archana Bahuguna ---- Decorator fn without the wrapper fn ----- Jan 6th 2014

def accept_n_gt_zero(fnToCall):
        if n <= 0:
            print 'From inside Decorator: n <=0 before raising exception'
           # raise Exception("Exception raised: n must be > 0")
            return 0
        else:
            print 'From inside Decorator: n > 0, before calling SquareRoot fn'
            return fnToCall(n, *args, **kwargs)


@accept_n_gt_zero
def SquareRoot(n):
    result = n**(1/2)
    return result
