"""
Giving 2 quadratic equation, find the interception and graph out

"""


import numpy as np
from matplotlib.pyplot import *
 
np.set_printoptions(precision=2)
 
class intersect:
 
    def __init__(self, fun_1, fun_2):
 
        self.fun_1=fun_1
 
        self.fun_2=fun_2
 
        self.fun=np.array(self.fun_1 - self.fun_2)
 
        self.part_one=np.square(self.fun[1]) - 4* self.fun[0] *self.fun[2]
 
    def value_y(self, x):
 
        y=self.fun_1[0] * np.square(x) + self.fun_1[1] * x + self.fun_1[2]
 
        #   y=self.fun[0] * np.square(x) +self.fun[1] * x + self.fun[2]
 
        return y
 
    def single_root(self):
 
        x= -(self.fun[2]) / self.fun[1]
 
        return np.array([x, self.value_y(x)])
 
    def root_one(self):
 
        x=( -(self.fun[1]) + np.sqrt(self.part_one )) / (2 * self.fun[0])
 
        return np.array([x, self.value_y(x)])
 
    def root_two(self):
 
        x= (-(self.fun[1]) - np.sqrt(self.part_one ) )/ (2 * self.fun[0])
 
        return np.array([x, self.value_y(x)])   
 
    def final(self):
        x=linspace(-2,2, 200)
 
        y_1=self.fun_1[0]*np.square(x)+self.fun_1[1]*x+self.fun_1[2]
 
        y_2=self.fun_2[0]*np.square(x)+self.fun_2[1]*x+self.fun_2[2]
 
        figure()
        plot(x,y_1)
        plot(x,y_2)
        grid(True)
 
        if self.part_one < 0:
 
            print  "No Real Root"
 
        elif self.fun[0] == 0:
 
            print "Single Root: ", self.single_root()
 
        else:
 
            print "Root One: ", self.root_one() 
 
            print "Root Two: ", self.root_two()
 
if __name__ == '__main__':
 
#the equation will like y=x^2+4x+1
    y1=np.array([1,4,1])
 
    y2=np.array([-1,1,1])
 
    test=intersect(y1,y2) 
 
    test.final()
