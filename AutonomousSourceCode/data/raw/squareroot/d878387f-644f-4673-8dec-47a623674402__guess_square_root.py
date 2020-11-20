# Question: What is square root of 6427?

import random as rand

class FindSquareRoot:

    def __init__(self,target,sensitivity):
        self.tg = target
        self.sy = sensitivity
    
    def setup(self):
        self.ulim = self.tg + (self.tg * self.sy)
        self.llim = self.tg - (self.tg * self.sy)
    
    def test_sqrt(self,val):
        if (val**2 <= self.ulim) and (val**2 >= self.llim):
            return True
        else:
            return False
    
    def get_next_value(self):
        # Guess the next root value
        # in this case, simply increment the current root
        if (self.rt**2 > self.tg):
            self.rt = self.rt - self.sy
        elif (self.rt**2 < self.tg):
            self.rt = self.rt + self.sy
    
    def random_increment(self):
        self.rt = self.rt + ((0.5-rand.random())*2)

    def run(self):
        # Want to count how many steps
        self.steps = 0
        while not self.test_sqrt(val=self.rt):
            self.steps = self.steps + 1
            #self.get_next_root()
            self.random_increment()

    def print_answer(self):
        print 'The answer is: ' + str(self.rt)
        print 'Which gives:   ' + str(self.rt**2)
        print 'and it took:   ' + str(self.steps) + ' steps'
    
    def run_model(self,seedRoot):
        self.rt = seedRoot
        print 'Seed Root is: ' + str(seedRoot)        

        self.setup()
        self.run()
        self.print_answer()

def main():
    m = FindSquareRoot(target=642.0,sensitivity=0.001)
    m.run_model(seedRoot=32.0)

main()





