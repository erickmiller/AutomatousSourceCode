
def square_root(x,guess=1):
    def improve_answer():
        def average(a,b):
            return (a+b)/2.0
        return average(guess,x/guess)   
    def good_enough():
        good = abs(guess*guess-x)
        return good<0.001
    while not good_enough():
        guess = improve_answer()
    return guess

if __name__ == '__main__':
    x = float(raw_input("Enter a number to get the square root: "))
    sqrt = square_root(x)
    print "sqrt(%f) = %f"%(x,sqrt)
    print "sqrd(%f) = %f"%(sqrt,sqrt*sqrt)
