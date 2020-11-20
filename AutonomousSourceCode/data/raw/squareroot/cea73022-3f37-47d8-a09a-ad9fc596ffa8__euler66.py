import decimal, mpmath
from mpmath import mp
from fractions import Fraction
from timeit import timeit
from operator import itemgetter
from math import sqrt, ceil, floor
from itertools import count, product, takewhile
from functools import reduce
from pdb import set_trace
from collections import namedtuple
from eulerUtils import (
    getSimpleFractOfContinuedFract, getContinuedFract)


EULER66_NUM_OF_X_SQUARE_MINUS_1S = 10000000
EULER66_MAX_Y_SQUARE_WHICH_IS_EASY_TO_FIND = 10000000
EULER66_STOP_D = 1001
ONES_DIGITS_SQUARES_CANT_HAVE = {2, 3, 7, 8}
EVEN_DIGITS = {0, 2, 4, 6 ,8}
ODD_DIGITS = {1, 3, 5, 7, 9}
ONES_DIGIT_TO_TENS_DIGITS_SQUARES_CAN_HAVE = {  0: {0},
                                                1: EVEN_DIGITS,
                                                4: EVEN_DIGITS,
                                                5: {2},
                                                6: ODD_DIGITS,
                                                9: EVEN_DIGITS}
DIGITS_SQUARES_CAN_END_WITH = { '00',
                                '01', '21', '41', '61', '81',
                                '04', '24', '44', '64', '84',
                                '25',
                                '16', '36', '56', '76', '96',
                                '09', '29', '49', '69', '89'}

DIGIT_TO_COMPLEMENT_TO_TEN_MUL_DICT = { 0: 10,
                                        1: 10,
                                        2: 5,
                                        3: 10,
                                        4: 5,
                                        5: 2,
                                        6: 5,
                                        7: 10,
                                        8: 5,
                                        9: 10 }
EULER66_NEEDED_PRECISION_IN_DIGITS = 100
EULER66_NEEDED_PRECISION_IN_BITS = 150
EULER66_D_ROOT_MUL_Y_MIN_FIRST_DIGIT_AFTER_DEC_POINT = 9
EULER66_D_ROOT_MUL_Y_MIN_VAL_AFTER_DEC_POINT = 0.9999

BASE_ONES_DIGIT_TO_SQUARE_ONES_DIGIT_DICT = {   0: 0,
                                                1: 1,
                                                2: 4,
                                                3: 9,
                                                4: 6,
                                                5: 5,
                                                6: 6,
                                                7: 9,
                                                8: 4,
                                                9: 1    }

ONES_DIGITS_SQUARES_CAN_END_WITH = BASE_ONES_DIGIT_TO_SQUARE_ONES_DIGIT_DICT.values()

EULER66_MAX_FRACT_TO_REFER_TO_AS_ZERO = 0.000000001
EULER66_MIN_FRACT_TO_REFER_TO_AS_ONE = 0.999999999


def euler66(stopD=EULER66_STOP_D):
    # a set of squares doesn't help here.. too many squares 
    # (e.g. a set of 20m squares is ~1.5GB of my precious RAM).
    decimal.getcontext().prec = EULER66_NEEDED_PRECISION_IN_DIGITS
    potentDsList = [d for d in range(stopD) if not sqrt(d).is_integer()]

    potentialDToMinYSquareDict = {potentD: getMinXForDByContinuedFract(
        potentD) for potentD in potentDsList}
    return max(potentialDToMinYSquareDict.items(), key=itemgetter(1))


def getMinXForDByContinuedFract(d):
    dRootContinuedFract = getContinuedFract(
        decimal.Decimal(d).sqrt(), 
        EULER66_MAX_FRACT_TO_REFER_TO_AS_ZERO,
        EULER66_MIN_FRACT_TO_REFER_TO_AS_ONE)
    for numOfRepeatsOfPeriodicTerms in count(1):
        potentXDivPotentYAsSimpleFract = getSimpleFractOfContinuedFract(
            dRootContinuedFract.intPart,
            (dRootContinuedFract.periodicTermsList * (
                numOfRepeatsOfPeriodicTerms))[:-1])
        potentX, potentY = (potentXDivPotentYAsSimpleFract.numerator, 
                            potentXDivPotentYAsSimpleFract.denominator)
        if 1 == (potentX ** 2 - d * potentY ** 2):
            print('d: {0}, x: {1}, y: {2}'.format(d, potentX, potentY))
            return potentX
    #print(getSimpleFractOfContinuedFract(6, [1]))
    #print(getSimpleFractOfContinuedFract(7, [3, 1, 1, 3]))
    #print(getSimpleFractOfContinuedFract(7, [3, 1, 1, 3, 14, 3, 1, 1, 3]))





def getPotentialSolutionsToEuler66(stopD=EULER66_STOP_D):
    dList = [d for d in range(stopD) if not safeHasSquareRoot(d)]
    return filter(lambda d: getMinYSquareForD2(
        d, EULER66_MAX_Y_SQUARE_WHICH_IS_EASY_TO_FIND) is None, dList)


