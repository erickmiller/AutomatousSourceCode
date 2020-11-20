__author__ = 'Antony Cherepanov'

from Objects import Point, PointException


class SortBy(object):
    X_COORD = 0
    Y_COORD = 1


def Start():
    input = [Point(1, 1), Point(5, 7), Point(3, 0), Point(6, 2), Point(10, 10),
        Point(2, 1), Point(0, 10), Point(6, 5), Point(7, 2)]

    result = ClosestPoints(input)
    print "result = ", result


def ClosestPoints(t_input):
    """
     Get two closest points. Algorithm based on Merge Sort
     @input:
     - list of point objects
     @output:
     - list of two points
    """

    pointsSortedX = MergeSortForPoints(t_input, SortBy.X_COORD)
    for i in pointsSortedX:
        print i
    pointsSortedY = MergeSortForPoints(t_input, SortBy.Y_COORD)
    for i in pointsSortedY:
        print i


def MergeSortForPoints(t_points, t_sortByCoord):
    length = len(t_points)
    if 2 < length:
        halfLength = length / 2
        leftHalf = t_points[:halfLength]
        rightHalf = t_points[halfLength:]
        sortedLeft = MergeSortForPoints(leftHalf, t_sortByCoord)
        sortedRight = MergeSortForPoints(rightHalf, t_sortByCoord)
        i = 0
        j = 0
        result = list()
        for k in range(length):
            if len(sortedLeft) <= i:
                result.extend(sortedRight[j:])
                break

            if len(sortedRight) <= j:
                result.extend(sortedLeft[i:])
                break

            # Choose by which coordinate we should sort
            if t_sortByCoord == SortBy.X_COORD:
                leftPointCoord = sortedLeft[i].GetX()
                rightPointCoord = sortedRight[j].GetX()
            else:
                leftPointCoord = sortedLeft[i].GetY()
                rightPointCoord = sortedRight[j].GetY()

            # Merge sorted halves
            if leftPointCoord < rightPointCoord:
                result.append(sortedLeft[i])
                i += 1
            else:
                result.append(sortedRight[j])
                j += 1

        return result

    else:
        if 1 == length:
            return t_points
        elif 2 == length:
            # Choose by which coordinate we should sort
            if t_sortByCoord == SortBy.X_COORD:
                first = t_points[0].GetX()
                second = t_points[1].GetX()
            else:
                first = t_points[0].GetY()
                second = t_points[1].GetY()

            if first < second:
                return t_points
            else:
                return [t_points[1], t_points[0]]


Start()