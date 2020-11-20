from Tkinter import *

def draw_square(canvas, color, width, height, center):
  '''Does: Draws a square.
  Arguments: The canvas to draw on, the fill and outline color,
  the width and height of the square, and the center as a tuple.
  Returns: The square that is drawn.'''

  x1 = center[0] - width / 2
  x2 = center[0] + width / 2
  y1 = center[1] - height / 2
  y2 = center[1] + height / 2
  square = canvas.create_rectangle(x1, y1, x2, y2, fill = color, \
      outline = color)
  return square

if __name__ == '__main__':
  root = Tk()
  root.geometry('800x800')
  c = Canvas(root, width=800, height=800)
  c.pack()
  draw_square(c, 'red', 100, 100, (50, 50))
  draw_square(c, 'green', 100, 100, (750, 50))
  draw_square(c, 'blue', 100, 100, (50, 750))
  draw_square(c, 'yellow', 100, 100, (750, 750))

  root.mainloop()
