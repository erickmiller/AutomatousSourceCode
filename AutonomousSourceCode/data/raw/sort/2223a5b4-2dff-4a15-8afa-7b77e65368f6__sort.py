from operator import attrgetter

class Sort():
    def sort(self, results):
        raise NotImplementedError("You have not implemented the sort method")

class RatingSort(Sort):
    #sort results in descending order by rating
    def sort(self, results):
        return sorted(results, key=attrgetter('rating'), reverse=True)

class AvailabilitySort(Sort):
    #sort results in ascending order by availability
    def sort(self, results):
        return sorted(results, key=attrgetter('availability'))
