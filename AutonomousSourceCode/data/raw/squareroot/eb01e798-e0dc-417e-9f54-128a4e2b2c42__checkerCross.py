__author__ = "BeepC"

from tkinter import *


class Board:

    squares = {}
    active_square = None
    active_state = -1
    active_x = -1
    active_y = -1
    last_x = -1
    last_y = -1
    dragging = False
    clicked = False
    drag_plane = ""
    drag_coord = -1

    def __init__(self, master, x, y, launcher_used):

        self.frame = Frame(master, bg="GREY28")
        self.x = x
        self.y = y
        self.frame.tk_focusFollowsMouse()
        self.frame.grid()

        launcher_used.destroy()

        self.frame.bind_all("<Button-1>", self.start_mark)
        self.frame.bind_all("<ButtonRelease-1>", self.end_mark)
        self.frame.bind_all("<B1-Motion>", self.drag)

        for j in range(0, self.y):
            for i in range(0, self.x):
                square_id = "{0},{1}".format(i, j)
                self.squares[square_id] = Square(self.frame, self, i, j)

        self.frame.lift()

    def start_mark(self, event):

        self.clicked = True
        mouse_x = self.frame.winfo_pointerx() - self.frame.winfo_rootx()
        mouse_y = self.frame.winfo_pointery() - self.frame.winfo_rooty()
        event_grid = self.frame.grid_location(mouse_x, mouse_y)
        self.active_square = self.squares["{0},{1}".format(event_grid[0], event_grid[1])]
        self.active_x, self.active_y = [int(i) for i in self.active_square().split(',')]
        self.last_x = self.active_x
        self.last_y = self.active_y

        if self.active_square.state == 0:
            self.active_square.state = 1
        elif self.active_square.state == 1:
            self.active_square.state = 2
        elif self.active_square.state == 2:
            self.active_square.state = 0

        self.active_state = self.active_square.state
        print(self.active_square())

    def drag(self, event):

        mouse_x = self.frame.winfo_pointerx() - self.frame.winfo_rootx()
        mouse_y = self.frame.winfo_pointery() - self.frame.winfo_rooty()
        event_grid = self.frame.grid_location(mouse_x, mouse_y)
        event_x, event_y = [int(i) for i in event_grid]

        if event_x < 0:
            event_x = 0
        elif event_x >= self.x:
            event_x = self.x - 1

        if event_y < 0:
            event_y = 0
        elif event_y >= self.y:
            event_y = self.y - 1

        event_square = self.squares["{0},{1}".format(event_x, event_y)]

        if self.drag_coord != -1:
            self.drag_mark(event_square, event_x, event_y)
            return None

        if self.clicked is True and self.dragging is False:

            if self.active_x == event_x and self.active_y != event_y:
                    self.drag_coord = event_x
                    self.drag_plane = "V"
                    self.dragging = True
            elif self.active_y == event_y and self.active_x != event_x:
                    self.drag_coord = event_y
                    self.drag_plane = "H"
                    self.dragging = True

    def drag_mark(self, event_square, event_x, event_y):
        if self.drag_plane == "V" and event_y != self.last_y:

            event_square = self.squares["{0},{1}".format(self.drag_coord, event_y)]
            last_square = self.squares["{0},{1}".format(self.drag_coord, self.last_y)]

            if event_square.dragged is False and event_square != self.active_square:
                event_square.dragged = True
                event_square.state = self.active_state

            elif last_square.dragged is True and last_square != self.active_square:
                last_square.dragged = False
                last_square.state = last_square.prev_state

            self.last_y = event_y

        elif self.drag_plane == "H" and event_x != self.last_x:

            event_square = self.squares["{0},{1}".format(event_x, self.drag_coord)]
            last_square = self.squares["{0},{1}".format(self.last_x, self.drag_coord)]

            if event_square.dragged is False and event_square != self.active_square:
                event_square.dragged = True
                event_square.state = self.active_state

            elif last_square.dragged is True and last_square != self.active_square:
                last_square.dragged = False
                last_square.state = last_square.prev_state

            self.last_x = event_x

    def end_mark(self, event):

        mouse_x = self.frame.winfo_pointerx() - self.frame.winfo_rootx()
        mouse_y = self.frame.winfo_pointery() - self.frame.winfo_rooty()
        event_grid = self.frame.grid_location(mouse_x, mouse_y)
        event_x, event_y = [int(i) for i in event_grid]

        if event_x < 0:
            event_x = 0
        elif event_x >= self.x:
            event_x = self.x - 1

        if event_y < 0:
            event_y = 0
        elif event_y >= self.y:
            event_y = self.y - 1

        event_square = self.squares["{0},{1}".format(event_x, event_y)]

        for square in self.squares:
            self.squares[square].prev_state = self.squares[square].state
            self.squares[square].dragged = False

        self.clicked = False

        if self.dragging is True:

            event_square.prev_state = self.active_state
            event_square.dragged = False
            print(event_square())

            self.active_square = None
            self.active_state = 0
            self.dragging = False
            self.drag_coord = -1
            self.active_x = -1
            self.active_y = -1
            self.last_x = -1
            self.last_y = -1


class Square(Label):

    __state = 2
    __prev_state = 2
    __dragged = False

    def __init__(self, frame, board, x, y):

        super(Square, self).__init__(frame)

        self.frame = frame
        self.board = board
        self.x = x
        self.y = y

        self.tk_focusFollowsMouse()

        self.grid(row=self.y, column=self.x, padx=1, pady=1)
        self.config(image="", height=1, width=2, bg="BLANCHED ALMOND")

    def __call__(self):
        return "{0},{1}".format(self.x, self.y)

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, value):
        if value == 0:
            self.config(bg="BLACK")
        elif value == 1:
            self.config(bg="WHITE")
        else:
            self.config(bg="BLANCHED ALMOND")
        self.__state = value

    @property
    def prev_state(self):
        return self.__prev_state

    @prev_state.setter
    def prev_state(self, value):
        self.__prev_state = value

    @property
    def dragged(self):
        return self.__dragged

    @dragged.setter
    def dragged(self, value):
        self.__dragged = value


class CCLauncher(Frame):

    def __init__(self, master):

        super(CCLauncher, self).__init__(master)

        self.master = master
        self.button_frame = Frame(master)

        self.pack()
        self.button_frame.pack()

        self.get_x_entry = Entry(self)
        self.get_y_entry = Entry(self)
        self.get_x_label = Label(self, text="How many columns?")
        self.get_y_label = Label(self, text="How many rows?")
        self.ok_button = Button(self.button_frame, text="OK", command=self.click_ok, width=10)
        self.ok_button.bind("<Return>", self.click_ok)

        self.get_x_entry.grid(row=0, column=1, sticky='E')
        self.get_y_entry.grid(row=1, column=1, sticky='E')
        self.get_x_label.grid(row=0, column=0, sticky='W')
        self.get_y_label.grid(row=1, column=0, sticky='W')
        self.ok_button.pack()

        self.get_x_entry.focus_set()

    def click_ok(self, events=None):
        make_board(int(self.get_x_entry.get()), int(self.get_y_entry.get()), self.master)


def make_board(x, y, launcher_used):

    global checker_board
    global root
    root = Tk()
    root.tk_focusFollowsMouse()
    checker_board = Board(root, x, y, launcher_used)
    root.mainloop()

launcher_root = Tk()
launcher = CCLauncher(launcher_root)
launcher_root.mainloop()
