import math


def square_root(a):
    x = 3.0
    epsilon = 0.000001
    while True:
        y = (x + (a/x))/2
        if abs(y-x) < epsilon:
            return y
            break
        x = y


def test_square_root(a):
    function = square_root(a)
    builtin = math.sqrt(a)
    diff = abs(function - builtin)
    return '%d    %.8f    %.8f    %.11g' % (a, function, builtin, diff)


def eval_loop():
    while True:
        line = raw_input('>>> ')
        if line == 'done':
            print 'DONE'
            break
        print eval(line)


if __name__ == '__main__':

    # for a in range(2, 37, 3):
        # print 'Square root of %d is %f' %(a, square_root(a))

    # for a in range(0, 10):
        # print test_square_root(a)

    # eval_loop()
