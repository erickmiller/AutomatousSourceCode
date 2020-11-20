#Quinn Z Shen

import sys
import math

memo = dict()
memo_ana = dict()

def isFairAndSquare(num):
    square = math.sqrt(num)
    if square == int(square) and isFair(num) and isFair(int(square)):
        return 1
    return 0

def isFair(num):
    if num in memo_ana:
        return memo_ana[num]
    else:
        i = int(math.ceil(float(len(str(num)))/2))
        if str(num)[i:] == str(num)[:-i][::-1]:
            memo_ana[num] = True
        else:
            memo_ana[num] = False
        # print "ana: " + str(num) + " ana " + str(memo_ana[num]) + " num " + str(num) + " equals " + str(num)[i:] + " . " + str(num)[:-i][::-1]
        return memo_ana[num]

def solve(lower_limit, upper_limit):
    num_root = int(math.ceil(math.sqrt(lower_limit)))
    count = 0
    while num_root <= int(math.sqrt(upper_limit)):
        num = num_root ** 2
        if num in memo:
            count += memo[num]
        else:
            memo[num] = isFairAndSquare(num)
            count += memo[num]
            # print "num: " + str(num) + " FaS " + str(isFairAndSquare(num))
        num_root += 1 
    return count

def main():
    try:
        args = sys.argv[1:]
        if len(args) != 1:
            raise Exception("Error: Expected only 1 argument.")
        if args[0][-2:] != "in":
            raise Exception("Error: Expected .in file type.")
        input = open(args[0], 'r')
        output = open(args[0][:-2] + "out", 'w')

        total_cases = int(input.readline())

        for case in range(1, total_cases + 1):
            print "working on case#:" + str(case)
            line = (input.readline()).split()
            a, b = int(line[0]), int(line[1])

            output.write("Case #{0}: {1}".format(case, solve(a, b)) + "\n")
            
    except Exception as e:
        print e.args[0]

    print "DONE."

if __name__ == "__main__":
    main()