from Tkinter import *

class Application(Frame):
    def say_hi(self):
        print "hi there, everyone!"

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi

        self.hi_there.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()



#root = Tk()
# e = Entry(root)
# e.pack()
# e.focus_set()
# b = Button(root, text="regular", width=10)
# b.pack()
# c = Button(root, text="mini")
# c.pack()
# w = Button(root, text="word")
# w.pack()
# mainloop()
# root.destroy()

def cross_product(A, B):
    the_list = []
    for a in A:
        for b in B:
            the_list.append(a+b)
    return the_list


digits   = '123456789'
rows     = 'ABCDEFGHI'
cols = digits
square_list = cross_product(rows, digits)
unit_list = []
for c in cols:
    unit_list.append(cross_product(rows, c))
for r in rows:
    unit_list.append(cross_product(r, cols))
for x in ('ABC', 'DEF', 'GHI'):
    for y in('123', '456', '789'):
        unit_list.append(cross_product(x, y))
units = {}
peers = {}
for x in square_list:
    the_list = []
    for y in unit_list:
        if x in y:
            the_list.append(y)
    units[x] = the_list
peers = dict((s, set(sum(units[s],[]))-set([s]))
             for s in square_list)

def grid_values(grid):
    char_list = []
    for c in grid:
        if c in digits or c in '0.':
            char_list.append(c)
    result = dict(zip(square_list, char_list))
    return result

# def parse_grid(grid):
#     """Convert grid to a dict of possible values, {square: digits}, or
#     return False if a contradiction is detected."""
#     ## To start, every square can be any digit; then assign values from the grid.
#     values = dict((s, digits) for s in square_list)
#     for s,d in grid_values(grid).items():
#         if d in digits and not assign(values, s, d):
#             return False ## (Fail if we can't assign d to square s.)
#     return values

