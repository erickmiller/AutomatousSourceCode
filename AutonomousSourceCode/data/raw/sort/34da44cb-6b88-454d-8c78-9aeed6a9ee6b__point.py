from operator import attrgetter

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "(%f, %f)" % (self.x, self.y)

    @staticmethod
    def sort(points):
        return sorted(points, key=attrgetter('x', 'y'))