def getHardMinXForD(d):
    decimal.getcontext().prec = EULER66_NEEDED_PRECISION_IN_DIGITS
    dRoot = decimal.Decimal(d).sqrt()

    print(1 / dRoot)
    
    potentY = decimal.Decimal(1)
    while True:
        '''
        print((1 / zeroLeftToDecPoint(dRoot * potentY)).to_integral(
            rounding=decimal.ROUND_FLOOR))
        '''
        potentY *= floor(1 / zeroLeftToDecPoint(dRoot * potentY))
        potentX = (potentY ** 2 * d + 1).sqrt()
        if potentX == floor(potentX):
            print(d, potentX)
            return potentX
        print('potentY: {0}, potentY * dRootint: {1}, complexOne: {2}'.format(
            int(potentY), potentY * dRoot, int(floor(dRoot * potentY * 10) % 10)))
        potentY *= DIGIT_TO_COMPLEMENT_TO_TEN_MUL_DICT[floor(dRoot * potentY * 10) % 10]
        print('potentY: {0}, potentY * dRootint: {1}'.format(
            int(potentY), int(potentY * dRoot)))
        print()
        set_trace()

def getHardMinXForD2(d):
    decimal.getcontext().prec = EULER66_NEEDED_PRECISION_IN_DIGITS
    dRoot = decimal.Decimal(d).sqrt()

    for potentY, dRootMulPotentY in multiplesGenerator(dRoot):
        '''
        print(dRootMulPotentY, dRootMulPotentY.adjusted() + 1)
        print(dRootMulPotentY, dRootMulPotentY.as_tuple().digits[
            dRootMulPotentY.adjusted() + 1])
        '''
        if EULER66_D_ROOT_MUL_Y_MIN_FIRST_DIGIT_AFTER_DEC_POINT <= (
                dRootMulPotentY.as_tuple().digits[dRootMulPotentY.adjusted() + 1]):
            potentX = (d * potentY ** 2 + 1).sqrt()
            #print(potentX)
            if potentX == floor(potentX):
                print(d, potentX)
                return potentX


def multiplesGenerator(base):
    currProduct = decimal.Decimal(base)
    for currMulVal in count(1):
        yield (decimal.Decimal(currMulVal), currProduct)
        currProduct += base


def getHardMinYForD3(d):
    '''
    failed at 61 when used 120 bits for precision (succeeded at 53, 46)
    '''
    print('trying {}'.format(d))
    mp.prec = EULER66_NEEDED_PRECISION_IN_BITS

    dRoot = mp.mpf(d).sqrt()

    for potentY, dRootMulPotentY in multiplesGenerator2(dRoot):
        if EULER66_D_ROOT_MUL_Y_MIN_VAL_AFTER_DEC_POINT < zeroLeftToDecPoint(
                dRootMulPotentY):
            print(potentY)
            if mpmath.isint((d * potentY ** 2 + 1).sqrt()):
                print(d, potentY)
                print()
                return potentY


def multiplesGenerator2(base):
    currProduct = mp.mpf(base)
    for currMulVal in count(1):
        yield (mp.mpf(currMulVal), currProduct)
        currProduct += base


def getHardMinYForD4(d):
    print('trying {}'.format(d))
    mp.prec = EULER66_NEEDED_PRECISION_IN_BITS

    dRoot = mp.mpf(d).sqrt()

    for potentY, dRootMulPotentY in multiplesGenerator3(dRoot):
        if EULER66_D_ROOT_MUL_Y_MIN_VAL_AFTER_DEC_POINT < zeroLeftToDecPoint(
                dRootMulPotentY):
            print(potentY)
            if ((int(dRootMulPotentY) + 1) ** 2) == (d * potentY ** 2 + 1):
                print(d, potentY)
                print()
                return potentY


def multiplesGenerator3(base):
    currProduct = mp.mpf(base)
    for currMulVal in count(1):
        yield (currMulVal, currProduct)
        currProduct += base


def powersGenerator(base=10, startExponent=0):
    currPower = base ** startExponent
    while True:
        yield currPower
        currPower *= base


def zeroLeftToDecPoint(num):
    return num - floor(num)


def getMinYForD(d):
    for y in count(1):
        if safeHasSquareRoot3(d * y ** 2 + 1):
            print(d, y)
            return y


def getMinYSquareForD2(d, stopYSquare=1000000000000000000000000):
    for ySquare in takewhile(lambda ySquare: ySquare < stopYSquare, 
                            squaresGenerator()):
        if safeHasSquareRoot3(d * ySquare + 1):
            print('d: {0}, ySquare: {1}'.format(d, ySquare))
            return ySquare


def getHardMinYSquareForD5(d): # almost identical to getMinYSquareForD2
    # best so far. even better than getHardMinYForD4.
    for ySquare in squaresGenerator():
        if safeHasSquareRoot3(d * ySquare + 1):
            print('d: {0}, ySquare: {1}'.format(d, ySquare))
            return ySquare


