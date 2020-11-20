# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

#http://wangwei007.blog.51cto.com/68019/1100742
class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
	def merge(self, intervals):
		sortedIntervals = sorted(intervals,key=self.sortIntervals)
		# print len(sortedIntervals)
		# print sortedIntervals[0].start
		# for ele in sortedIntervals:
			# print ele.start, ele.end
		Index = 0
		while Index < len(sortedIntervals)-1:
			if sortedIntervals[Index].end >= sortedIntervals[Index+1].start:
				newStart = sortedIntervals[Index].start
				newEnd = sortedIntervals[Index+1].end if sortedIntervals[Index].end<sortedIntervals[Index+1].end else sortedIntervals[Index].end
				sortedIntervals.pop(Index)
				sortedIntervals.pop(Index)
				sortedIntervals.insert(Index,Interval(newStart,newEnd))
			else:
				Index = Index + 1
		return sortedIntervals
	def sortIntervals(self,interval):
		return interval.start
		
intervals = []
intervals.append(Interval(1,4))
intervals.append(Interval(1,4))
s = Solution()
s.merge(intervals)