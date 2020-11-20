
def square_root(a, x):
    i = 10;
    y = 0;
    while i > 0:
        i=i-1
        y = (x + a/x) / 2
        print i, y
        x = y

    return y

def main():
    while True:
        a = input('> ')
        #print 'entered', a
        if a == 'done':
            print 'Done!'
            return
        else:

            # check if its int or float
            if isinstance(a, int):
                pass
            elif isinstance(a, float):
                pass
            else:
                print 'Please enter int or float values'
                continue
        
            sq_val = square_root(a, 10);
            print 'sq(', a, ')=', sq_val


if __name__ == "__main__":
    main()        