def getHardMinYSquareForD6(d):
    for ySquare in euler66PotentialYSquaresGenerator(d):
        if safeHasSquareRoot6(d * ySquare + 1):
            print('d: {0}, ySquare: {1}'.format(d, ySquare))
            return ySquare


def getHardMinYSquareForD7(d):
    # maybe slightly better than getHardMinYSquareForD5, but not as beautiful.
    ySquare = 1
    for diffToNextSquare in count(3, 2):
        if safeHasSquareRoot3(d * ySquare + 1):
            print('d: {0}, ySquare: {1}'.format(d, ySquare))
            return ySquare
        ySquare += diffToNextSquare


def getHardMinYSquareForD8(d): 
    for ySquare in squaresGenerator():
        if isMaybeAPerfectSquare2(d * (ySquare % 100) + 1) and (
                safeHasSquareRoot(d * ySquare + 1)):
            print('d: {0}, ySquare: {1}'.format(d, ySquare))
            return ySquare


def isMaybeAPerfectSquare(num):
    numOnesDigit = num % 10
    if numOnesDigit not in ONES_DIGITS_SQUARES_CANT_HAVE:
        numTensDigit = num // 10 % 10
        return numTensDigit in ONES_DIGIT_TO_TENS_DIGITS_SQUARES_CAN_HAVE[
                numOnesDigit]
    return False


def isMaybeAPerfectSquare2(num):
    return ((num % 10) not in ONES_DIGITS_SQUARES_CANT_HAVE) and (
        (num // 10 % 10) in ONES_DIGIT_TO_TENS_DIGITS_SQUARES_CAN_HAVE[
                (num % 10)])


def getMinYForD3(d, stopY=None):
    if stopY is None:
        ysToTry = count(1)
    else:
        ysToTry = range(1, stopY)
    dRoot = d ** 0.5
    for y in ysToTry:
        # is dRoot * y safe??? what if the float is too big???
        if (ceil(dRoot * y) ** 2) == (d * y ** 2 + 1):
            print(d, ceil(dRoot * y))
            return y


def safeHasSquareRoot2(num):
    # really slow.
    lowMaybeRoot = 0
    highMaybeRoot = num
    while lowMaybeRoot <= highMaybeRoot:
        midMaybeRoot = (lowMaybeRoot + highMaybeRoot) // 2
        midMaybeRootSquare = midMaybeRoot ** 2
        if midMaybeRootSquare == num:
            return True
        elif midMaybeRootSquare < num:
            lowMaybeRoot = midMaybeRoot + 1
        else:
            highMaybeRoot = midMaybeRoot - 1

    return False


def safeHasSquareRoot3(num):
    # best so far.
    numOnesDigit = num % 10
    if numOnesDigit not in ONES_DIGITS_SQUARES_CANT_HAVE:
        numTensDigit = num // 10 % 10
        return (numTensDigit in ONES_DIGIT_TO_TENS_DIGITS_SQUARES_CAN_HAVE[
                numOnesDigit]) and safeHasSquareRoot(num)
    return False


def safeHasSquareRoot6(num): 
    '''
    assuming the square was received from euler66PotentialYSquaresGenerator
    '''
    return ((num // 10 % 10) in ONES_DIGIT_TO_TENS_DIGITS_SQUARES_CAN_HAVE[
        num % 10]) and safeHasSquareRoot(num)


def safeHasSquareRoot4(num):
    if num > 1000000:
        numOnesDigit = num % 10
        if numOnesDigit not in ONES_DIGITS_SQUARES_CANT_HAVE:
            numTensDigit = num // 10 % 10
            return (numTensDigit in ONES_DIGIT_TO_TENS_DIGITS_SQUARES_CAN_HAVE[
                    numOnesDigit]) and safeHasSquareRoot(num)
        return False
    else:
        return safeHasSquareRoot(num)


def safeHasSquareRoot5(num):
    # not so good
    numAsStr = str(num)
    return (numAsStr[-2:] in DIGITS_SQUARES_CAN_END_WITH) and safeHasSquareRoot(num)


def safeHasSquareRoot(num):
    return mpmath.isint(mpmath.sqrt(num))


def euler66PotentialYSquaresGenerator(d):
    for ySquare in squaresGenerator():
        if ((d * (ySquare % 10) + 1) % 10) in ONES_DIGITS_SQUARES_CAN_END_WITH:
            yield ySquare


def squaresGenerator():
    currSquare = 1
    for diffToNextSquare in count(3, 2):
        yield currSquare
        currSquare += diffToNextSquare


def squaresGeneratorEx(startBase=1, stopBase=10000000):
    startDiff = startBase * 2 + 1
    stopDiff = stopBase * 2 - 1
    currSquare = startBase ** 2
    for diffToNextSquare in range(startDiff, stopDiff, 2):
        yield currSquare
        currSquare = currSquare + diffToNextSquare


def checkSafeHasSquareRoot():
    list(map(safeHasSquareRoot, range(0, 100000000, 13)))






if __name__ == '__main__':
    print(euler66())
    #timeFunc('getHardMinYForD8', '996')
