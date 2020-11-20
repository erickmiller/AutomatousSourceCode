from problem_utils import *

class SquareOfDigits:
    def getMax(self, data):
        input_array = data
        # You are given a String[] data representing a rectangular grid where each cell contains a digit.
        # Find the largest square in this grid that contains the same digit in all of its corner cells.
        find(largest(square, that(contains(same(digit, all, corner)))))
        # The sides of the square must be parallel to the sides of the grid.
        # If there is more than one such largest square, pick any one of them.
        # Return the number of cells in the square.
        # ROOT-0(root=Return-1(dep=number-3(det=the-2, prep_of=cells-5(prep_in=square-8(det=the-7)))))
        return(number(cells(square)))
        # Note that a single cell is also considered a square, so there will always be an answer.



def example0():
	cls = SquareOfDigits()
	input0 = ["12", "34"]
	returns = 1
	result = cls.getMax(input0)
	return result == returns


def example1():
	cls = SquareOfDigits()
	input0 = ["1255", "3455"]
	returns = 4
	result = cls.getMax(input0)
	return result == returns


def example2():
	cls = SquareOfDigits()
	input0 = ["42101", "22100", "22101"]
	returns = 9
	result = cls.getMax(input0)
	return result == returns


def example3():
	cls = SquareOfDigits()
	input0 = ["1234567890"]
	returns = 1
	result = cls.getMax(input0)
	return result == returns


def example4():
	cls = SquareOfDigits()
	input0 = ["9785409507", "2055103694", "0861396761", "3073207669", "1233049493", "2300248968", "9769239548", "7984130001", "1670020095", "8894239889", "4053971072"]
	returns = 49
	result = cls.getMax(input0)
	return result == returns



if __name__ == '__main__':
	print(example0())