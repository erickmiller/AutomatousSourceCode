grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for item in grades:
        print item
print print_grades(grades)

def grades_sum(grades):
    total = 0
    for item in grades: 
        total += item
    return total
print grades_sum(grades)
    
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / len(grades)
    return average
print grades_average(grades)

def grades_variance(grades, average):
    sum_of_square = 0
    for item in grades:
        square_of_difference = (average - item) ** 2
        sum_of_square += square_of_difference
        variance = sum_of_square / len(grades)
    return variance
print grades_variance(grades, grades_average(grades))

def grades_std_deviation(variance):
    std_deviation = variance ** 0.5 # taking square root of variance
    return std_deviation
print grades_std_deviation(grades_variance(grades, grades_average(grades)))