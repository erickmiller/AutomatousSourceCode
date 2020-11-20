def root( num ):
    """
        not so newton root
        find square root of a number
    """
    def find_root( min, max ):
        guess = ( min + max ) / 2.0
        guess2 = guess * guess
        if ( abs( guess2 - num ) < delta ):
            return guess
        elif ( guess2 < num ):
            return find_root( guess, max )
        else:
            return find_root( min, guess )

    delta = 0.001*num
    return find_root( 0, max(1,num) )

def newtonroot( num ):
    """
        find square root of a number in newton's way
    """
    def find_root( whim ):
        guess = ( whim + num / whim ) / 2.0
        guess2 = guess**2
        if ( abs( guess2 - num ) < delta ):
            return guess
        else:
            return find_root( guess )

    delta = 0.001*num
    return find_root( 1 )
