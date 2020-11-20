#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Tuenti Challenge 3
#
# Challenge 11 - The escape from Pixel Island

# Look behind you, a Three-Headed Monkey!

import sys
import re
from PIL import Image, ImageDraw
from qrtools import QR

def parse_square(text):   
    if text[0] == 'w' or text[0] == 'b':
        return [ text[0], text[0], text[0], text[0] ]
        
    text = text[1:]
    square = []
    root = square
    pending = []
    
    while True:
        for c in text[0:4]:
            if c == 'p':
                square.append(None)
            else:
                square.append(c)
                
        text = text[4:]
        for i in range(len(square)):
            if square[i] is None:
                l = []
                square[i] = l
                pending.append(l)
        if len(pending) == 0:
            break
            
        square = pending[0]
        del pending[0]
    
    return root



    

def square_to_text(square):
    def square_to_text_inner(square):
        s = ''
        for elem in square:            
            if isinstance(elem, list):
                s += 'p'
            else:
                s += elem
                
        for elem in square:
            if isinstance(elem, list):
                s += square_to_text_inner(elem)
                
        return s
                
    text = square_to_text_inner(square)
    if text == 'wwww':
        return 'w'
    elif s == 'bbbb':
        return 'b'
    
    return 'p' + text
        

def add_squares(sq1, sq2):
    result = []
    for i in range(4):
        if not isinstance(sq1[i], list) and not isinstance(sq2[i], list):
            if sq1[i] == 'b' or sq2[i] == 'b':
                result.append('b')
            else:
                result.append('w')
        else:
            if not isinstance(sq1[i], list):
                c = sq1[i]
                sq1[i] = [ c, c, c, c ]
                
            if not isinstance(sq2[i], list):
                c = sq2[i]
                sq2[i] = [ c, c, c, c ]

            r = add_squares(sq1[i], sq2[i])
            if r == [ 'w', 'w', 'w', 'w' ]:
                r = 'w'
            elif r == [ 'b', 'b', 'b', 'b' ]:
                r = 'b'
            
            result.append(r)
            
    return result


def compress_square(square):
    result = []
    
    for elem in square:
        if isinstance(elem, list):
            if elem == [ 'w', 'w', 'w', 'w' ]:
                result.append('w')
            elif elem == [ 'b', 'b', 'b', 'b' ]:
                result.append('b')
            else:
                result.append(compress_square(elem))
        else:
            result.append(elem)

    return result
    

def get_square_depth(square, level):
    max_level = level
    
    for elem in square:
        if isinstance(elem, list):
            max_level = max(max_level, get_square_depth(elem, level + 1))
                
    return max_level


def get_square_size(square):
    
    depth = get_square_depth(square, 1)
    return 2**depth

   


def create_png(filename, square, max_level):
    
    def paint_png(draw, square, x0, y0, x1, y1, level, max_level):
        
        xh = (x0 + x1) // 2
        yh = (y0 + y1) // 2
        
        rects = [ ((xh, y0), (x1, yh)),
                  ((x0, y0), (xh, yh)),
                  ((x0, yh), (xh, y1)),
                  ((xh, yh), (x1, y1))]
                  
        
        for elem, rect in zip(square, rects):
            draw_rect = ((rect[0][0], rect[0][1]), (rect[1][0] - 1, rect[1][1] - 1))
            if not isinstance(elem, list):
                if elem == 'b':
                    color = 0
                else:
                    color = 1
                    
                draw.rectangle(draw_rect, fill = color)

            else:
                if level == max_level:
                    draw.rectangle(draw_rect, fill = 0)
                else:
                    paint_png(draw, elem, rect[0][0], rect[0][1], rect[1][0], rect[1][1], level + 1, max_level)
                                    
    
    max_level = min(get_square_depth(square, 1), max_level)
    size = 2**max_level
    
    im = Image.new('1', (size, size), 1)
    
    draw = ImageDraw.Draw(im)
    paint_png(draw, square, 0, 0, size, size, 1, max_level)
    
    # Resize the Image to avoid problems decoding
    im2 = im.resize((size * 3, size * 3))    
    im2.save(filename, "PNG")
    
    
import unicodedata

if __name__ == '__main__':
    resolution_level = 9
    
    num_cases = int(sys.stdin.readline())
    
    for num_case in range(num_cases):
        text_squares = sys.stdin.readline().rstrip('\r\n').split()

        squares = [ parse_square(s) for s in text_squares ]

        s = squares[0]
        
        for i in range(1, len(squares)):            
            s = add_squares(s, squares[i])       
               
        qrname = u'case%d_sum.png' % (num_case + 1)
        create_png(qrname, s, resolution_level)
        
        myCode = QR(filename=qrname)
        if myCode.decode():
            #m = md5.new()
            #m.update(myCode.data_to_string())
            #print m.hexdigest()
            secret = myCode.data_to_string()
            # Strip non iso-8859-1 characters
            secret = secret.decode('utf-8')
            secret = secret.encode('iso-8859-1', 'ignore')
            print secret
            
            

