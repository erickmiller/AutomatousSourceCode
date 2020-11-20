import Tkinter


def draw_square(canvas, color, size, position):
    """

    :param canvas:
    :param color:
    :param size:
    :param position:
    :return handle:

    Takes a Tkinter canvas, a color string, an integer size, and a tuple of
    x,y coordinates for the center of the rectangle.

    Returns the handle from the created rectangle.
    """
    upper_x = position[0] - size / 2
    upper_y = position[1] - size / 2

    lower_x = position[0] + size / 2
    lower_y = position[1] + size / 2

    return canvas.create_rectangle(upper_x,
                                   upper_y,
                                   lower_x,
                                   lower_y,
                                   fill=color,
                                   outline=color)


if __name__ == '__main__':
    root = Tkinter.Tk()
    root.geometry('800x800')

    c = Tkinter.Canvas(root, width=800, height=800)
    c.pack()

    draw_square(c, 'red', 100, (50, 50))
    draw_square(c, 'green', 100, (750, 50))
    draw_square(c, 'blue', 100, (50, 750))
    draw_square(c, 'yellow', 100, (750, 750))

    root.mainloop()
