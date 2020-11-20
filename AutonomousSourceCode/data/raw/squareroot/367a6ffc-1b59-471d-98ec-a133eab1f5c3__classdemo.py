# A slightly longer demo of usings class, that includes the use of a
# class attribute.  There's only one of these per class, and it's
# accessible to all the instances.
#
# In this example the class variable is used to count the number of
# cars that have been created.
#
# Also demonstrated is the dynamic addition of a method to the class.

import math
class car():                     # or car(vehicle) if car is subclass of vehicle
    count = 0
    def __init__(self, newColor):          # Constructor
        car.count +=1                      # Class variable, counts cars created
        self.id = car.count
        self.color = newColor
        
    def setColor(self, nowColor):          # Method
        self.color = nowColor

    def show(self):                        # Method
        print "ID=%d, colour=%6s, #cars=%d" % (self. id, self.color, self.count)

blueCar = car("blue")       # create and show two cars
blueCar.show()       

redCar  = car("red")
redCar.show()

blueCar.setColor("Black")   # update blueCar
blueCar.show()

blueCar.windows = False     # add an attribute
print "blueCar: windows=", blueCar.windows


# Dynamically add a method called SquareRoot to the class

def mySquareRoot(x):
    return math.sqrt(x)

redCar.SquareRoot = mySquareRoot     # add a method to redCar
print redCar.SquareRoot(49)

print "*"*60
print "call blueCar.SquareRoot(64) - should fail"
print blueCar.SquareRoot(64)   # This fails - SQRT added ONLY to redCar
print "*"*60
