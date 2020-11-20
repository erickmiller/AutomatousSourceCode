from Tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, BOTTOM, LEFT
import tkMessageBox

MARGIN = 20  # Pixels around the board
SIDE = 50  # Width of every board cell.
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9  # Width and height of the whole board

def mapping(row, col):
    return [a+b for a in row for b in col]

digits = '123456789'
rows = 'ABCDEFGHI'
cols = digits
squares = mapping(rows, cols)
unitlist = ([mapping(rows, c) for c in cols] + [mapping(r, cols) for r in rows] + [mapping(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')]) #cols, rows, boxes
units = dict((square, [u for u in unitlist if square in u]) for square in squares) #col, row, and box for each square
peers = dict((square, set(sum(units[square],[]))-set([square])) for square in squares) #unit for each square in unit of s, but not s

#possibilities is dict mapping each square to every value it can have
#possibilities[s] is specific square

def parse_grid(board):
    possibilities = dict((square, digits) for square in squares) #each square has every possible answer
    for square,digit in grid_values(board).items():
        if digit in digits and not assign(possibilities, square, digit): #assign if d is a digit
            return False
    return possibilities

def grid_values(board):
    values = [c for c in board if c in digits or c in '0.'] #list of squares values (0 or . for empty/unknown squares)
    return dict(zip(squares, values)) #map each square to its value

def assign(possibilities, square, digit):
    other_possibilities = possibilities[square].replace(digit, '') #other_values is every possiblity except digit
    if all(remove(possibilities, square, d2) for d2 in other_possibilities): #if those values are all invalid, found answer
        return possibilities
    else:
        return False

def remove(possibilities, square, digit): #eliminate d from values[s]
    if digit not in possibilities[square]:
        return possibilities #eliminated
    
    possibilities[square] = possibilities[square].replace(digit, '') #remove possibility from square
    
    if len(possibilities[square]) == 0:
        return False #removed last value, should be impossible
    
    elif len(possibilities[square]) == 1:
        d2 = possibilities[square]
        if not all(remove(possibilities, s2, d2) for s2 in peers[square]): #should be impossible
            return False
        
    for u in units[square]:
        dplaces = [square for square in u if digit in possibilities[square]] #valid places to put d
        if len(dplaces) == 0: #no valid places
            return False
        elif len(dplaces) == 1:
            if not assign(possibilities, dplaces[0], digit):
                return False
    return possibilities

def search(possibilities):
    if possibilities is False:
        return False
    if all(len(possibilities[square]) == 1 for square in squares): #if each square has one solution, solved
        return possibilities
    n, square = min((len(possibilities[square]), square) for square in squares if len(possibilities[square]) > 1) #find square with min guesses not already solved
    return find_element(search(assign(possibilities.copy(), square, digit)) for digit in possibilities[square]) #for each square, reduce the possiblities, go through each square (depth first)

def find_element(values):
    for e in values:
        if e:
            return e
    return False

class SudokuUI(Frame):
    
    def __draw_puzzle(self):
        self.canvas.delete("numbers")
        for i in xrange(9):
            for j in xrange(9):
                answer = self.puzzle[i][j]
                if answer != 0:
                    x = MARGIN + j * SIDE + SIDE / 2
                    y = MARGIN + i * SIDE + SIDE / 2
                    color = "black"
                    self.canvas.create_text(
                        x, y, text=answer, tags="numbers", fill=color
                    )

    def __draw_grid(self):
        """
        Draws grid divided with blue lines into 3x3 squares
        """
        for i in xrange(10):
            color = "blue" if i % 3 == 0 else "gray"

            x0 = MARGIN + i * SIDE
            y0 = MARGIN
            x1 = MARGIN + i * SIDE
            y1 = HEIGHT - MARGIN
            self.canvas.create_line(x0, y0, x1, y1, fill=color)

            x0 = MARGIN
            y0 = MARGIN + i * SIDE
            x1 = WIDTH - MARGIN
            y1 = MARGIN + i * SIDE
            self.canvas.create_line(x0, y0, x1, y1, fill=color)

    def __initUI(self):
        self.parent.title("Sudoku Solver")
        self.pack(fill=BOTH)
        self.canvas = Canvas(self,
                             width=WIDTH,
                             height=HEIGHT)
        self.canvas.pack(fill=BOTH, side=TOP)

        f = Frame(width=100)
        f.pack()

        solve_button = Button(f, text="Solve", command=self.__solve)
        solve_button.pack(side=LEFT)

        clear_button = Button(f, text="Clear", command=self.__clear)
        clear_button.pack(side=LEFT)


        self.__draw_grid()
        self.__draw_puzzle()

        self.canvas.bind("<Button-1>", self.__cell_clicked)
        self.canvas.bind("<Key>", self.__key_pressed)
        self.canvas.bind("<Left>", self.__go_left)
        self.canvas.bind("<Right>", self.__go_right)
        self.canvas.bind("<Up>", self.__go_up)
        self.canvas.bind("<Down>", self.__go_down)
    
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent

        self.row, self.col = -1, -1

        self.puzzle = []

        for i in range(9):
            self.puzzle.append([])
            for j in range(9):
                self.puzzle[i].append(0)

        self.convert()

        self.__initUI()

    def reset(self):
        for i in range(9):
            for j in range(9):
                self.puzzle[i][j] = 0

    def convert(self):
        self.string = ''.join([str(cell) for sub in self.puzzle for cell in sub])

    def __draw_cursor(self):
        self.canvas.delete("cursor")
        if self.row >= 0 and self.col >= 0:
            x0 = MARGIN + self.col * SIDE + 1
            y0 = MARGIN + self.row * SIDE + 1
            x1 = MARGIN + (self.col + 1) * SIDE - 1
            y1 = MARGIN + (self.row + 1) * SIDE - 1
            self.canvas.create_rectangle(
                x0, y0, x1, y1,
                outline="red", tags="cursor"
            )

    def __cell_clicked(self, event):
        x, y = event.x, event.y
        if (MARGIN < x < WIDTH - MARGIN and MARGIN < y < HEIGHT - MARGIN):
            self.canvas.focus_set()

            # get row and col numbers from x,y coordinates
            row, col = (y - MARGIN) / SIDE, (x - MARGIN) / SIDE

            #if cell was selected already - deselect it
            if (row, col) == (self.row, self.col):
                self.row, self.col = -1, -1
            else:
                self.row = row
                self.col = col
        else:
            self.row, self.col = -1, -1

        self.__draw_cursor()

    def __go_up(self, event):
        if self.row >= 1 and self.row <= 8:
            self.row -= 1
            self.__draw_cursor()

    def __go_down(self, event):
        if self.row >= 0 and self.row <= 7:
            self.row += 1
            self.__draw_cursor()

    def __go_right(self, event):
        if self.col >= 0 and self.col <= 7:
            self.col += 1
            self.__draw_cursor()

    def __go_left(self, event):
        if self.col >= 1 and self.col <= 8:
            self.col -= 1
            self.__draw_cursor()

    def __key_pressed(self, event):
        if self.row >= 0 and self.col >= 0 and event.char in "1234567890":
            self.puzzle[self.row][self.col] = int(event.char)
            #self.col, self.row = -1, -1
            self.__draw_puzzle()
            self.__draw_cursor()        

    def __clear(self):
        self.reset()
        self.__draw_puzzle()

    def __solve(self):
        self.convert()
        raw = search(parse_grid(self.string))

        if raw == False:
            tkMessageBox.showinfo("Error", "Your sudoku is invalid. Check your input again")

        else:
            it = iter(sorted(raw.items()))

            temp = []
            i = 0
            
            while i < 81:
                temp.append(it.next()[1])
                i += 1

            for i in range(9):
                for j in range(9):
                    self.puzzle[i][j] = temp[i*9 + j]

            self.__draw_puzzle()
        
def main():
    root = Tk()
    SudokuUI(root)
    root.geometry("%dx%d" % (WIDTH, HEIGHT + 40))
    root.mainloop()

if __name__ == '__main__':
    main()
